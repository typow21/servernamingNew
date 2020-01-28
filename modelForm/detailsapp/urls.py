from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

urlpatterns = [
    path('userdetails/', detailsapp_views.serverDetails),
    path('display/', detailsapp_views.serverDetails),
    # path('form/', detailsapp_views.form),
    # path('results/', detailsapp_views.results),
    path('admin/', admin.site.urls),
]
