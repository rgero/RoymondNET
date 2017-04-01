from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["post_title","author","created_date","published_date"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
