import logging

from celery.decorators import task
from celery.utils.log import get_task_logger

from api.helpers.summarizer_helper import summarize
from api.helpers.transcriber_helper import transcribe
from api.helpers.question_generator_helper import generate_questions
from api.models import Videos, Summary, Questions

logger = logging.getLogger(__name__)


@task(bind=True, name="process_video", max_retries=10, default_retry_delay=60)
def process_video(self, video_obj):
    try:
        video = Videos.objects.get(video_id=video_obj["video_id"])

        logger.info('Processing file...')
        transcribed_text = transcribe(video_obj["filename"])
        logger.info('Transcription success!')
        
        # Summarize transcibed text
        logger.info('Summarizing text...')
        summarized_text = summarize(transcribed_text)
        summary = Summary.objects.create(
            video_id=video,
            text=summarized_text
        )
        logger.info('Summarized text!')
        
        # Generate questions from summary
        logger.info('Generating questions...')
        questions = generate_questions(summarized_text)
        for item in questions:
            print(item)
            print(item["question"])
            Questions.objects.create(
                video_id=video,
                question=item["question"],
                answer=item["answer"],
            )
        logger.info('Generated questions!')

        video.is_processed = True
        video.save()

        logger.info('Finished processing!')

    except Exception as e:
        raise self.retry(exc=e)