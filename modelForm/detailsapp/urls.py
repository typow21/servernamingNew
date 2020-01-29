from django.urls import path
from django.contrib import admin

from detailsapp import views as detailsapp_views

urlpatterns = [
    path('form/', detailsapp_views.form),
    path('displaywindow/', detailsapp_views.form),
    path('displaylinux/', detailsapp_views.form),
    path('displayserver/', detailsapp_views.form),
    # path('form/', detailsapp_views.form),
    # path('results/', detailsapp_views.results),
    path('admin/', admin.site.urls),
]
