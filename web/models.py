from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Blogger(models.Model):
    name = models.CharField(max_length=64, help_text='enter a blogger name')
    bio = models.TextField(max_length=500, null=True, blank=True)
    # blogs = models.ForeignKey(Blog)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=self.name)


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    commentary = models.TextField(max_length=500)

    def __str__(self):
        return self.comment_author


class Blog(models.Model):
    title = models.CharField(max_length=100, help_text='Blog title')
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500)
    comments = models.ManyToManyField(Comment, help_text='comments for this post')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=self.title)
