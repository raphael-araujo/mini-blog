from django.test import TestCase
from django.urls import reverse

from ..models import Blog, Blogger


class BlogListViewTest(TestCase):
    """testa a class-based view que lista os blogs"""
    @classmethod
    def setUpTestData(cls):
        """
        cria 9 blogs, cada um com um título que começa com a string "Blog de número" e termina com o número da variável "blog_id"
        """
        number_of_blogs = 9

        for blog_id in range(1, number_of_blogs + 1):
            Blog.objects.create(
                title=f'Blog de número {blog_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        """
        checa se o URL "/blog/all_blogs/" existe e retorna o código de status 200
        """
        response = self.client.get('/blog/all_blogs/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_acessible_by_name(self):
        """
        testa se a view com o nome "all_blogs" retorna um código de status 200"
        """
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        testa se a view retorna um código de status 200 e se usa o template correto
        """
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/blog_list.html')

    def test_pagination_is_five(self):
        """
        testa se a página está paginada. Caso esteja, então o número de blogs por página deve ser 5
        """
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)

        if response.context['is_paginated']:
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['blog_list']) == 5)
        else:
            self.assertFalse(response.context['is_paginated'])

    def test_lists_all_blogs(self):
        """
        testa a segunda página da lista de blogs. Caso a página esteja paginada, o código de status será 200 e 
        serão mostrados 4 blogs. Se a página não estiver páginada, então o código de status deve ser 404
        """
        response = self.client.get(reverse('all_blogs')+'?page=2')

        if 'is_paginated' in response.context:
            self.assertEquals(response.status_code, 200)
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['blog_list']) == 4)
        else:
            self.assertEquals(response.status_code, 404)


class BloggersListViewTest(TestCase):
    """testa a class-based view que lista os blogueiros"""
    @classmethod
    def setUpTestData(cls):
        """
        cria 9 blogueiros, cada um com um nome, sobrenome e o número da variável "blogger_id"
        """
        number_of_bloggers = 9

        for blogger_id in range(1, number_of_bloggers + 1):
            Blogger.objects.create(
                first_name=f'Autor{blogger_id}',
                last_name=f'Sobrenome do Autor{blogger_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        """
        checa se o URL "/blog/all_bloggers/" existe e retorna o código de status 200
        """
        response = self.client.get('/blog/all_bloggers/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_acessible_by_name(self):
        """
        testa se a view com o nome "all_bloggers" retorna um código de status 200"
        """
        response = self.client.get(reverse('all_bloggers'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        testa se a view retorna um código de status 200 e se usa o template correto
        """
        response = self.client.get(reverse('all_bloggers'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/blogger_list.html')

    def test_pagination_is_five(self):
        """
        testa se a página está paginada. Caso esteja, então o número de blogs por página deve ser 5
        """
        response = self.client.get(reverse('all_bloggers'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)

        if response.context['is_paginated']:
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['blogger_list']) == 5)
        else:
            self.assertFalse(response.context['is_paginated'])

    def test_lists_all_bloggers(self):
        """
        testa a segunda página da lista de blogueiros. Caso a página esteja paginada, o código de status será 200 e 
        serão mostrados 4 blogueiros. Se a página não estiver páginada, então o código de status deve ser 404
        """
        response = self.client.get(reverse('all_bloggers')+'?page=2')

        if 'is_paginated' in response.context:
            self.assertEquals(response.status_code, 200)
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['blogger_list']) == 4)
        else:
            self.assertEquals(response.status_code, 404)
