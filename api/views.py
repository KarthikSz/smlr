import os
import json
import logging

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import View

from api.custom_storage import VideoStorage
from api.decorators.response import JsonResponseDecorator

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
class ProcessVideoView(View):
    """
    Uploads the video
    """

    def post(self, request):
        file_obj = request.FILES.get('video', '')

        # Validation here e.g. file size/type check

        # organize a path for the file in bucket
        file_directory_within_bucket = 'videos'

        # synthesize a full file path; note that we included the filename
        file_path_within_bucket = os.path.join(
            file_directory_within_bucket,
            file_obj.name
        )

        # Get custom media storage
        media_storage = VideoStorage()

        if not media_storage.exists(file_path_within_bucket): # Avoid overwriting existing file
            media_storage.save(file_path_within_bucket, file_obj)
            file_url = media_storage.url(file_path_within_bucket)

            return {
                'fileUrl': file_url,
            }
        else:
            return {
                'status_code': 400,
                'data': 'Error: file-{filename} already exists at {file_directory} in bucket-{bucket_name}'.format(
                    filename=file_obj.name,
                    file_directory=file_directory_within_bucket,
                    bucket_name=media_storage.bucket_name
                ),
            }

        return {
            'message': 'OK'
        }