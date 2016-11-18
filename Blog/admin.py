from django.contrib import admin
from Blog.models import Post, Category, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','category']
    list_filter = ['published','created']
    search_fields = ['title','content','category']
    date_hierarchy = 'created'
    save_on_top = True
    prepopulated_fields = {"slug":["title"]}

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    save_on_top=True

class TagAdmin(admin.ModelAdmin):
    list_display=['title']
    save_on_top=True

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag, TagAdmin)
