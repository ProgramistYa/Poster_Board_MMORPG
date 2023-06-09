from django.contrib import admin
from .models import Post, Response, Category, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'dateCreation']
    list_filter = ('author', 'dateCreation')


admin.site.register(Post, PostAdmin)
admin.site.register(Response)
admin.site.register(Category)
admin.site.register(Author)