from django.contrib import admin

# Register your models here.
from hodaapp.models import Book
from hodaapp.models import Users
admin.site.register(Book)
admin.site.register(Users)
