
''' How to use :
1) Video to text:
from transcribe import amazon_transcribe
result=(amazon_transcribe(audio_file_name))
#include .mp4 while passing file name

2)Drop-box Integration:
from drop_box import dropbox_upload
dropbox_upload(<String containing summary>,<String containing possible questions >)

3)Question generation API:
from pipelines import pipeline
print(pipeline("question-generation")(<string containing summary>))
'''