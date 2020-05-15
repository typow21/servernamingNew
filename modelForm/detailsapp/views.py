import csv
from datetime import date, datetime
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

# Rederns the html for the home page
def home(request):
    return render(request, "detailsapp/template/index.html", {})

# Renders HTML page that displays the last made server
def displayserver(request):
    currentInstance = ServerDetails.objects.last()
    # Is this/does this need to be a relative path?
    # print(currentInstance.time)
    return render(request, "detailsapp/template/displayserver.html", {'currentServer':currentInstance})

# Renders HTML page that displays windows servers table
def displaylinux(request):
    servers = ServerDetails.objects.all()
    linServers = []
    for server in servers:
        if(server.OS == '35'): #35 is the code for linux
            linServers.append(server)
    currLinServer = linServers[-1]
    columnSets = models.createArrayOfSets(servers)
    currentInstance = ServerDetails.objects.last()
    # for server in linServers:

    # Is this/does this need to be a relative path?
    return render(request, "detailsapp/template/displayLinux.html", {'columnSets':columnSets, 'currentServer':currentInstance, 'currLinServer': currLinServer})

# Renders HTML page that displays windows servers table
# Sends necessary data to the html page
def displaywindows(request):
    servers = ServerDetails.objects.all()
    winServers = []
    for server in servers:
        if(server.OS == '30'): # 30 is the code for windows
            winServers.append(server)
    currWinServer = winServers[-1]
    columnSets = models.createArrayOfSets(servers) 
    currentInstance = ServerDetails.objects.last()
    # Does the link need to be a relative path?
    return render(request, "detailsapp/template/displaywindows.html", {'columnSets':columnSets, 'currentServer':currentInstance, 'currWinServer': currWinServer})

# Exports windows table
def windowsTableDownload(request):
    response = HttpResponse(content_type = 'text/csv')
    today = date.today()
    today = str(today)
    filename = "windows"+today+".csv"
    response['Content-Disposition'] = 'attachment; filename = ' + filename  # This is the name of the attachment

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['OS', 'Role', 'Purpose', 'Server name'])
    # Windows servers
    # Production web
    pw_servers = ServerDetails.objects.filter(ident = 'wpw')
    for server in pw_servers:
        writer.writerow(['Windows', 'Production', 'Web', server.serverName])

    # Production app
    pa_servers = ServerDetails.objects.filter(ident = 'wpa')
    for server in pa_servers:
        writer.writerow(['Windows', 'Production', 'app',server.serverName])

    # Production database
    pd_servers = ServerDetails.objects.filter(ident = 'wpd')
    for server in pd_servers:
       writer.writerow(['Windows', 'Production', 'Database',server.serverName])

    # Production storage
    ps_servers = ServerDetails.objects.filter(ident = 'wps')
    for server in ps_servers:
        writer.writerow(['Windows', 'Production', 'Storage',server.serverName])

    # NP web
    npw_servers = ServerDetails.objects.filter(ident = 'wnw')
    for server in npw_servers:
        writer.writerow(['Windows', 'Non-production', 'Web',server.serverName])

    # NP app
    npa_servers = ServerDetails.objects.filter(ident = 'wna')
    for server in npa_servers:
        writer.writerow(['Windows', 'Non-production', 'App',server.serverName])

    # NP database
    npd_servers = ServerDetails.objects.filter(ident = 'wnd')
    for server in npd_servers:
        writer.writerow(['Windows', 'Non-production', 'Database',server.serverName])

    # NP storage
    nps_servers = ServerDetails.objects.filter(ident = 'wns')
    for server in nps_servers:
        writer.writerow(['Windows', 'Non-production', 'Storage',server.serverName])

    # Test web
    tw_servers = ServerDetails.objects.filter(ident = 'wtw')
    for server in tw_servers:
        writer.writerow(['Windows', 'Test', 'Web',server.serverName])

    # Test app
    ta_servers = ServerDetails.objects.filter(ident = 'wta')
    for server in ta_servers:
        writer.writerow(['Windows', 'Test', 'App',server.serverName])

    # Test database
    td_servers = ServerDetails.objects.filter(ident = 'wtd')
    for server in td_servers:
        writer.writerow(['Windows', 'Test', 'Database',server.serverName])

    # Test storage      
    ts_servers = ServerDetails.objects.filter(ident = 'wts')
    for server in ts_servers:
        writer.writerow(['Windows', 'Test', 'Storage',server.serverName])

    return response

