# Create your views here.
from django.shortcuts import render
from .models import Replies
from .serializer import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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



