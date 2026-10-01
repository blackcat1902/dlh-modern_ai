Web Scraping Data Collection
0-fetch_html.py
Write a function def fetch_html(url, headers = None, timeout = 10): that fetches a web page and returns its HTML as text:

 url is the page to retrieve
 headers is an optional dict of HTTP headers (e.g. {"User-Agent": "…”})
 timeout is the number of seconds to wait before aborting
 Must raise an exception on any HTTP status ≥ 400
 Returns: the full HTML of the response as a string
Only import: import requests

1-scrape_basic.py
Write a function def scrape_basic(url): that scrapes the first page of quotes from quotes.toscrape.com:

[x]
 url is the Quotes List endpoint (e.g. https://quotes.toscrape.com/)
 Use fetch_html() to retrieve the HTML then parse it with BeautifulSoup
 Extract for each quote block:
"text": the quote text
"author": the quote’s author
"tags": a list of tag strings
 You are not allowed to use regular expressions for this task
 Returns: a list of dicts, e.g. [{ "text": "...", "author": "...", "tags": [...] }, …]
Imports: from bs4 import BeautifulSoup and fetch_html = __import__('0-fetch_html').fetch_html

2-scrape_paginated.py
Write a function def scrape_paginated(base_url): that follows “Next” links on quotes.toscrape.com until no more pages remain:

 base_url is the first page URL (https://quotes.toscrape.com/)
 Must detect and follow the
link dynamically
 Implement delays between requests (e.g. time.sleep)
 Combine results from all pages into one list
 Returns: the full list of quote dicts (same format as Task 1)
Imports: from bs4 import BeautifulSoup, import time, from urllib import parse, fetch_html = __import__('0-fetch_html').fetch_html and scrape_basic = __import__('1-scrape_basic').scrape_basic

3-scrape_via_api.py
Write a function def scrape_via_api(base_url): that fetches quote data from all the quotes' API pages:

 base_url is the root URL of the site (e.g. "https://quotes.toscrape.com")
 Build each page’s API endpoint starting from page one (/api/quotes?page=1)
 Use fetch_html() to retrieve the JSON payload
 From each page’s "quotes" array, extract:
"text": the quote text
"author": the author’s name
"tags": the list of tags
 Return: a list of quote dicts, each with keys "text", "author", and "tags"
Imports: import json and fetch_html = __import__('0-fetch_html').fetch_html

4-extract_jsonld.py
Write a function def extract_jsonld(url): that pulls quotes from embedded JSON‑LD on a page:

 url is the Quotes List endpoint (e.g. "https://quotes.toscrape.com/")
 Use fetch_html() to fetch the HTML
 Locate all <script type="application/ld+json"> blocks and parse each with json.loads()
 From each JSON‑LD object of "@type": "Quote", extract:
 "text": the quote text (.get("text"))
 "author": the author’s name (.get("author", {}).get("name"))
 "tags": keywords, (p.s. split into a list if provided as a comma-separated string)
 Return: a list of quote dicts, each with keys "text", "author", and "tags"
Imports: import json, from bs4 import BeautifulSoup and fetch_html = __import__('0-fetch_html').fetch_html

5-login_and_scrape.py
Write a function def login_and_scrape(login_url, user, pwd): that logs in and scrapes quotes visible only after authentication:

 login_url is the login page (e.g. "https://quotes.toscrape.com/login")
 Use requests.Session() to persist cookies across requests
 GET the login form and extract the CSRF token from
 POST credential fields (username, password, csrf_token) back to login_url
 After successful login, GET the protected quotes page (https://quotes.toscrape.com/)
 Use BeautifulSoup to parse each <div class="quote"> and extract:
"text": the quote text
"author": the author’s name
"tags": a list of tag strings
 Return: a list of quote dicts, each with keys "text", "author", and "tags"
Imports: import requests, from bs4 import BeautifulSoup

6-products_list.py
Write a function def scrape_products_list(url): that opens a static product category page and returns a list of product dictionaries. Each dict should have:

[x]"title": the product’s name (from the title attribute of the tag)
[x]"price": the product’s price (text of the
element)
[x]"description": the product’s description (text of the
)

[x]"rating": the number of stars (
under .ratings)

Imports: import time, from selenium import webdriver

For this task 6 and the rest of the tasks:
Use only Selenium (webdriver, By, etc.)
Run Chrome in headless mode in a 1920 by 1080 window and no sandbox.
Don’t use BeautifulSoup or regex
7-product_detail.py
Scrape Single Product Detail

Write a function def scrape_product_detail(url, delay=2.0): that opens a detail page for one product, waits delay seconds, and returns a dictionary with:

[x]"title": the product title (the second
inside .caption)
[x]"price": the price (text of the first
)
[x]"description": the full description (text of
)

[x]"rating": the number of stars (count of
in .ratings)

Use only Selenium with find_element(s), CSS selectors, and no external parsers.

Imports: import time, from selenium import webdriver

8-scroll_and_scrape.py
Write a function def scroll_and_scrape(url, scroll_pause=2.0): that scrolls and extracts all products from a JS‐rendered infinite‐scroll page

The function should:

 Open the given infinite-scroll page in headless Chrome.
 Scroll to the bottom repeatedly, waiting scroll_pause seconds each time, until the page height stops increasing.
 Find every div.thumbnail product card and extracts:
 "title": the product name (from the title attribute of )
 "price": the price (text of
)
 "description": the short description (text of
)

 "rating": the star count (number of
under .ratings)

 Skip duplicate products by tracking (title, price) pairs.
 Return a list of unique product dicts, e.g.
 Use only Selenium’s execute_script for scrolling and its element-finding APIs for extraction.
Imports: import time, from selenium import webdriver