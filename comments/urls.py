from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CommentsListView.as_view(), name="comments"),
    path('new_comment/', views.new_comment, name="new_comment")
    ]
