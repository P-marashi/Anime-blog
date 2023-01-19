from django.urls import path
from .views import index, detail_article, about_me, best_in_month

app_name = "blog"
urlpatterns = [
    path('', index, name="index"),
    path('page/<int:page>', index, name="index"),
    path('article/<slug:slug>', detail_article, name="article_detail"),
    path('best_in_month/', best_in_month, name="best_in_month"),
    path('about_me/', about_me, name="about_me"),
]
