from .base import FunctionalTest

from blog.models import Article


class IndexTest(FunctionalTest):

    def test_home_page_shows_recent_articles(self):
        self.init_db()

        self.browser.get(self.live_server_url)

        self.assertIn("Giraffe's COOK HOUSE", self.browser.title)

        name = self.browser.find_element_by_css_selector('h1')
        self.assertEqual(name.text, "Giraffe's COOK HOUSE")

        titles = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Title1', [title.text for title in titles])
        self.assertIn('Title3', [title.text for title in titles])

        abstract = self.browser.find_elements_by_tag_name('p')
        self.assertEqual(abstract[0].text, self.article3.abstract)  # 同时测试排序，最新发布的在前面

        button = self.browser.find_elements_by_tag_name('a')
        self.assertIn(self.article1.get_absolute_url(), button[2].get_attribute('href'))
