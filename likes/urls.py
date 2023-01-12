from django.urls import path
from likes import views

urlpatterns = [
    path('likes/<int:pk>/', views.Likes.as_view()),
]