# Exports linux table
def linuxTableDownload(request):
    # TO-DO
    response = HttpResponse(content_type = 'text/csv')
    today = date.today()
    today = str(today)
    filename = "linux"+today+".csv"
    response['Content-Disposition'] = 'attachment; filename = ' + filename  # This is the name of the attachment

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['Date', today,'Time Stamp:', datetime.now().time()])
    writer.writerow(['Linux Servers'])
    writer.writerow(['Production Web'])
    pw_servers = ServerDetails.objects.filter(ident = 'lpw')
    for server in pw_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Production App'])
    pa_servers = ServerDetails.objects.filter(ident = 'lpa')
    for server in pa_servers:
       writer.writerow([server.serverName])

    writer.writerow(['Production Database'])
    pd_servers = ServerDetails.objects.filter(ident = 'lpd')
    for server in pd_servers:
       writer.writerow([server.serverName])

    writer.writerow(['Production Stroage'])  
    ps_servers = ServerDetails.objects.filter(ident = 'lps')
    for server in ps_servers:
       writer.writerow([server.serverName])

    writer.writerow(['Non-production Web'])
    npw_servers = ServerDetails.objects.filter(ident = 'lnw')
    for server in npw_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Non-production App'])
    npa_servers = ServerDetails.objects.filter(ident = 'lna')
    for server in npa_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Non-production Database'])
    npd_servers = ServerDetails.objects.filter(ident = 'lnd')
    for server in npd_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Non-production Stroage']) 
    nps_servers = ServerDetails.objects.filter(ident = 'lns')
    for server in nps_servers:
       writer.writerow([server.serverName])

    writer.writerow(['Test Web'])
    tw_servers = ServerDetails.objects.filter(ident = 'ltw')
    for server in tw_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Test App'])
    ta_servers = ServerDetails.objects.filter(ident = 'lta')
    for server in ta_servers:
        writer.writerow([server.serverName])

    writer.writerow(['Test Database'])
    td_servers = ServerDetails.objects.filter(ident = 'ltd')
    for server in td_servers:
        writer.writerow([server.serverName])
        
    writer.writerow(['Test Stroage'])       
    ts_servers = ServerDetails.objects.filter(ident = 'lts')
    for server in ts_servers:
        writer.writerow([server.serverName])

    
    return response

# This function deals with the form submission
# NEED to add some more info
def form(request):
    if request.method == 'POST':
        form = ServerModelForm(request.POST)
        if form.is_valid():
            u = form.save()

            currentInstance = ServerDetails.objects.last()
            models.classifyServer(currentInstance)

            # raise error if you submit a blank form
            if(currentInstance.OS == "--" or currentInstance.purpose == "--" or currentInstance.role == "--"):
                print("\nBlank form submitted.\n\nForm Reset.\n")
                form_class = ServerModelForm
                error = "Please fill out all required fields"
                print(currentInstance)
                currentInstance.delete()
                print(currentInstance)
                return render(request, 'detailsapp/template/form.html' , {'form':form_class, 'error':error} ) # sends the error message to the html page and reloads page

            
            servers = ServerDetails.objects.all() # loads set of all server names into the servers variable
            columnSets = models.createArrayOfSets(servers) # creates an array of server sets categorized by column
            currentColumIndex = models.classifMap() # maps each server category to an index
            print("Views: current ident: ",currentInstance.ident) 
            print("Views: current server column index: ",currentColumIndex.get(currentInstance.ident))

            # Uses the current server's ident to return all servers in the set of current server category
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

            # print("Current server name 2:",ServerDetails.objects.last().serverName)
            
            #returns an array of server sets -- each index is a set of servers with same ident
            #ident is the naming key for groups of servers
            #ident is used to classify servers into their columns
            # columnSets = models.createArrayOfSets(servers) 
            # currentColumIndex = models.classifMap()
            # print(currentInstance.ident)
            # print(currentColumIndex.get(currentInstance.ident))
            # print("column sets", columnSets[currentColumIndex.get(currentInstance.ident)])

            #if the ident starts with w it is windows so it redirects to the windows db
            # if (currentInstance.ident[0] == "w"):
            #     print("windows\n")
            #     return HttpResponseRedirect('/displaywindows/')

            # #if the ident starts with l it is linux so it redirects to the linux db
            # else:
            #     print("linux\n")
            #     return HttpResponseRedirect('/displaylinux/')   

            # if you want it to just direct to the current server name comment out logic
            # and uncomment next line
            return HttpResponseRedirect('/displayserver/')
    else:
        form_class = ServerModelForm
        return render(request, 'detailsapp/template/form.html' , {'form':form_class} )

