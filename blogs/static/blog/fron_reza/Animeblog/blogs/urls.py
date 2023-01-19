from django.urls import path
from .views import index, detail_article,category,communication,about_me
app_name = "blog"
urlpatterns = [
    path('', index, name="index"),
    path('page/<int:page>', index, name="index"),
    path('article/<slug:slug>', detail_article, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/page/<int:page>', category, name="category"),
    path('communication/', communication, name="communication"),
    path('about_me/', about_me, name="about_me"),
]