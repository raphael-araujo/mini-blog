from django.contrib import admin
from .models import Blog, Blogger, Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ['comments']


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    ordering = ('first_name',)
    prepopulated_fields = {"slug": ("first_name", "last_name")}

