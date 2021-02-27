from django.db import models


class Videos(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=2000, null=True)
    filename = models.TextField(max_length=2000, unique=True, null=False)
    is_processed = models.BooleanField(default=False)


class Summary(models.Model):
    summary_id = models.AutoField(primary_key=True)
    video_id = models.ForeignKey(Videos, db_column='video_id', on_delete=models.CASCADE)
    text = models.TextField(max_length=20000, null=True)


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    video_id = models.ForeignKey(Videos, db_column='video_id', on_delete=models.CASCADE)
    question = models.TextField(max_length=2000, null=False)