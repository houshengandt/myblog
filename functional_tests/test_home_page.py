from .base import FunctionalTest

from blog.models import Article


class IndexTest(FunctionalTest):

    def test_home_page_shows_recent_articles(self):
        self.init_db()

        self.browser.get(self.live_server_url)

        self.assertIn("Giraffe's COOK HOUSE", self.browser.title)

        name = self.browser.find_element_by_id('id-site-title')
        self.assertEqual(name.text, "ZhiyuC")

        titles = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Title1', [title.text for title in titles])
        self.assertIn('Title3', [title.text for title in titles])

        article_list = self.browser.find_element_by_id('id-article-list')
        abstract = article_list.find_elements_by_tag_name('p')
        self.assertEqual(abstract[0].text, self.article3.abstract)

        article_list = self.browser.find_element_by_tag_name('h2')
        button = article_list.find_element_by_tag_name('a')
        self.assertIn(self.article3.get_absolute_url(), button.get_attribute('href'))

    def test_home_page_show_tags(self):
        self.init_db()

        self.browser.get(self.live_server_url)

        tags = self.browser.find_element_by_css_selector('div.tags')
        tag = tags.find_elements_by_tag_name('a')
        num = tags.find_elements_by_tag_name('span')
        self.assertIn(self.tag1.tag_name, tag[0].text)
        self.assertEqual(self.tag1.article.count(), int(str(num[0].text).strip('(').strip(')')))
