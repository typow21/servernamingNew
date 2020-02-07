from django.shortcuts import render
from django.db import models
from detailsapp.models import ServerDetails
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from .forms import ServerModelForm
from django.db.models import F
from detailsapp import models

# from .forms import ServerNameForm
# from .models import Server

def displayserver(request):
    currentInstance = ServerDetails.objects.last()
    return render(request, "detailsapp/template/displayserver.html", {'currentServer':currentInstance})

def displaylinux(request):
    servers = ServerDetails.objects.all()
    columnSets = models.createArrayOfSets(servers) 
    currentInstance = ServerDetails.objects.last()
    return render(request, "detailsapp/template/displayLinux.html", {'columnSets':columnSets, 'currentServer':currentInstance})
    
def displaywindows(request):
    servers = ServerDetails.objects.all()
    columnSets = models.createArrayOfSets(servers) 
    currentInstance = ServerDetails.objects.last()
    return render(request, "detailsapp/template/displaywindows.html", {'columnSets':columnSets, 'currentServer':currentInstance})

# add a delete button
# add an export option

def form(request):
    if request.method == 'POST':
        form = ServerModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            currentInstance = ServerDetails.objects.last()
            # raise error if you submit a blank form
            currentInstSequence = currentInstance.sequence
            # i feel like this should be done in the model
            # this makes the first server name end in a 1 when it should end in a zero.
            while(models.checkDuplicates(currentInstance)):
                currentInstance.sequence = models.updateSequence(currentInstance)
                print("updating sequence")

            currentInstance.serverName = currentInstance.assignName()
            serverName = currentInstance.assignName()

            # print("Current Server Name: " , serverName)
            models.classifyServer(currentInstance)
            servers = ServerDetails.objects.all()
            currentInstance.save()

            print("Current server name 2:",ServerDetails.objects.last().serverName)
            #returns an array of server sets -- each index is a set of servers with same ident
            #ident is the naming key for groups of servers
            columnSets = models.createArrayOfSets(servers) 
            print("column sets", columnSets[0])
            if (currentInstance.ident[0] == "w"):
                print("windows\n")
                return HttpResponseRedirect('/displaywindows/')
            else:
                print("linux\n")
                return HttpResponseRedirect('/displaylinux/')    
            # return HttpResponseRedirect('/displayserver/')
    else:
        form_class = ServerModelForm
        return render(request, 'detailsapp/template/serverDetails.html' , {'form':form_class,} )
