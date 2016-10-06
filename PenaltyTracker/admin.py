from django.contrib import admin

# Register your models here.
from .models import SearchOptionGroup,Option

admin.site.register(SearchOptionGroup)
admin.site.register(Option)