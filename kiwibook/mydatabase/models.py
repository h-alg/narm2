from django.db import models
from django.forms import ModelForm


# Create your models here.
class Users(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    birthday_date = models.DateField(auto_now_add=True)
    # picture_user = models.ImageField(upload_to= None , height_field = None , width_field = None , max_length = 100)
    adress = models.CharField(max_length=500)
    hesab = models.IntegerField()
    favorite = ['-abc']

    def __unicode__(self):
        return self.username


class Book(models.Model):
    UNIVERSITY = 'UN'
    ART = 'AR'
    SCIENCE = 'SC'
    KIDS = 'KD'
    BOOK_FIELD_CHOICES = (
        (UNIVERSITY, 'University'),
        (ART, 'Art'),
        (SCIENCE, 'Science'),
        (KIDS, 'Kids'),
    )

    id_book = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    #image=models.ImageField()
    author = models.CharField(max_length=100)
    edition = models.IntegerField(default=1)
    field = models.CharField(max_length=100, choices=BOOK_FIELD_CHOICES, default=ART)
    price = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s' % self.id_book


from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['id_book','name', 'author', 'edition', 'field', 'price', 'rate']
