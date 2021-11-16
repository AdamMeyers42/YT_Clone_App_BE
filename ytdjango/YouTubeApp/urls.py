from django.urls import path
from . import views 

urlpatterns = [
    # path('comments/', views.CommentList.as_view()),
    path('comments/like/<int:pk>/', views.LikeComment.as_view()),
    path('comments/dislike/<int:pk>/', views.DislikeComment.as_view()),
    path('comments/<video_id>/', views.CommentList.as_view())
]