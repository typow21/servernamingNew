from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

urlpatterns = [
    path('home/', detailsapp_views.home),
    path('form/', detailsapp_views.form),
    path('displaywindows/', detailsapp_views.displaywindows),
    path('displaywindowsedit/',detailsapp_views.displaywindowsedit),
    path('displaylinux/', detailsapp_views.displaylinux),
    path('displaylinuxedit/', detailsapp_views.displaylinuxedit),
    path('displayserver/', detailsapp_views.displayserver),
    # path('form/', detailsapp_views.form),
    # path('results/', detailsapp_views.results),
    path('admin/', admin.site.urls),
]
