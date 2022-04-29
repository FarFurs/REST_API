from django.urls import path
from . import views
# from rest_framework import routers


urlpatterns = [
    path('getArticle/', views.getArticle),
    path('getComment_all/', views.getComment_all),
    path('getComment_to_comments/', views.getComment_to_comments),
    path('getComment_to_articles/', views.getComment_to_articles),
    path('addArticle/', views.addArticle),
    path('addComment/', views.addComment)
]


