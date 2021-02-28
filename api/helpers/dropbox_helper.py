import json
import logging
from api.helpers.api_fns.drop_box import dropbox_upload

logger = logging.getLogger(__name__)

def update_dropbox(summary,questions):
    dropbox_upload(summary,questions)
