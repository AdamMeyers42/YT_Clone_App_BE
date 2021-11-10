from django.urls import path
from . import views 

urlpatterns = [
    path('RepliesApp/', views.RepliesList.as_view()),
    path('comments/like/<int:pk>/', views.LikeComment.as_view()),
    path('comments/dislike/<int:pk>/', views.DislikeComment.as_view())
    
]

