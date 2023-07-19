from django.urls import path
from . views import good_search, good_seek, GoodsListView

urlpatterns = [
    #path("", goods_list, name="index"),
    path("", good_search, name='catalogs'),
    path("<int:_id1>/", good_search, name='catalogs1'),
    path("<int:_id1>/<int:_id2>/", good_search, name='catalogs2'),
    path("<int:_id1>/<int:_id2>/<int:_id3>/", good_search, name='catalogs3'),
    #path("seek", good_seek, name='seek')
    #path("seek/<slug:filter>/", GoodsListView.as_view(filter=filter), name='search_result')
    # ex: /goods/5/
    #path("<int:_id>/", views.detail, name="detail"),

]