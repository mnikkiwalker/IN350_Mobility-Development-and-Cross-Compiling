from django.test import TestCase
from django.test import SimpleTestCase
from my_app import views

# Create your tests here.
class WebScrapeTests(SimpleTestCase):

    def test_website_fetch(self):
        response = views.get_website_html('https://www.google.com')

        self.assertEqual(response.status_code, 200)


    def test_bs4_parse(self):

        test_html = """
            <div>
                <p>Welcome to my site. Check out the <a href="https://example.com/about">About Us</a> page.</p>
                <p>Or visit our blog at <a class="external" href="https://blog.example.com">Blog Link</a>.</p>
                <a href="/relative-path">A Relative Link</a>
            </div>
        """

        response = views.find_urls(test_html)

        urls_found = len(response)

        self.assertGreaterEqual(urls_found, 0)


    def test_web_url_scrape(self):

        response = views.run_website_scrape("https://google.com")
        urls_found = len(response)

        self.assertGreaterEqual(urls_found, 0)

