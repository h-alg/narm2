from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext , loader
from django.shortcuts import render_to_response 
from django.http import HttpResponse
from django.core.context_processors import csrf 
from django.http import HttpResponse 
import datetime
#from __future__ import unicode_literals
import codecs

###DPI
from mydatabase.models import Users
from mydatabase.models import Book
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
    #return render_to_response('test.html' )
    return render_to_response('base.html' )






def sabtenam(request):


    if 'username' in request.GET and request.GET['username']:
        #f = request.GET['firstname']
        #p = request.GET['password']
        #e = request.GET['email']


        username = request.GET['username']
        name = request.GET['name']
        family = request.GET['family']
        password = request.GET['password']
        email = request.GET['email']
        #birthday = request.GET['birthday']
        address = request.GET['address']




        sub = True
        if not (username or name or family or password or email or address):
        #if (not f) and (not p)  and (not e):
            vorood = False

        else :
            eusername = False
            ename= False
            efamily= False
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
                elif len (str(name)) > 10 or len(str(name)) < 3 :
                    ename = True
                elif len (str(family)) > 30 or len(str(family)) < 3 :
                    efamily = True
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
                    new_user=Users(name=name,password= password , email = email , username= username , adress = address , family = family , hesab = 0)
                    new_user.save()
            else :
                tekrari = True
                #ezafe kardan be db

        return render_to_response('sabtenam.html', {'efamily': efamily ,'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername , 'ename' : ename , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})

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
    a=(int(page)-1) * 2
    b = a+2
    newpage = str(int(page)+1)
    oldpage = str(int(page)-1)
    error = False
    empty = False
    user = username
    endlist = []
    
    if int(oldpage) == 0:
        error = True
    #book_list = Books.objects.all()[a:b]
    book_list=Book.objects.filter(context__icontains=group )[a:b]
    if str(book_list)== "[]":
        empty = True
    else:
        endlist = []
        for i in book_list:
            mylist =[]
            mylist.append(i.name)
            mylist.append(i.publication)
            mylist.append(i.price)
            #mylist.append(i.school)
            endlist.append(mylist)
           
    #gozar=s.sharh
    return render_to_response('book_list.html', {'endlist' : endlist , 'empty': empty ,'error': error , 'book_list' : book_list, 'newpage' : newpage , 'oldpage': oldpage , 'group' : group , 'username' : username })

