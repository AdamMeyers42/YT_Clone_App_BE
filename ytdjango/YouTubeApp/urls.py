from django.urls import path
from . import views 

urlpatterns = [
    path('YouTubeApp/', views.CommentList.as_view()),
]