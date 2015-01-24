from django.shortcuts import render
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
from hodaapp.models import Users
from hodaapp.models import Book

from django import forms
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext , loader
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from hodaapp.models import BookForm
from hodaapp.models import UserForm

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
    flist = new_user.favorite
    
    #flist = ["UN" , "KD"]
    #too alaghe manD hash daste haye ketaba hast
    #begam az ketabaye oon daste do taye bartar ro BRe
    proffer_list=[]
    #####
    endlist=[]
    ####
    for f in flist :
        newlist = Book.objects.filter(field= f)
        #newlist = Book.objects.filter(field__icontains= f)

        
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
    return render_to_response('proffer.html', {'flist' : flist , 'endlist':endlist , 'proffer_list' : proffer_list  , 'username' : username })


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
            ##########
            final_list = []
            for i in list_search:
                mylist =[]
                mylist.append(i.id_book)
                mylist.append(i.name)
                mylist.append(i.author)
                mylist.append(i.price)

                final_list.append(mylist)
            #########
            #endlist = list_search
            return render_to_response('proffer.html',{'endlist':final_list })
    else:
        errors.append("empty field")
        return render_to_response('base2.html',{'errors':errors})


def search1(request):
    empty = False
    list_search =[]
    errors=[]
    s_name= request.GET["selection"]
    if 'q' in request.GET and request.GET['q']:
        message = request.GET['q']
        if s_name=="author_name":
            list_search = Book.objects.filter(author__icontains=message)
        if s_name=="book_name":
            list_search = Book.objects.filter(name__icontains=message)
        final_list=[]
        if str(list_search) == "[]":
            empty = True
            errors.append("not found")
            return render_to_response('base2.html',{'errors':errors})
        else:
            final_list = []
            for i in list_search:
                mylist =[]
                mylist.append(i.id_book)
                mylist.append(i.name)
                mylist.append(i.author)
                mylist.append(i.price)

                final_list.append(mylist)

        return render_to_response('proffer.html', {'endlist':final_list})





# Create your views here.
def sefaresh(request):
    sabt = False
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
            #return HttpResponseRedirect('/thanks.html')
            sabt = True
            return render(request, 'sefaresh.html' , {'sabt' :sabt})


        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = BookForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request,'sefaresh.html',{'form':form})

def log (request):
    sabt = False
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save(commit=True)
            sabt = True

            #return HttpResponseRedirect('/thanks/')
            #return render(request, 'thanks.html')
            #return render(request, 'thanks.html')
            return render(request, 'sabtenam.html' , {'sabt' :sabt})



    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    #return render(request, 'log.html', {'form': form})
    return render(request, 'sabtenam.html', {'form': form})




def buy(request , username , id_book):
    new_book = Book.objects.get(id_book=id_book)
    #new_book = Book.objects.get(id_book__icontains=id_book)

    book_name = new_book.name
    book_price = new_book.price
    book_author = new_book.author
    book_id = str(new_book.id_book)


    
        

    return render_to_response('infbook.html', {'username' : username , 'book_id' : book_id ,'book_name' : book_name   , 'book_price' : book_price , 'book_author' : book_author})



#######################
def endbuy(request , username , id_book):
    new_book = Book.objects.get(id_book=id_book)
    #new_book = Book.objects.get(id_book__icontains=id_book)

    book_name = new_book.name
    book_price = new_book.price
    book_author = new_book.author
    book_id = str(new_book.id_book)
    #book_str=""
    #book_str=book_str+book_id+','
    new_user= Users.objects.get(username = username)    #new_user= ye usere kufti
    new_str = new_user.books                            #new_str = ketabaye usere kufti be surate string
    end_str= new_str +"," + str(id_book)                #end_str = stringe ketabaye kufti +
    new_user.books = end_str
    new_user.save()
    book_list=end_str.split(',')
    list_of_book =[]

    #booklist : id haye ketabaye too sabad
    for id in book_list:
        newbook = []
        new_book = Book.objects.get(id_book=id)

        book_name = new_book.name
        book_price = new_book.price
        newbook.append(book_name)
        newbook.append(book_price)


        list_of_book.append(newbook)
    sum = 0
    for i in range( len(list_of_book)):
        sum = sum + int(list_of_book[i][1])

    l=["jame kol" , sum]
    list_of_book.append(l)


        

    return render_to_response('endbuy.html', {'list_of_book': list_of_book , 'sum': sum  , 'new_str':end_str})

