from django import forms
from .models import Comments

example = ''

class CommentForm(forms.ModelForm):

    comment_text = forms.CharField(label="Ваш отзыв", max_length=1000, help_text="(максисмум 1000 знаков)",
                                   strip=True,
                                   widget=forms.widgets.Textarea(attrs={'cols': 100, 'rows': 10}))

    comment_sign = forms.CharField(label='Представьтесь, пожалуйста', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}))

    comment_contact = forms.CharField(label='Ваш телефон или e-mail', max_length=100,
                                   help_text="",
                                   strip=True, widget=forms.widgets.TextInput(attrs={'size':100}))

    not_robot = forms.BooleanField(label="Подтвердите, что вы не робот", help_text="",
                                   widget=forms.widgets.CheckboxInput())

    captcha = forms.IntegerField(label=example, label_suffix='=', widget=forms.widgets.TextInput(attrs={'size': 3}))

    class Meta:
        model = Comments
        fields = ('comment_text', 'comment_sign', 'comment_contact', 'not_robot', 'captcha')
