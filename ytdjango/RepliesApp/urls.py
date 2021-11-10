from django.urls import path
from . import views 

urlpatterns = [
    path('replies/', views.RepliesList.as_view()),
    path('replies/like/<int:pk>/', views.LikeReplies.as_view()),
    path('replies/dislike/<int:pk>/', views.DislikeReplies.as_view())
    
]

