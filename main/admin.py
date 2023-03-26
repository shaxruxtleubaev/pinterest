from django.contrib import admin
from main.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('title', )
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted_date', 'category', )
    list_display_links = ('title',)
admin.site.register(Post, PostAdmin)