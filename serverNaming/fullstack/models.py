# Create your models here.
from django.db import models
from datetime import date, datetime
class ServerDetails(models.Model):
    # these map variables to their respective strings
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

    # Populates the options for html drop down menu
    # maps the drop down options to their string variable values
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

    tu = models.CharField(max_length = 2, default = "tu") # This does not change
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
    time = models.TimeField()
    time = datetime.now()
    print("Models time:" + str(time))
    sequence = models.CharField(max_length = 100, default = "000")
    serverName = models.CharField(max_length = 100, default = "")
    ident = models.CharField(max_length = 15, default ="")
    # alias = models.CharField(max_length = 15, default="Alias") future feature
    serverIdent = models.CharField(max_length=100, default="")
    print("ident",ident)
    def assignName(self): # This is the string that gets shown on all html pages
        serverName = self.tu + self.purpose + self.role + self.OS + self.sequence
        return serverName

    def __str__(self): # This is the string that gets shown on the admin
        serverName = self.tu + self.purpose + self.role + self.OS + self.sequence
        return serverName


def classifyServer(currentInstance): # currentInstance is the current server that is requesting a name
    #first char = os :: second char: purpose :: third char: role
    classifier={"0012030":"wpw", "0012130": "wpa", "0012230": "wpd", "0012330": "wps",  #windows prod
                "1002030":"wnw", "1002130": "wna", "1002230": "wnd", "1002330": "wns", #windows non prod
                "1112030":"wtw", "1112130": "wta", "1112230": "wtd", "1112330": "wts", #windos test
                "0012035":"lpw", "0012135": "lpa", "0012235": "lpd", "0012335": "lps",  #linux prod
                "1002035":"lnw", "1002135": "lna", "1002235": "lnd", "1002335": "lns", #linux non prod
                "1112035":"ltw", "1112135": "lta", "1112235": "ltd", "1112335": "lts"} #linux test
    currentInstance.ident = classifier.get(currentInstance.purpose+currentInstance.role+currentInstance.OS)
    print("classification: ", currentInstance.ident)

# This mapping is used when placing servers in the html table
# Each ident is mapped to that servers index in the columnSets array that is created below
def classifMap():
    indexForArrayOfSetsMap = {'wpw': 0, 'wpa': 1, 'wpd': 2, 'wps': 3,  #windows prod
                "wnw":4, "wna":5 , "wnd":6,  "wns":7, #windows non prod
                "wtw":8,  "wta":9,  "wtd":10, "wts":11, #windos test
                "lpw":12,  "lpa":13,  "lpd": 14, "lps": 15,  #linux prod
                "lnw":16, "lna": 17,  "lnd":18,  "lns":19, #linux non prod
               "ltw":20, "lta":21, "ltd":22, "lts":23}
    print(indexForArrayOfSetsMap.get('wpw'))
    return indexForArrayOfSetsMap

# Creates an array (columnSets) of sets
# the sets are each category of servers
def createArrayOfSets(servers): # servers is the set of all servers in the database
    columnSets = [
    servers.filter(ident = "wpw"), servers.filter(ident = "wpa"), servers.filter(ident = "wpd"), servers.filter(ident = "wps"),
    servers.filter(ident = "wnw"), servers.filter(ident = "wna"), servers.filter(ident = "wnd"), servers.filter(ident = "wns"),
    servers.filter(ident = "wtw"), servers.filter(ident = "wta"), servers.filter(ident = "wtd"), servers.filter(ident = "wts"),
    servers.filter(ident = "lpw"), servers.filter(ident = "lpa"), servers.filter(ident = "lpd"), servers.filter(ident = "lps"),
    servers.filter(ident = "lnw"), servers.filter(ident = "lna"), servers.filter(ident = "lnd"), servers.filter(ident = "lns"),
    servers.filter(ident = "ltw"), servers.filter(ident = "lta"), servers.filter(ident = "ltd"), servers.filter(ident = "lts")]
    return columnSets

# This checks for duplicates in the entire set of servers
# called by updateSequence()
def checkDuplicates(currentInstance):
    duplicate = False
    serverFilter = ServerDetails.objects.filter( 
                            OS = currentInstance.OS, 
                                purpose = currentInstance.purpose,
                                    role = currentInstance.role,
                                        sequence = currentInstance.sequence)
    for server in serverFilter:
        print("Models: checkDuplicates: Server Set: \n"+server.serverName)
    numOfMatches = serverFilter.count()
    print("Models: checkDuplicates: Number of matches:",numOfMatches)        
    if(numOfMatches > 0):
        duplicate = True;
    return duplicate

# converts the last 3 number characters to ints
# increments each individual int accordingly
# converts the ints back into individual strings
# combines the 3 different strings into one sequence string
# returns the unique sequence to be added to the end of the server name
# increments the sequence and rechecks for duplicats
def updateSequence(currentInstance):
    currentInstSequence = currentInstance.sequence

    #convert string to 3 ints
    firstDig = int(currentInstSequence[0])
    secondDig = int(currentInstSequence[1])
    thirdDig = int(currentInstSequence[2])
    #decimal logic addition
    #since currentInstSequence is a str you can't just increment normally
    if thirdDig < 9: #if less than 9
        thirdDig += 1 # increment by one
    else: #if number is 9
        thirdDig = 0 #make it a zero
        if secondDig < 9:# if less than 9
            secondDig += 1 # increment
        else: #if number is 9 
            secondDig = 0 #make it a zero
            if firstDig < 9:
                print("Error: Ran out of Server Names")
                quit()
            firstDig += 1
    #convert back to string
    firstDigStr = str(firstDig)
    secondDigStr = str(secondDig)
    thirdDigStr = str(thirdDig)
    newSequence = firstDigStr + secondDigStr + thirdDigStr
    currentInstance.sequence = newSequence
    checkDuplicates(currentInstance)
    return newSequence
