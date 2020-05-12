from django.shortcuts import render
from bigcow.forms import AddTextInput
from bigcow.models import CowInput
import subprocess


def index(request):
    if request.method == "POST":
        form = AddTextInput(request.POST)
        if form.is_valid():
            cow_data = form.cleaned_data
            CowInput.objects.create(cow_input=cow_data['cow_input'])
            cowput = cow_words(cow_data['cow_input'])
            form = AddTextInput()
            return render(
                request, 'index.html',
                {"form": form,  'cowput': cowput}
                )
        form = AddTextInput()
    return render(request, 'index.html', {'form': AddTextInput()})


def cow_words(string):
    cow_output = subprocess.Popen(
        ['cowsay', string],
        stdout=subprocess.PIPE).communicate()[0]
    return cow_output.decode("utf8")


def history(request):
    cow_data = CowInput.objects.all()
    cow_history = []
    for cow in cow_data:
        cow_history.append(cow)
# Quackers - Matt helped with slicing
    cow_history = cow_history[-10:]
    cow_history.reverse()
    cow = cow_words('Our Last 10 Cows said:')
    return render(request, 'history.html', {
        "cow_history": cow_history, "cow": cow
        })
