from .base import FunctionalTest


class ArchivePageTest(FunctionalTest):

    def test_archive_show_articles_by_order(self):
        self.init_db()

        self.browser.get(self.live_server_url + '/archive/')

        titles = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Title1', [title.text for title in titles])
        self.assertEqual('Title3', titles[0].text)
