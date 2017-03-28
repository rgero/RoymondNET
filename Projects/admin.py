from django.contrib import admin
from .models import *

class ProjectPageAdmin(admin.ModelAdmin):
    list_display = ("pageTitle", "language")


# Register your models here.
admin.site.register(Language)
admin.site.register(ProjectPage, ProjectPageAdmin)
