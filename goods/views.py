from django.shortcuts import render, redirect, Http404
from . models import Good, Category
from django.http import Http404
from django.core.paginator import Paginator
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


def detail(request, _id):
    try:
        good = Good.objects.get(pk=_id)
    except Good.DoesNotExist:
        raise Http404("Good does not exist")
    return render(request, "goods/detail.html", {"good": good.name, "id": good.id, "description": good.description})


def good_search(request, _id1=None, _id2=None, _id3=None, search=None):

    # обработка запроса поиска товара
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        if form.is_valid():
            how_to_search = form.cleaned_data['how_to_search']
            search = form.cleaned_data['search']
            # обработка строки поиска
            a = [s.strip() for s in search.split(" ")]
            if len(a) == 0:
                search = ''
            elif len(a) == 1:
                search = a[0]
            else:
                search = a[0]
                for i in range(1, len(a)):
                    search = search + '.+' + a[i]
            # обработка, когда не выбраны категории товаров
            if _id1 is None and _id2 is None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
                goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                    'cat3').filter(is_good=True,  name__iregex=search).order_by('name')

                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'page': page, 'goods': page.object_list}
                return render(request, "goods/categories4.html", context)
            # обработка, когда выбран раздел 1-ого уровня
            elif _id1 is not None and _id2 is None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                         cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
                        is_good=True, name__iregex=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, name__iregex=search).order_by('name')
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'page': page, 'goods': page.object_list}
                return render(request, "goods/categories4.html", context)
            # обработка, когда выбран раздел 2-ого уровня
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
                                    'cat3').filter(is_good=True, name__iregex=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, cat2=_id2, name__iregex=search).order_by('name')
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page, 'goods': page.object_list}
                return render(request, "goods/categories4.html", context)
            # обработка, когда выбран раздел 3-его уровня
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
                                is_good=True, name__iregex=search).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(
                        is_good=True, cat1=_id1, cat2=_id2, cat3=_id3, name__iregex=search).order_by('name')
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page, 'goods': page.object_list}

                return render(request, "goods/categories4.html", context)
    # начальный вывод поиска товаров
    else:
        form = GoodsForm()
    # начальный вывод
    if _id1 is None and _id2 is None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
            is_good=True).order_by('name')

        # постраничный вывод
        paginator = Paginator(goods, 100)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context = {'form': form, 'cat1': cat1, 'page': page, 'goods': page.object_list}
        return render(request, "goods/categories4.html", context)
    # вывод при выбранном разделе 1-ого уровня
    elif _id1 is not None and _id2 is None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(is_good=True,
                                                    cat1=_id1).order_by('name')
        # постраничный вывод
        paginator = Paginator(goods, 100)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)

        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'page': page, 'goods': page.object_list}
        return render(request, "goods/categories4.html", context)
    # вывод при выбранном разделе 2-ого уровня
    elif _id1 is not None and _id2 is not None and _id3 is None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by(
            'name')
        cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1, cat2=_id2,
                                                                                     cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
            is_good=True, cat1=_id1, cat2=_id2).order_by('name')

        # постраничный вывод
        paginator = Paginator(goods, 100)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)

        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page, 'goods': page.object_list}
        return render(request, "goods/categories4.html", context)
    # вывод при выбранном разделе 3-его уровня
    elif _id1 is not None and _id2 is not None and _id3 is not None and search is None:
        cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by('name')
        cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0, cat3=0).order_by(
            'name')
        cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1, cat2=_id2,
                                                                             cat3=0).order_by('name')
        goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2', 'cat3').filter(
            is_good=True, cat1=_id1, cat2=_id2, cat3=_id3).order_by('name')

        # постраничный вывод
        paginator = Paginator(goods, 100)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)

        context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page, 'goods': page.object_list}
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