from django.shortcuts import render, reverse, HttpResponseRedirect
from bigcow.models import CowInput
from bigcow.forms import AddTextInput
import subprocess
# Create your views here.

# def index(request):
#     data = CowInput.objects.all()
#     return render(request, 'index.html', {'data': data})


def index(request):
    cow_data = CowInput.objects.all()
    form = AddTextInput()
    if request.method == "POST":
        form = AddTextInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowInput.objects.create(
                cow_input=data['cow_input']
            )            
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'index.html', {'cow_data': cow_data, 'form': form})
