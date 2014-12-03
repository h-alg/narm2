from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext , loader
from django.shortcuts import render_to_response 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf 
from django.http import HttpResponse 
import datetime
#from __future__ import unicode_literals
import codecs

###DPI
from mydatabase.models import Users
from mydatabase.models import Book
from kiwibook.forms import BookForm
import kiwibook.forms
from django import forms


#from db.models import person
#from db.models import case
#from db.models import laptop
#from db.models import external_tools
#from db.models import log
#import codecs




from django.http import HttpResponse 




##############DPI



############

def kerase(request):
    mm=[["a","b","c"],["d" , "e" , "f"],["h" , "i" , "k"]]
    #return render_to_response('main.html' )
    #return render_to_response('kerase.html' )
    return render_to_response('base.html' )






def sabtenam(request):


    if 'username' in request.GET and request.GET['username']:
        #f = request.GET['firstname']
        #p = request.GET['password']
        #e = request.GET['email']


        username = request.GET['username']
        #name = request.GET['name']
        #family = request.GET['family']
        password = request.GET['password']
        email = request.GET['email']
        #birthday = request.GET['birthday']
        address = request.GET['address']




        sub = True
        #if not (username or name or family or password or email or address):
        if not (username or password or email or address):

        #if (not f) and (not p)  and (not e):
            vorood = False

        else :
            eusername = False
            #ename= False
            #efamily= False
            epassword= False
            eemail= False
            eaddress = False
            #ebirthday=False
            vorood = True
            #mina = Users.objects.filter(name__icontains=f)
            check_user = Users.objects.filter(username__icontains=username)

            str_check = str (check_user)
            if str_check == "[]" :
                tekrari = False
                if len(str(username)) > 15 or len(str(username)) < 4:
                    eusername = True
                #elif len (str(name)) > 10 or len(str(name)) < 3 :
                    #ename = True
                #elif len (str(family)) > 30 or len(str(family)) < 3 :
                    #efamily = True
                elif len (str(password)) > 15 or len(str(password)) < 4 :
                    epassword = True
                #elif len (str(address)) > 15 or len(str(name)) < 3 :
                    #ename = True
                elif len(str(address)) == 0 :
                    eaddress = True
                #elif len(str(email)) == 0 :
                elif not(((str(email).find("@") < str(email).find(".") ) and (str(email).find("@")!= -1 ))):
                    eemail = True
                else:
                    #new_user=Users(name=name,password= password , email = email , username= username , adress = address , family = family , hesab = 0)
                    new_user=Users(password= password , email = email , username= username , adress = address , hesab = 0)

                    new_user.save()
            else :
                tekrari = True
                #ezafe kardan be db

