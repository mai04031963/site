from django.urls import path

from . import views

urlpatterns = [
    #path("", views.comments_, name="comments")
     path('', views.CommentsListView.as_view(), name="comments")
    ]