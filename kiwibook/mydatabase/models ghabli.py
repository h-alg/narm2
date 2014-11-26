from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
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
    id_book = models.IntegerField()
    name = models.CharField(max_length=100)
    # picture_book = models.ImageField(upload_to= None , height_field = None , width_field = None , max_length = 100)
    authors = ['-fdw']
    publish_date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    publication = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    sell_public = models.IntegerField()
    sell_users = models.IntegerField()
    count = models.IntegerField()

    def __unicode__(self):
        return u"%s" % self.id_book
