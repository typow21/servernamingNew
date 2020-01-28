from django.shortcuts import render
from django.db import models
from detailsapp.models import ServerDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import ServerModelForm
from django.db.models import F
from detailsapp import models

# from .forms import ServerNameForm
# from .models import Server

def results(request):
    return render(request, "detailsapp/template/results.html", {})

def home(request):
    return render(request, "detailsapp/template/home.html", {})
    
def serverDetails(request):
    if request.method == 'POST':
        form = ServerModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            currentInstance = ServerDetails.objects.last()
            # raise error if you submit a blank form
            print("\n")
            # print("\nCurrent Server: ", currentInstance)
            currentInstSequence = currentInstance.sequence
            # print("Set of servers: ", servers)
            # i feel like this should be done in the model
            while(models.checkDuplicates(currentInstance)):
                currentInstance.sequence = models.updateSequence(currentInstance)
            currentInstance.serverName = currentInstance.assignName()
            currentInstance.save()
            serverName = currentInstance.assignName()
            print("Current Server Name: " , serverName)
            models.classifyServer(currentInstance)
            servers = ServerDetails.objects.all()
            print(ServerDetails.objects.last().serverName)
            # serverTypes --> have a function return a dictionary of all types of servers
            return render(request, 'detailsapp/template/display.html', {'servers':servers, 'currentServer':currentInstance})
    else:
        form_class = ServerModelForm
        return render(request, 'detailsapp/template/serverDetails.html' , {'form':form_class,} )
