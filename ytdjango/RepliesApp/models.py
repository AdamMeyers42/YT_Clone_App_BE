from django.db import models

from django.db import models


class Replies(models.Model):
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    video_id = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    comment = models.ForeignKey('YouTubeApp.Comment',blank=True, null=True, on_delete=models.CASCADE)
# Create your models here.
