from django.contrib import admin
from .models import *

# Register your models here.
class FolderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Folder._meta.fields]

    class Meta:
        model = Folder

class FileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in File._meta.fields]

    class Meta:
        model = File

admin.site.register(Folder, FolderAdmin)
admin.site.register(File, FileAdmin)
