from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

urlpatterns = [
    path('userdetails/', detailsapp_views.userDetails),
    path('display/', detailsapp_views.userDetails),
    # path('form/', detailsapp_views.form),
    # path('results/', detailsapp_views.results),
    path('admin/', admin.site.urls),
]
