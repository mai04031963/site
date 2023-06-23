from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from . models import News
from django.http import Http404


# Create youfrr views here.
def news(request):
    news_list = News.objects.all()
    context = {"news_list": news_list,}
    return render(request, "news/news.html", context)
