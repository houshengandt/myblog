from django.test import TestCase

from blog.models import Article, Tags


class ArticleModelTest(TestCase):

    def test_absolute_url(self):
        article = Article.objects.create()
        date = article.pub_time.date()
        self.assertEqual(article.get_absolute_url(), '/' + str(date.year) + '/' + str(date.month) + '/' + str(date.day) + '/' + str(article.pk))


class TagsModelTest(TestCase):

    def test_many_to_many_relation(self):
        article1 = Article.objects.create()
        article2 = Article.objects.create()
        article3 = Article.objects.create()
        tag1 = Tags.objects.create(tag_name='Tag1')
        tag2 = Tags.objects.create(tag_name='Tag2')
        tag1.article.add(article1)
        tag1.article.add(article2)
        tag1.article.add(article3)
        tag2.article.add(article2)
        tag2.article.add(article3)

        self.assertEqual(tag1.article.count(), 3)
        self.assertEqual(tag2.article.count(), 2)

        self.assertEqual(article1.tags.count(), 1)
        self.assertEqual(article3.tags.count(), 2)