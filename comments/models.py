from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.


class Comments(models.Model):
    comment_date = models.DateField(auto_now_add=True)
    comment_text = models.TextField(blank=True)
    comment_sign = models.CharField(max_length=100, blank=True)
    comment_contact = models.CharField(max_length=100, blank=True)
    answer_for_comment = models.TextField(blank=True)
    answer_sign = models.CharField(max_length=100, blank=True)

    #def __str__(self):
    #    return str(self.comment_date)