from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all().order_by('-published_at')
    context = {
        'object_list': object_list
    }
    ordering = '-published_at'
    return render(request, template, context)