from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

# This maps the urls to the views
urlpatterns = [
    path('',detailsapp_views.home), 
    path('home/', detailsapp_views.home),
    path('form/', detailsapp_views.form),
    path('displaywindows/', detailsapp_views.displaywindows),
    path('displaylinux/', detailsapp_views.displaylinux),
    path('displayserver/', detailsapp_views.displayserver),
    # path('form/', detailsapp_views.form),
    # path('results/', detailsapp_views.results),
    path('download-windows-csv/', detailsapp_views.windowsTableDownload),
    path('download-linux-csv/', detailsapp_views.linuxTableDownload),
    path('admin/', admin.site.urls),
]
