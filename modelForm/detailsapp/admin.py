from django.contrib import admin
from .models import ServerDetails
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(ServerDetails)
@admin.register(ServerDetails)
class serverAdmin(admin.ModelAdmin):
    search_fields = ['serverName'] # enables the user to search for a server name
    pass
    