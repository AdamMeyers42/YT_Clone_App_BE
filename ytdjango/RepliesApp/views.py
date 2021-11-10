# Create your views here.
from django.shortcuts import render
from .models import Replies
from .serializer import ReplySerializer
from rest_framework.views import APIView
from rest_framework.views import Response 
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import HttpResponse


# Create your views here.

class RepliesList(APIView):
    
    def get(self, request):
        reply = Replies.objects.all()
        serializer = ReplySerializer (reply, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LikeReplies(APIView):

    def get_id(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        replies = self.get_id(pk)
        replies.like += 1
        replies.save()
        serializer = ReplySerializer(replies)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DislikeReplies(APIView):
    
    def get_id(self, pk):
        try:
            return Replies.objects.get(pk=pk)
        except Replies.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        replies = self.get_id(pk)
        replies.dislike += 1
        replies.save()
        serializer = ReplySerializer(replies)
        return Response(serializer.data, status=status.HTTP_200_OK)



