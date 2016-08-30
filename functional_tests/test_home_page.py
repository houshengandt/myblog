from .base import FunctionalTest


class IndexTest(FunctionalTest):

    def test_home_page_shows_recent_articles(self):
        self.browser.get(self.live_server_url)

        self.assertIn("Giraffe's COOK HOUSE", self.browser.title)

        # name = self.browser.find_element_by_css_selector('h1')
        # self.assertEqual(name, "Giraffe's COOK HOUSE")
        #
        # titles = self.browser.find_elements_by_class_name('h2')
        # self.assertContains(titles, 'Title1')
        # self.assertContains(titles, 'Title3')