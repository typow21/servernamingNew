from django.shortcuts import render
from .forms import ServerNameForm
from .models import Server

def results(request):
    return render(request, "detailsapp/template/results.html", {})

def home(request):
    return render(request, "detailsapp/template/home.html", {})
    
def form(request):
    if request.method == 'POST':
        form = ServerNameForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get("OS")
    else:
        form = ServerNameForm()
    Server()
    Server.OS = request.POST.get('OS')
    print(Server.OS)
    return render(request, "detailsapp/template/form.html", {'form': form})
        
