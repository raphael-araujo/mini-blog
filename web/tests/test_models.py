from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Blog, Blogger, Comment

# Create your tests here.


class BloggerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blogger.objects.create(
            first_name='Nome',
            last_name='Sobrenome',
            slug='nome-sobrenome'
        )

    def test_first_name_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_slug_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_blogs_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('blogs').verbose_name
        self.assertEquals(field_label, 'blogs')

    def test_first_name_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 64)

    def test_last_name_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 64)

    def test_slug_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('slug').max_length
        self.assertEquals(max_length, 128)

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_first_name_and_last_name(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = f'{blogger.first_name} {blogger.last_name}'
        self.assertEquals(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        expected_url = f'/blog/blogger/{blogger.slug}'
        self.assertEquals(expected_url, blogger. get_absolute_url())


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_author').verbose_name
        self.assertEquals(field_label, 'comment author')

    def test_comment_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('comment_date').verbose_name
        self.assertEquals(field_label, 'comment date')

    def test_commentary_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('commentary').verbose_name
        self.assertEquals(field_label, 'commentary')

    def test_commentary_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('commentary').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_comment_author_and_first_75_letters_commentary(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'\nUser: {comment.comment_author} | {comment.commentary[:75].strip()}...'
        self.assertEquals(expected_object_name, str(comment))


class BlogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self. assertEquals(field_label, 'title')

    def test_slug_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_post_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_author_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_comments_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('comments').verbose_name
        self.assertEquals(field_label, 'comments')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_slug_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('slug').max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length, 2000)

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'\n{blog.title}'
        self.assertEquals(expected_object_name, str(blog))

    def test_absolute_url(self):
        blog = Blog.objects.get(id=1)
        expected_url = f'/blog/{blog.slug}/'
        self.assertEquals(expected_url, blog.get_absolute_url())
