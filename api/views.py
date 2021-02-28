import os
import json
import logging
import uuid

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import View

from api.custom_storage import VideoStorage
from api.decorators.response import JsonResponseDecorator
from api.tasks import process_video
from api.models import Videos, Summary, Questions

logger = logging.getLogger(__name__)


@method_decorator(JsonResponseDecorator, name='dispatch')
class IndexView(View):
    """
    Returns the index view response
    """
    def get(self, request):
        return {
            'message': 'You are not supposed to be here'
        }


@method_decorator(JsonResponseDecorator, name='dispatch')
class PingView(View):
    """
    Returns the app status
    """

    def get(self, request):
        return {
            'message': 'Pong'
        }


@method_decorator(JsonResponseDecorator, name='dispatch')
class UploadVideoView(View):
    """
    Uploads the video
    """

    def post(self, request):
        file_obj = request.FILES.get('video', '')
        title = request.POST.get('title')
        title='sad'

        # Validation here e.g. file size/type check

        original_filename = file_obj.name
        ext = original_filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)

        file_directory_within_bucket = 'videos'

        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            filename
        )

        # Get custom media storage
        media_storage = VideoStorage()

        file_url = ''
        if not media_storage.exists(file_path_within_bucket): # Avoid overwriting existing file
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)
            logger.info(filename+'Video upload success')
        else:
            return {
                'status_code': 400,
                'data': 'Error: file-{filename} already exists at {file_directory} in bucket-{bucket_name}'.format(
                    filename=file_obj.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }

        video = Videos.objects.create(
            title=title,
            filename=filename
        )

        video = model_to_dict(video)
        # Add video for processing to celery tasks
        process_video.delay(video)
        
        return {
            'video': video,
            'file_url': file_url
        }


@method_decorator(JsonResponseDecorator, name='dispatch')
class ProcessedVideosView(View):
    """
    """

    def get(self, request):
        videos = Videos.objects.all()

        videos = model_to_dict(videos)
        
        return {
            'videos': videos,
        }

@method_decorator(JsonResponseDecorator, name='dispatch')
class ProcessedVideoView(View):
    """
    """

    def get(self, request):
        video_id = request.GET.get('id')
        
        video = Videos.objects.get(
            video_id=video_id
        )
        summary = Summary.objects.get(
            video_id=video
        )
        questions = Questions.objects.filter(
            video_id=video
        )

        video = model_to_dict(video)
        
        return {
            'video': model_to_dict(video),
            'summary': model_to_dict(summary),
            'questions': model_to_dict(questions)
        }