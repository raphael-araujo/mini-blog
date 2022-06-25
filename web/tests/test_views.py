from django.test import TestCase
from django.urls import reverse

from ..models import Blog


class BlogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 9

        for blog_id in range(1, number_of_blogs + 1):
            Blog.objects.create(
                title=f'Blog de número {blog_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/all_blogs/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_acessible_by_name(self):
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('all_blogs'))
        self.assertEquals(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)

        if response.context['is_paginated']:
            self.assertTrue(response.context['is_paginated'])

            self.assertTrue(len(response.context['blog_list']) == 5)
        else:
            self.assertFalse(response.context['is_paginated'])

    def test_lists_all_blogs(self):
        response = self.client.get(reverse('all_blogs')+'?page=2')

        if 'is_paginated' in response.context:
            self.assertEquals(response.status_code, 200)
            self.assertTrue(response.context['is_paginated'])
            self.assertTrue(len(response.context['blog_list']) == 4)
        else:
            self.assertEquals(response.status_code, 404)
