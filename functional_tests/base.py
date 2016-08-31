from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone
from selenium import webdriver

from blog.models import Article, Tags


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def init_db(self):
        self.article1 = Article.objects.create(title='Title1', abstract='abstract for article1')
        self.article2 = Article.objects.create(title='Title2', abstract='abstract for article2')
        self.article3 = Article.objects.create(title='Title3', abstract='abstract for article3')
        self.tag1 = Tags.objects.create(tag_name='Tag1')
        self.tag2 = Tags.objects.create(tag_name='Tag2')
        self.tag1.article.add(self.article1)
        self.tag1.article.add(self.article2)
        self.tag2.article.add(self.article2)
        self.tag2.article.add(self.article3)
