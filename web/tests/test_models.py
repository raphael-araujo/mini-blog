from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Blog, Blogger, Comment


class BloggerModelTest(TestCase):
    """testa o modelo Blogger"""

    @classmethod
    def setUpTestData(cls):
        """
        cria um objeto Blogger com os campos first_name, last_name e slug preenchidos e salva no banco de dados

        :param cls: Este é o objeto de classe
        """
        Blogger.objects.create(
            first_name='Nome',
            last_name='Sobrenome',
            slug='nome-sobrenome'
        )

    def test_first_name_label(self):
        """
        testa se o título do campo "first_name" é igual a "first name"
        """
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        """
        testa se o título do campo "last_name" é igual a "last name"
        """
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_slug_label(self):
        """
        testa se o título do campo "slug" é igual a "slug"
        """
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_bio_label(self):
        """
        testa se o título do campo "bio" é igual a "bio"
        """
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_blogs_label(self):
        """
        testa se o título do campo "blogs" é igual a "blogs"
        """
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('blogs').verbose_name
        self.assertEquals(field_label, 'blogs')

    def test_first_name_max_length(self):
        """
        testa o comprimento máximo do campo "first_name" no modelo Blogger
        """
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 64)

    def test_last_name_max_length(self):
        """
        testa o comprimento máximo do campo "last_name" no modelo Blogger
        """
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 64)

    def test_slug_max_length(self):
        """
        testa o comprimento máximo do campo "slug" no modelo Blogger
        """
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('slug').max_length
        self.assertEquals(max_length, 128)

    def test_bio_max_length(self):
        """
        testa o comprimento máximo do campo "bio" no modelo Blogger
        """
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_first_name_and_last_name(self):
        """
        testa se o nome do objeto é formado pelo nome e sobrenome do blogueiro
        """
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f'{blogger.first_name} {blogger.last_name}'
        self.assertEquals(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        """
        testa se o método get_absolute_url() retorna o URL esperado
        """
        blogger = Blogger.objects.get(id=1)
        expected_url = f'/blog/blogger/{blogger.slug}'
        self.assertEquals(expected_url, blogger. get_absolute_url())


class CommentModelTest(TestCase):
    """testa o modelo Comment"""
    @classmethod
    def setUpTestData(cls):
        """
        cria um usuário e um comentário, depois associa o comentário com o usuário que foi criado
        """
        user = User.objects.create(
            username='Usuario',
            password='Senha123'
        )

        Comment.objects.create(
            comment_author=user,
            comment_date=datetime.now(),
            commentary='Comentário de teste.'
        )

    def test_comment_author_label(self):
        """
        testa se o título do campo "comment_author" é igual a "comment author"
        """
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_author').verbose_name
        self.assertEquals(field_label, 'comment author')

    def test_comment_date_label(self):
        """
        testa se o título do campo "comment_date" é igual a "comment date"
        """
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_date').verbose_name
        self.assertEquals(field_label, 'comment date')

    def test_commentary_label(self):
        """
        testa se o título do campo "commentary" é igual a "commentary"
        """
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('commentary').verbose_name
        self.assertEquals(field_label, 'commentary')

    def test_commentary_max_length(self):
        """
        testa o comprimento máximo do campo "commentary" no modelo Comment
        """
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('commentary').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_comment_author_and_first_75_letters_commentary(self):
        """
        testa se o nome do objeto é formado pelo autor do comentário e pelos primeiros 75 caracteres do comentário
        """
        comment = Comment.objects.get(id=1)
        expected_object_name = f'\nUser: {comment.comment_author} | {comment.commentary[:75].strip()}...'
        self.assertEquals(expected_object_name, str(comment))


class BlogModelTest(TestCase):
    """testa o modelo Blog"""
    @classmethod
    def setUpTestData(cls):
        """
        cria um blogueiro e um blog, depois associa o blog com o blogueiro que foi criado
        """
        blogger = Blogger.objects.create(
            first_name='Nome',
            last_name='Sobrenome'
        )

        Blog.objects.create(
            title='um Título de um Blog',
            slug='um-titulo-de-um-blog',
            post_date=datetime.now(),
            author=blogger,
            description='O conteúdo do blog'
        )

    def test_title_label(self):
        """
        testa se o título do campo "title" é igual a "title"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self. assertEquals(field_label, 'title')

    def test_slug_label(self):
        """
        testa se o título do campo "slug" é igual a "slug"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_post_date_label(self):
        """
        testa se o título do campo "post_date" é igual a "post date"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_author_label(self):
        """
        testa se o título do campo "author" é igual a "author"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_description_label(self):
        """
        testa se o título do campo "description" é igual a "description"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_comments_label(self):
        """
        testa se o título do campo "comments" é igual a "comments"
        """
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_title_max_length(self):
        """
        testa o comprimento máximo do campo "title" no modelo Blog
        """
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_slug_max_length(self):
        """
        testa o comprimento máximo do campo "slug" no modelo Blog
        """
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('slug').max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        """
        testa o comprimento máximo do campo "description" no modelo Blog
        """
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_title(self):
        """
        testa se o nome do objeto é formado pelo título do blog
        """
        blog = Blog.objects.get(id=1)
        expected_object_name = f'\n{blog.title}'
        self.assertEquals(expected_object_name, str(blog))

    def test_absolute_url(self):
        """
        testa se o método get_absolute_url() retorna o URL esperado
        """
        blog = Blog.objects.get(id=1)
        expected_url = f'/blog/{blog.slug}/'
        self.assertEquals(expected_url, blog.get_absolute_url())
