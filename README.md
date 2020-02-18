# ServerNaming

## Web application for naming servers to assist users in following server naming conventions.

[http://np-iosws01.temple.edu/form/] 

**Resources:**

    Django documentation [https://docs.djangoproject.com/en/3.0/]

**Access:**

    Site is hosted on the IOS private network and therefore can only be reached from inside this network.

**admin.py:**

    *Username:* admin
    *Password:* TUios2020
    This page gives us access to the database directly. It comes pre-implemented with Django. We are able to edit inputs, delete inputs, and can add timestamps to when servers were created. The admin page is fairly customizable but is currently in the default layout.

**Database:**

    Using a model and sqlite the database for the servers is made. Although it appears to have to seperate tables when the data is populated in the linux servers and windows servers pages, all of the data is put into one table with 24 columns. It is seperated for the user to make it more consistent.

**Model.py: This is where the server object is created .**

    Each server object is one model (Server Details) that is broken down by seven attributes
    **Server Details:**
        *tu* - constant that starts name
        *OS* - linux = “35” /  windows = “30”
        *Purpose* - production = “001” /  non-production = “100” / test = “111”
        *Role* - web = “20”/app = “21”/database = “22”/storage = “23”
        *Sequence* - increments from 000
            Compares to all servers in the same column set as the server object that was just made. The column set is all of the servers that share the same core server name (tu+OS+purpose+role). If an identical server is found then the sequence increments by 1 and repeats until a unique server name is found.
        *Ident* - This is used for mapping purposes and is used for easier reading on the admin page. It is in the format of 3 characters, the first character is for the os the second is for purpose, and the third is for the role. ( Example: “wpw” = windows production web server.)

**Views.py:** 

    There are five views (one for each page): They are home, display server, display linux, display windows, and form. The views play the role of passing data from the models to the template html files. The form is the most crucial view. This is the view that displays the form, verifies and saves the data given by the user. This data is then sent to the model to be processed. 

**URL:** 

    This is where all urls are held that direct users throughout the site. This also tells django what views to look at for which urls.

**Forms.py**:

    This uses the model to create a html form that is sent to the views.

**Export database:**

    Will export all server names as a csv file. This feature is not yet active but is in development.

**Audit:**

    Will compare all server names in database with all server names that follow convention in vmware. This feature is not yet active and is not in development. 
