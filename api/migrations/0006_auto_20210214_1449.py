# Generated by Django 3.1.6 on 2021-02-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_course_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Type',
            field=models.TextField(default='youtubeplaylist'),
        ),
        migrations.AddField(
            model_name='course',
            name='difficulty',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='course',
            name='enrolnum',
            field=models.TextField(default='0'),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.TextField(default=0.0),
        ),
        migrations.AddField(
            model_name='course',
            name='rating_count',
            field=models.BigIntegerField(default=0),
        ),
    ]