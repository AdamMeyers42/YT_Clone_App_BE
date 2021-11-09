from rest_framework import serialiers 
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'video_id', 'like', 'dislike', 'comment']