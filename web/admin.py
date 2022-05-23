from django.contrib import admin
from .models import Blog, Blogger, Comment

# Register your models here.

admin.site.register(Comment)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # mostra as colunas "title", "author" e "post_date" na tabela de blog na página de admin do django:
    list_display = ('title', 'author', 'post_date')

    # preenche automaticamente o campo "slug" com o título do blog, para ser utilizado no url:
    prepopulated_fields = {"slug": ("title",)}

    # campo apenas para leitura:
    readonly_fields = ['comments']


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    # ordena os dados em orbem alfabética, seguindo o primeiro nome do blogueiro:
    ordering = ('first_name',)

    # preenche automaticamente o campo "slug" com o primeiro e o último nome do blogueiro, para ser utilizado no url:
    prepopulated_fields = {"slug": ("first_name", "last_name")}
