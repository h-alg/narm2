from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
import mydatabase.models

class BookForm(ModelForm):
    class Meta:
        model=mydatabase.models.Book
        fields=['id_book' ,'name','author','edition','field','price','rate']
