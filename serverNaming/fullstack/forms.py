from django.forms import ModelForm
from detailsapp.models import ServerDetails
from django import forms

class ServerModelForm(ModelForm):
        # turn into radio buttons
        # osChoices = forms.ChoiceField(choices=ServerDetails.OpSys, widget = forms.RadioSelect())
        # purposeChoice = forms.ChoiceField(choices=ServerDetails.PURPOSE, widget = forms.RadioSelect())
        # roleChoice = forms.ChoiceField(choices=ServerDetails.ROLE, widget = forms.RadioSelect())
        class Meta:
                model = ServerDetails
                fields = ['OS','purpose','role']

# class selectionForm(ModelForm):
#         class Meta:

                







































# from django import forms

# class ServerNameForm(forms.Form):
#     blank = "--"
#     linux = "35"
#     windows = "30"
    
#     web = "20"
#     app = "21"
#     database = "22"
#     storage = "23"
    
#     prd = "001"
#     np = "100"
#     test = "111"
    
#     OS  = (
#     (blank,"--"),
#     (linux, "Linux/Unix"),
#     (windows, "Windows"),
#     )
#     PURPOSE = (
#     (blank,"--"),
#     (prd, "prd"),
#     (np, "np"),
#     (test, "test"),
#     )
#     ROLE = (
#     ("--","--"),
#     (web, "web"),
#     (app, "app"),
#     (database, "db"),
#     (storage, "storage"),
#     )
#     os  = forms.ChoiceField(
          
#             choices = OS,
            
#             )
#     purpose = forms.ChoiceField(
           
#             choices = PURPOSE,
           
#             )
#     role = forms.ChoiceField(
        
#             choices = ROLE,
            
#             )