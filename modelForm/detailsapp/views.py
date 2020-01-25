from django.shortcuts import render
from django.db import models
from detailsapp.models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import UserModelForm
from django.db.models import F
# from .forms import ServerNameForm
# from .models import Server

def results(request):
    return render(request, "detailsapp/template/results.html", {})

def home(request):
    return render(request, "detailsapp/template/home.html", {})
    
def userDetails(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            u = form.save()
            currentInstance = UserDetails.objects.last()
            # raise error if you submit a blank form
            print("\n")
            print("\nCurrent Server: ", currentInstance)
            currentInstSequence = currentInstance.sequence
            servers = UserDetails.objects.all()
            # print("Set of servers: ", servers)
            # i feel like this should be done in the model
            while(checkDuplicates(currentInstance)):
                currentInstance.sequence = updateSequence(currentInstance)
            currentInstance.save()
            return render(request, 'detailsapp/template/display.html', {'servers':servers})
    else:
        form_class = UserModelForm
        return render(request, 'detailsapp/template/userdetails.html' , {'form':form_class,} )

def checkDuplicates(currentInstance):
    duplicate = False
    newSequence = currentInstance.sequence
    numOfMatches = UserDetails.objects.filter(
                            OS = currentInstance.OS, 
                                purpose = currentInstance.purpose,
                                    role = currentInstance.role,
                                        sequence = currentInstance.sequence).count()
    if numOfMatches >= 1:
        if numOfMatches >= 2:
            print("Error: Duplicate server name.")
            # add a js alert here as a notice
        # newSequence = updateSequence(currentInstance)
        duplicate = True
        print("Current Inst Seq: ", newSequence)
        
    return duplicate

def updateSequence(currentInstance):
    print("reached 1")
    currentInstSequence = currentInstance.sequence
    firstDig = int(currentInstSequence[0])
    secondDig = int(currentInstSequence[1])
    thirdDig = int(currentInstSequence[2])
    if thirdDig < 9: #if less than 9
        thirdDig += 1 # increment by one
        # print("\treached 2")
        # print("\t", thirdDig)
    else: #if number is 9
        # print("reached 3")
        thirdDig = 0 #make it a zero
        if secondDig < 9:# if less than 9
            secondDig += 1 # increment
        else: #if number is 9 
            secondDig = 0 #make it a zero
            if firstDig < 9:
                print("Error: Ran out of Server Names")
                quit()
            firstDig += 1

    firstDigStr = str(firstDig)
    secondDigStr = str(secondDig)
    thirdDigStr = str(thirdDig)
    newSequence = firstDigStr + secondDigStr + thirdDigStr
    currentInstance.sequence = newSequence
    checkDuplicates(currentInstance)
    return newSequence