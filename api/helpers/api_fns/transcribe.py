import pandas as pd
import time
import boto3

transcribe = boto3.client('transcribe',
aws_access_key_id = "AKIAJK6DO2WYFHAX7NMA",
aws_secret_access_key = "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",
region_name = "ap-south-1")

def check_job_name(job_name):
  job_verification = True
  
  # all the transcriptions
  existed_jobs = transcribe.list_transcription_jobs()
  
  for job in existed_jobs['TranscriptionJobSummaries']:
    if job_name == job['TranscriptionJobName']:
      job_verification = False
      break

  if job_verification == False:
    command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
    if command.lower() == "y" or command.lower() == "yes":
      transcribe.delete_transcription_job(TranscriptionJobName=job_name)
    elif command.lower() == "n" or command.lower() == "no":
      job_name = input("Insert new job name? ")
      check_job_name(job_name)
    else: 
      print("Input can only be (Y/N)")
      command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
  return job_name

def amazon_transcribe(audio_file_name):
  job_uri = "s3://smlr/videos/"+audio_file_name
  # Usually, I put like this to automate the process with the file name
  # "s3://bucket_name" + audio_file_name 

  # Usually, file names have spaces and have the file extension like .mp3
  # we take only a file name and delete all the space to name the job
  job_name = (audio_file_name.split('.')[0])
  
  # file format
  file_format = audio_file_name.split('.')[1]

  # check if name is taken or not
  job_name = check_job_name(job_name)
  transcribe.start_transcription_job(
      TranscriptionJobName=job_name,
      Media={'MediaFileUri': job_uri},
      MediaFormat = file_format,
      LanguageCode='en-US')
  
  while True:
    result = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if result['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
      print("FAILED")
      break
    time.sleep(15)

  if result['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
    data = pd.read_json(result['TranscriptionJob']['Transcript']['TranscriptFileUri'])
  
  return data['results'][1][0]['transcript']