from .base import FunctionalTest


class ArticleDetailTest(FunctionalTest):

    def test_detail_page_show_correct_article(self):
        self.init_db()

        self.browser.get(self.live_server_url + self.article1.get_absolute_url())

        title = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(title.text, self.article1.title)