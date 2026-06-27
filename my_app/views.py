import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


# Create your views here.
def run_website_scrape(website_url, headers=None):
    
    # get website html
    html = get_website_html(website_url, headers)

    # parse and find urls
    urls = find_urls(html.text)

    return urls



def get_website_html(website_url, headers=None):

    # request URL text
    url = website_url
    test_headers={
        'User-Agent': 'UniversityAssignmentScraper/1.0 (contact-email@example.com) Python-Requests/2.31.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    request_headers = headers or test_headers

    response = requests.get(
        url
        , headers=request_headers
        , timeout=30)

    # print(response.text)

    return response


def find_urls(html_content):
    
    soup = BeautifulSoup(html_content, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url:  # Ensure the a tag actually has an href attribute
            urls = urls.append(url) if url in urls else urls  # Quick duplicate check if needed
            urls.append(url)

    return urls


def render_form():
