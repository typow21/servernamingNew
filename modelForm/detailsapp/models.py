# Create your models here.
from django.db import models

class ServerDetails(models.Model):
    blank = "--"
    linux = "35"
    windows = "30"
    
    web = "20"
    app = "21"
    database = "22"
    storage = "23"
    
    prd = "001"
    np = "100"
    test = "111"
    
    OpSys  = (
    (blank,"--"),
    (linux, "Linux/Unix"),
    (windows, "Windows"),
    )
    PURPOSE = (
    (blank,"--"),
    (prd, "Production"),
    (np, "Non-Production"),
    (test, "Test"),
    )
    ROLE = (
    (blank,"--"),
    (web, "Web"),
    (app, "Application"),
    (database, "Database"),
    (storage, "Storage"),
    )

    tu = models.CharField(max_length = 2, default = "tu")
    OS = models.CharField(
        max_length = 10,
        choices = OpSys,
        default = blank,
    )
    purpose = models.CharField(
        max_length = 10,
        choices = PURPOSE,
        default = blank,
    )
    role = models.CharField(
        max_length = 10,
        choices = ROLE,
        default = blank,
    )
    sequence = models.CharField(max_length = 100, default = "000")
    serverName = models.CharField(max_length = 100, default = "")
    ident = models.CharField(max_length = 15, default ="")
    # alias = models.CharField(max_length = 15, default ="Alias") future feature
    print("ident",ident)
    def assignName(self):
        serverName = self.tu + self.OS + self.purpose + self.role + self.sequence
        return serverName

def classifyServer(currentInstance):
    #first char = os :: second char: purpose :: third char: role
    classifier={"3000120":"wpw", "3000121": "wpa", "3000122": "wpd", "3000123": "wps",  #windows prod
                "3010020":"wnw", "3010021": "wna", "3010022": "wnd", "3010023": "wns", #windows non prod
                "3011120":"wtw", "3011121": "wta", "3011122": "wtd", "3011123": "wts", #windos test
                "3500120":"lpw", "3500121": "lpa", "3500122": "lpd", "3500123": "lps",  #linux prod
                "3510020":"lnw", "3510021": "lna", "3510022": "lnd", "3510023": "lns", #linux non prod
                "3511120":"ltw", "3511121": "lta", "3511122": "ltd", "3511123": "lts"} #linux test
    currentInstance.ident = classifier.get(currentInstance.OS+currentInstance.purpose+currentInstance.role)
    print("classification: ", currentInstance.ident)

def createArrayOfSets(servers):
    columnSets = [
    servers.filter(ident = "wpw"),servers.filter(ident = "wpa"),servers.filter(ident = "wpd"),servers.filter(ident = "wps"),
    servers.filter(ident = "wnw"),servers.filter(ident = "wna"),servers.filter(ident = "wnd"),servers.filter(ident = "wns"),
    servers.filter(ident = "wtw"),servers.filter(ident = "wta"),servers.filter(ident = "wtd"),servers.filter(ident = "wts"),
    servers.filter(ident = "lpw"),servers.filter(ident = "lpa"),servers.filter(ident = "lpd"),servers.filter(ident = "lps"),
    servers.filter(ident = "lnw"),servers.filter(ident = "lna"),servers.filter(ident = "lnd"),servers.filter(ident = "lns"),
    servers.filter(ident = "ltw"),servers.filter(ident = "lta"),servers.filter(ident = "ltd"),servers.filter(ident = "lts")]
    return columnSets

def checkDuplicates(currentInstance):
    duplicate = False
    newSequence = currentInstance.sequence
    numOfMatches = ServerDetails.objects.filter(
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
        # print("Current Inst Seq: ", newSequence)
        
    return duplicate

def updateSequence(currentInstance):
    # print("reached 1")
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