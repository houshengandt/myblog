from django.test import TestCase


class IndexViewTest(TestCase):

    def test_index_render_the_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/index.html')