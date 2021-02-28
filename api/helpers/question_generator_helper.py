import json
import logging
from api.helpers.api_fns.pipelines import pipeline

logger = logging.getLogger(__name__)

def generate_questions(summary):
    return pipeline("question-generation")(summary)