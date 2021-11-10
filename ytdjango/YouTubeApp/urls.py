from django.urls import path
from . import views 

urlpatterns = [
    path('YouTubeApp/', views.CommentList.as_view()),
    path('RepliesApp/', views.RepliesList.as_view()),
]