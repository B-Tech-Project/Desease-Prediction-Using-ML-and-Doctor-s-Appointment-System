from django.contrib import admin
from .models import DatabaseFiles, Symptom
# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ('File_Type', 'File_Path')


admin.site.register(DatabaseFiles, FileAdmin)
admin.site.register(Symptom)
