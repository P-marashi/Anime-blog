from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request, page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 8)
    articles = paginator.get_page(page)
    context = {

        "articles": articles,
    }
    return render(request, "blogs/Anime-blog.html", context)


def detail_article(request, slug):
    published_articles = Article.objects.published()[:10]
    context = {
        "published_articles": published_articles,
        "article": get_object_or_404(Article.objects.published(), slug=slug, status="p"),

    }
    return render(request, "blogs/show-detail.html", context)


def best_in_month(request):
    context = {
        "best_in_month": Article.objects.monthly_publish()
    }
    return render(request, "blogs/top-the-month.html", context)


def about_me(request):
    return render(request, "blogs/about-me.html")
