from django.contrib import admin
from .models import ServerDetails
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(ServerDetails)
# @admin.register(View)
# class ViewAdmin(ImportExportModelAdmin):
#     pass