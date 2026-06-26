import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


# Create your views here.
def scrape_site(website_url, headers=None):

    # request URL text
    url = website_url
    test_headers={
        'User-Agent': 'UniversityAssignmentScraper/1.0 (contact-email@example.com) Python-Requests/2.31.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
    }

    request_headers = headers or test_headers

    response = requests.get(url, headers=request_headers)

    print(response.text)



scrape_site("https://en.wikipedia.org/wiki/Mepenzolate")