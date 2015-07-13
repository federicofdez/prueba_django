from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's a valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/result')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'simple_form/name.html', {'form': form})

def result(request):
    render(request, 'simple_form/result.html', {'result': result})