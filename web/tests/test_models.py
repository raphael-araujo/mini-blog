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
