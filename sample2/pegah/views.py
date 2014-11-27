# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import *
#from django.template import *
import datetime
#from django import forms
from models import *

def search_book(request):
    return render_to_response("search_book.html")

def search(request,username):
    empty = False
    s_name= request.GET["selection"]
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
        phrase = message.encode('utf-8')
        if s_name=="author name": type_search="author"
        if s_name=="name of book":type_search="name"
        type_search = type_search.encode('utf-8')
        list_search = Book.objects.filter(type_search__icontains=phrase)
        if str(list_search)=="[]":
            return HttpResponse("Not Found!!!")
        else:
            return render_to_response('proffer.html', {'list_search' : list_search  , 'username' : username })
    else:
        return HttpResponse('you submitted empty form!!!.')


