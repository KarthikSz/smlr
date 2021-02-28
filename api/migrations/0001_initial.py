# Generated by Django 3.1.7 on 2021-02-28 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('video_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=2000, null=True)),
                ('filename', models.TextField(max_length=2000, unique=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('summary_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=20000, null=True)),
                ('video_id', models.ForeignKey(db_column='video_id', on_delete=django.db.models.deletion.CASCADE, to='api.videos')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(max_length=2000)),
                ('answer', models.TextField(max_length=2000, null=True)),
                ('video_id', models.ForeignKey(db_column='video_id', on_delete=django.db.models.deletion.CASCADE, to='api.videos')),
            ],
        ),
    ]
