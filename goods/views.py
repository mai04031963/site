from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
from . models import Good, Category
from django.http import Http404

def index(request):
    goods_list = Good.objects.all()
    context = {"goods_list": goods_list, }
    return render(request, "goods/index.html", context)


def detail(request, _id):
    try:
        good = Good.objects.get(pk=_id)
    except Good.DoesNotExist:
        raise Http404("Good does not exist")
    #result = good.name
    #return HttpResponse(result)
    return render(request, "goods/detail.html", {"good": good.name, "id": good.id, "description": good.description})


def results(request, _id):
    response = "You're looking for good %s."
    return HttpResponse(response % _id)


def vote(request, _id):
    return HttpResponse("You're choosing good № %s." % _id)


def good(request):
    return 'in good function'


def category(request):
    return 'in category function'