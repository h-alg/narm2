from django.shortcuts import render
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


# Create your views here.
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

def login (request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})