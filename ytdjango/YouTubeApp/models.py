from django.db import models

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=100, blank=True, null=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.CharField(max_length=100)