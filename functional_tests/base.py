from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone
from selenium import webdriver

from blog.models import Article


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
