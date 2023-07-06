from django import forms
from .models import Good


class GoodsForm(forms.ModelForm):

    name = forms.CharField(max_length=50, widget=forms.widgets.ChoiceWidget())

    class Meta:
        model = Good
        fields = {'name', 'description', 'cat1', 'cat2', 'cat3', 'is_good', 'in_stock', 'price'}