#######################teste zaher

def zeinab(request):
   
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        password = request.POST['password']




        sub = True

        if (not username) and (not password)  :
            vorood = False

        else :
            epassword= False
            vorood = True
            new_user = Users.objects.get(username = username)
            if new_user.password != password :
                epassword = True
            else:
                template=loader.get_template('zeinab.html' )
                context=RequestContext(request,{'epassword': epassword , 'username':username ,'username': username})
                    
                return HttpResponse(template.render(context))
                
            


            


        template=loader.get_template('base.html')
        context=RequestContext(request,{'epassword': epassword ,  "sub" : sub })
        return HttpResponse(template.render(context))

    #else :
       # sub = False
       # template=loader.get_template('base.html')
      #  context=RequestContext(request,{'error': False , "sub" : sub  })
        #return HttpResponse(template.render(context))
    ######sabte nam
    #elif 'uname' in request.GET and request.GET['uname']:
    elif 'usernamesignup' in request.POST and request.POST['usernamesignup']:
        #f = request.GET['firstname']
        #p = request.GET['password']
        #e = request.GET['email']


       # username = request.GET['uname']
        
        #password = request.GET['youpasswd']
        #email = request.GET['youemail']
        #address = request.GET['youaddress']



        username = request.POST['usernamesignup']
        #name = request.GET['name']
        #family = request.GET['family']
        password = request.POST['passwordsignup']
        email = request.POST['emailsignup']
        #birthday = request.GET['birthday']
        address = request.POST['addresssignup']




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
        return render_to_response('zeinab.html', {'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername  , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})


    #else :
       # sub = False
       # return render_to_response('base.html', {'error': False , "sub" : sub})
    else :
        sub = False
        template=loader.get_template('base.html')
        context=RequestContext(request,{'error': False , "sub" : sub  })
        return HttpResponse(template.render(context))



#################################
def kerase(request):
   
    if 'username' in request.POST and request.POST['username']:
        username = request.POST['username']
        password = request.POST['password']




        sub = True

        if (not username) and (not password)  :
            vorood = False

        else :
            epassword= False
            vorood = True
            new_user = Users.objects.get(username = username)
            if new_user.password != password :
                epassword = True
            else:
                ########## *********** hamin ja Pshnehad e ma behesh bayad maloom she ke too safhe ash neshoon beDm : Pshnehad e kerase be shoma !!
                template=loader.get_template('afterlog.html' )
                context=RequestContext(request,{'epassword': epassword , 'username':username ,'username': username})
                    
                return HttpResponse(template.render(context))
                
            


            


        template=loader.get_template('base.html')
        context=RequestContext(request,{'epassword': epassword ,  "sub" : sub })
        return HttpResponse(template.render(context))

   
    elif 'usernamesignup' in request.POST and request.POST['usernamesignup']:
        



        username = request.POST['usernamesignup']
        password = request.POST['passwordsignup']
        email = request.POST['emailsignup']
        address = request.POST['addresssignup']



        sabtshod = False
        sub = True
        if not (username or password or email or address):

            vorood = False

        else :
            eusername = False
            epassword= False
            eemail= False
            eaddress = False
            vorood = True
            check_user = Users.objects.filter(username__icontains=username)

            str_check = str (check_user)
            if str_check == "[]" :
                tekrari = False
                if len(str(username)) > 15 or len(str(username)) < 4:
                    eusername = True
                elif len (str(password)) > 15 or len(str(password)) < 4 :
                    epassword = True
                elif len(str(address)) == 0 :
                    eaddress = True
                elif not(((str(email).find("@") < str(email).find(".") ) and (str(email).find("@")!= -1 ))):
                    eemail = True
                else:
                    new_user=Users(password= password , email = email , username= username , adress = address , hesab = 0)

                    new_user.save()
                    sabtshod = True
            else :
                tekrari = True

        return render_to_response('base.html', {'sabtshod' : sabtshod , 'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername  , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})


    
    else :
        sub = False
        template=loader.get_template('base.html')
        context=RequestContext(request,{'error': False , "sub" : sub  })
        return HttpResponse(template.render(context))



#################################



