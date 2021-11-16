from django.shortcuts import render
from rest_framework.serializers import Serializer
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.views import Response 
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import HttpResponse

class CommentList(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer (comment, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeComment(APIView):

    def get_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        comments = self.get_id(pk)
        comments.like += 1
        comments.save()
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DislikeComment(APIView):
    
    def get_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        comments = self.get_id(pk)
        comments.dislike += 1
        comments.save()
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)
