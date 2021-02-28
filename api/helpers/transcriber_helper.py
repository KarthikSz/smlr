import json
import logging
from api.helpers.api_fns.transcribe import amazon_transcribe

logger = logging.getLogger(__name__)

def transcribe(filename):
    return amazon_transcribe(filename)