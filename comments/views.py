from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from django.template import loader
from . models import Comments
from django.http import Http404
from django.views.generic import ListView, CreateView
from datetime import date
from django import forms
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . forms import CommentForm, example
from random import random, choice

class CommentsListView(ListView):
    model = Comments
    template_name = "comments/comments.html"
    paginate_by = 5
    allow_empty = True

    def get(self, request, *args, **kwargs):
        return super(CommentsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Comments.objects.all().order_by("-comment_date")


def new_comment(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            return redirect('../')
        else:
            context = {'form': form}
            return render(request, 'comments/new_comment.html', context)
    else:
        form = CommentForm()
        context = {'form': form}
        return render(request, 'comments/new_comment.html', context)


