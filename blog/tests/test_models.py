from django.test import TestCase

from blog.models import Article


class ArticleModelTest(TestCase):

    def test_absolute_url(self):
        article = Article.objects.create()
        date = article.pub_time.date()
        self.assertEqual(article.get_absolute_url(), '/' + str(date.year) + '/' + str(date.month) + '/' + str(date.day) + '/' + str(article.pk))
