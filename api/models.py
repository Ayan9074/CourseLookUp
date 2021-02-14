from django.db import models


class Course(models.Model):
    title = models.TextField()
    description = models.TextField()
    link =models.TextField()
    img = models.TextField()
    web = models.TextField(default='none')
    section = models.TextField(default='none')
    rating = models.TextField(default=0.0)
    rating_count = models.TextField(default=0)
    enrolnum = models.TextField(default='0')
    difficulty = models.TextField(default='0')
    Type = models.TextField(default='youtubeplaylist')