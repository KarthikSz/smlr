import os
import magic

from django.core.exceptions import ValidationError

def validate_is_video(file):
    valid_mime_types = [
        'video/mp4',
        'video/x-msvideo',
        'video/mpeg',
        'video/ogg',
        'video/mp2t',
        'video/webm',
        'video/3gpp',
    ]
    valid_file_extensions = [
        'mp4',
        'avi',
        'mpeg',
        'ogg',
        'ts',
        'webm',
        '3gp'
    ]

    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')

    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')