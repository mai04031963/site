from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
from . models import Comments
from django.http import Http404
from django.views.generic import ListView
from datetime import date


# Create your views here.
#def comments_(request):
#    comments_list = Comments.objects.get(pk=2)
#    context = {"id": comments_list.id,
#               "comment_date": comments_list.comment_date,
#               "comment_text": comments_list.comment_date,
#               "comment_sign": comments_list.comment_sign,
#               "answer_for_comment": comments_list.answer_for_comment
#               }
#    print(context)
#    print(comments_list.id, comments_list.comment_date, comments_list.comment_text,
#          comments_list.comment_sign, comments_list.answer_for_comment)
#    return render(request, "comments/comments.html", context)


class CommentsListView(ListView):
    model = Comments
    template_name = "comments/comments.html"
    #queryset = Comments.objects.all().order_by("-comment_date")
    paginate_by = 5
    allow_empty = True

    def get(self, request, *args, **kwargs):
        return super(CommentsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CommentsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Comments.objects.all().order_by("-comment_date")
