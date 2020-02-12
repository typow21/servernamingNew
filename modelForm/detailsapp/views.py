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

def home(request):
    return render(request, "detailsapp/template/index.html", {})

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


            # i feel like this should be done in the model!!!!
            # potential feature
            # nameChecks()
            currentInstance = ServerDetails.objects.last()
            models.classifyServer(currentInstance)

            # raise error if you submit a blank form
            if(currentInstance.OS == "--" or currentInstance.purpose == "--" or currentInstance.role == "--"):
                print("\nBlank form submitted.\n\nForm Reset.\n")
                form_class = ServerModelForm
                error = "Please fill out all required fields"
                return render(request, 'detailsapp/template/form.html' , {'form':form_class, 'error':error} )

            
            servers = ServerDetails.objects.all()
            columnSets = models.createArrayOfSets(servers) 
            currentColumIndex = models.classifMap()
            print("Views: current ident: ",currentInstance.ident)
            print("Views: current server column index: ",currentColumIndex.get(currentInstance.ident))
            currServSet = columnSets[currentColumIndex.get(currentInstance.ident)]

            # checks for duplicates and updates sequence if one is found
            for server in currServSet:
                if(server.sequence == currentInstance.sequence):
                    models.updateSequence(currentInstance)
                print("Views: currentInstance in currServSet test: ")
            
            #assigns the name to the server
            currentInstance.serverName = currentInstance.assignName()
            # serverName = currentInstance.assignName()

            # print("Current Server Name: " , serverName)
            models.classifyServer(currentInstance)
            servers = ServerDetails.objects.all()
            currentInstance.save()

            print("Current server name 2:",ServerDetails.objects.last().serverName)
            
            #returns an array of server sets -- each index is a set of servers with same ident
            #ident is the naming key for groups of servers
            #ident is used to classify servers into their columns
            # columnSets = models.createArrayOfSets(servers) 
            # currentColumIndex = models.classifMap()
            # print(currentInstance.ident)
            # print(currentColumIndex.get(currentInstance.ident))
            # print("column sets", columnSets[currentColumIndex.get(currentInstance.ident)])

            #if the ident starts with w it is windows so it redirects to the windows db
            if (currentInstance.ident[0] == "w"):
                print("windows\n")
                return HttpResponseRedirect('/displaywindows/')

            #if the ident starts with l it is linux so it redirects to the linux db
            else:
                print("linux\n")
                return HttpResponseRedirect('/displaylinux/')   

            # if you want it to just direct to the current server name comment out logic
            # and uncomment next line
            # return HttpResponseRedirect('/displayserver/')
    else:
        form_class = ServerModelForm
        error = ""
        return render(request, 'detailsapp/template/form.html' , {'form':form_class} )
