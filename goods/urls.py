from django.urls import path
from . views import good_search2

urlpatterns = [
    path("", good_search2, name='catalogs'),
    path("<int:_id1>/", good_search2, name='catalogs1'),
    path("<int:_id1>/<int:_id2>/", good_search2, name='catalogs2'),
    path("<int:_id1>/<int:_id2>/<int:_id3>/", good_search2, name='catalogs3')
]