#        return render_to_response('sabtenam.html', {'efamily': efamily ,'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername , 'ename' : ename , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})
        return render_to_response('sabtenam.html', {'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername  , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})
    

    else :
        sub = False
        return render_to_response('sabtenam.html', {'error': False , "sub" : sub})



####login
def login(request):
    #if 'username' in request.GET and request.GET['username']:
       # username = request.GET['username']
        #password = request.GET['password']
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        password = request.POST['password']
        
        
        

        sub = True

        if (not username) and (not password)  :
            vorood = False

        else :
            epassword= False
            vorood = True
            list_user = Users.objects.filter(username__icontains=username)
            str_user = str (list_user)
            #mona = sazman.objects.filter(name__icontains=f)
            #nn = str(mona)
            if str_user == "[]"  :
                epassword = True
                
               
            else :
                new_user = Users.objects.get(username__icontains=username)
                if new_user.password != password:
                    epassword = True
                else :
                    template=loader.get_template('base2.html' )
                    #template=loader.get_template('aa.html')
                    context=RequestContext(request,{'epassword': epassword , 'username':username ,'username': username})
                    return HttpResponse(template.render(context))
                    #return render_to_response('base2.html' , {"username" : username})
                               
                
        template=loader.get_template('login.html')
        #template=loader.get_template('aa.html')
        context=RequestContext(request,{'epassword': epassword ,   'username' :username, 'password' : password , 'error': vorood ,  "sub" : sub , "list_user" : list_user})
        return HttpResponse(template.render(context))
        #return render_to_response('login.html', {'epassword': epassword ,   'username' :username, 'oassword' : password , 'error': vorood ,  "sub" : sub , "list_user" : list_user})

    else :
        sub = False
        template=loader.get_template('login.html')
        #template=loader.get_template('aa.html')
        context=RequestContext(request,{'error': False , "sub" : sub  })
        return HttpResponse(template.render(context))
        #return render_to_response('login.html', {'error': False , "sub" : sub})


def aa(request,username):
    mm=[["a","b","c"],["d" , "e" , "f"],["h" , "i" , "k"]]
    return render_to_response('aa.html', {'username': username})




def book(request , username , group , page):
    a=(int(page)-1) * 3
    b = a+3
    newpage = str(int(page)+1)
    oldpage = str(int(page)-1)
    error = False
    empty = False
    user = username
    endlist = []
    
    if int(oldpage) == 0:
        error = True
    #book_list = Books.objects.all()[a:b]
    book_list=Book.objects.filter(field__icontains=group )[a:b]
    #book_list=Book.objects.filter(context__icontains=group )[a:b]

    if str(book_list)== "[]":
        empty = True
    else:
        endlist = []
        for i in book_list:
            mylist =[]
            mylist.append(i.id_book)
            mylist.append(i.name)
            mylist.append(i.author)
            mylist.append(i.price)
            
            endlist.append(mylist)
           
    #gozar=s.sharh
    return render_to_response('book_list.html', {'endlist' : endlist , 'empty': empty ,'error': error , 'book_list' : book_list, 'newpage' : newpage , 'oldpage': oldpage , 'group' : group , 'username' : username })

def proffer(request , username):
    new_user = Users.objects.get(username__icontains=username)
   # flist = new_user.favorite
    flist = ["UN" , "KD"]
    #too alaghe manD hash daste haye ketaba hast
    #begam az ketabaye oon daste do taye bartar ro BRe
    proffer_list=[]
    for f in flist :
        newlist = Book.objects.filter(field__icontains= f)
        ratelist=[]
        for onsor in newlist:
            ratelist.append( onsor.rate)
        max_rate = max (ratelist)
        for i in range(len(ratelist )):
            if ratelist[i] == max(ratelist):
                proffer_list.append(newlist[i])

        endlist = []
        for i in proffer_list:
            mylist =[]
            mylist.append(i.id_book)
            mylist.append(i.name)
            mylist.append(i.author)
            mylist.append(i.price)
            
            endlist.append(mylist)

    #profferlist shamele behtarin ketab az har daste E ke karbar e mazkoor gozashte too alaghe hash
    


    #return render_to_response('proffer.html', {'flist' : flist  , 'username' : username })
    return render_to_response('proffer.html', {'endlist':endlist , 'proffer_list' : proffer_list  , 'username' : username })    

    
def inf_book(request , id_book):
    new_book = Book.objects.get(id_book=id_book)
    #new_book = Book.objects.get(id_book__icontains=id_book)

    book_name = new_book.name
    book_price = new_book.price
    book_author = new_book.author


    return render_to_response('infbook.html', {'book_name' : book_name  , 'book_price' : book_price , 'book_author' : book_author})    
    


    #####pegah

def search(request):
    empty = False
    list_search =[]
    errors=[]
    s_name= request.GET["selection"]
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
        #phrase = message.encode('utf-8')
        if s_name=="author name":
            list_search = Book.objects.filter(author__icontains=message)
        if s_name=="name of book":
            list_search = Book.objects.filter(name__icontains=message)

        if str(list_search)=="[]":
            errors.append("not found")
            return render_to_response('base2.html',{'errors':errors})
        else:
            #endlist = list_search
            return render_to_response('proffer.html',{'list_search':list_search })
    else:
        errors.append("empty field")
        return render_to_response('base2.html',{'errors':errors})
#hodaaaaaaaaaaaaaaaa
def sefaresh(request):
    # A HTTP POST?
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponseRedirect('/thanks.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BookForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request,'sefaresh.html',{'form':form})