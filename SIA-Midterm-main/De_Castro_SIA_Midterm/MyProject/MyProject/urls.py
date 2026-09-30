from django.urls import path
from MyApp import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]