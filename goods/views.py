from django.shortcuts import render, redirect, Http404
from . models import Good, Category
from django.http import Http404
from django.views.generic import ListView
from . forms import GoodsForm


class GoodsListView(ListView):
    model = Good
    template_name = "goods/goods.html"
    paginate_by = 100
    allow_empty = True
    filter = ''

    def get(self, request, *args, **kwargs):
        return super(GoodsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        print(filter.__dict__)
        return Good.objects.all().filter(is_good=True).order_by("id")


#def index(request):
#    form = GoodsForm()
#    context = {'form': form}
#    return render(request, "goods/cat1.html", context)


def detail(request, _id):
    try:
        good = Good.objects.get(pk=_id)
    except Good.DoesNotExist:
        raise Http404("Good does not exist")
    return render(request, "goods/detail.html", {"good": good.name, "id": good.id, "description": good.description})


#def goods_list(request):

#    form = GoodsForm()
#    context = {'form': form}
#    if request.method == 'GET':
#        print("произошел get запрос")
#    if request.method == 'POST':
#        print('произошел POST запрос')
#    return render(request, "goods/goods_seek.html", context)


def good_search(request, _id1=None, _id2=None, _id3=None, search=None):

    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            how_to_search = form.cleaned_data['how_to_search']
            search = form.cleaned_data['search']
            if _id1 is None and _id2 is None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
                goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                    'cat3').filter(is_good=True,  name__icontains=search).order_by('name')
                context = {'form': form, 'cat1': cat1, 'goods': goods}
                return render(request, "goods/categories4.html", context)

            elif _id1 is not None and _id2 is None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                         cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
                        is_good=True, name__icontains=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, name__icontains=search).order_by('name')
                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'goods': goods}
                return render(request, "goods/categories4.html", context)

            elif _id1 is not None and _id2 is not None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by(
                    'name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                             cat3=0).order_by('name')
                cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                     cat2=_id2,
                                                                                     cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                    'cat3').filter(is_good=True, name__icontains=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, cat2=_id2, name__icontains=search).order_by('name')
                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'goods': goods}
                return render(request, "goods/categories4.html", context)

            elif _id1 is not None and _id2 is not None and _id3 is not None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by(
                    'name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                             cat3=0).order_by(
                    'name')
                cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                     cat2=_id2,
                                                                                     cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                 'cat3').filter(
                                is_good=True, name__icontains=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(
                        is_good=True, cat1=_id1, cat2=_id2, cat3=_id3, name__icontains=search).order_by('name')
                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'goods': goods}

                return render(request, "goods/categories4.html", context)

    else:
        form = GoodsForm()

    if _id1 is None and _id2 is None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        context = {'form': form, 'cat1': cat1}
        return render(request, "goods/categories4.html", context)

    elif _id1 is not None and _id2 is None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(is_good=True,
                                                    cat1=_id1).order_by('name')
        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'goods': goods}
        return render(request, "goods/categories4.html", context)

    elif _id1 is not None and _id2 is not None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by(
            'name')
        cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1, cat2=_id2,
                                                                                     cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
            is_good=True, cat1=_id1, cat2=_id2).order_by('name')
        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'goods': goods}
        return render(request, "goods/categories4.html", context)

    elif _id1 is not None and _id2 is not None and _id3 is not None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by(
            'name')
        cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1, cat2=_id2,
                                                                             cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
            is_good=True, cat1=_id1, cat2=_id2, cat3=_id3).order_by('name')
        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'goods': goods}
        return render(request, "goods/categories4.html", context)

    else:
        return Http404


def good_seek(request):

    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            how_to_search = form.cleaned_data['how_to_search']
            search = form.cleaned_data['search']
            if how_to_search:
                #good_list = Good.objects.all().filter(is_good=True, name__contains=search).order_by('name')
                filter = search
                #context = {'good_list': good_list}
                return redirect("seek/search_result", filter=filter)

    else:
        form = GoodsForm()

    deps = Good.objects.values_list('id', 'name', 'cat1', 'cat2', 'cat3').filter(is_good=False).order_by('name')
    string_num = deps.count()
    quant = string_num / 4 + 1 if string_num % 4 != 0 else string_num / 4
    col1 = Good.objects.values_list('id', 'name', 'cat1', 'cat2', 'cat3').filter(is_good=False).order_by('name')[0: quant]
    col2 = Good.objects.values_list('id', 'name', 'cat1', 'cat2', 'cat3').filter(is_good=False).order_by('name')[quant + 1: quant * 2]
    col3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2', 'cat3').filter(is_good=False).order_by('name')[quant * 2 + 1: quant * 3]
    col4 = Good.objects.values_list('id', 'name', 'cat1', 'cat2', 'cat3').filter(is_good=False).order_by('name')[quant * 3 + 1:]

    context = {'form': form, 'col1': col1, 'col2': col2, 'col3': col3, 'col4': col4}

    return render(request, "goods/categories3.html", context)