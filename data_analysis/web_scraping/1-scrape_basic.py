#!/usr/bin/env python3
"""
Module for scraping quotes from quotes.toscrape.com using BeautifulSoup.
"""
from bs4 import BeautifulSoup

# Importing the fetch_html function from the previous task
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Scrapes the first page of quotes from the given URL.

    Args:
        url (str): The Quotes List endpoint URL.

    Returns:
        list: A list of dictionaries containing text, author, and tags.
    """
    # 1. Fetch the raw HTML content using our previous function
    html_content = fetch_html(url)
    
    # 2. Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 3. Initialize an empty list to store our structured data
    quotes_list = []
    
    # 4. Find all the quote blocks on the page
    # Each quote on this website is contained within a div with class="quote"
    quote_blocks = soup.find_all('div', class_='quote')
    
    # 5. Loop through each quote block and extract details
    for block in quote_blocks:
        # Extract the text of the quote (found in <span class="text">)
        text = block.find('span', class_='text').get_text(strip=True)
        
        # Extract the author (found in <small class="author">)
        author = block.find('small', class_='author').get_text(strip=True)
        
        # Extract all tags (found in <a class="tag"> inside a div with class="tags")
        tag_elements = block.find_all('a', class_='tag')
        tags = [tag.get_text(strip=True) for tag in tag_elements]
        
        # 6. Append the structured data into our results list
        quotes_list.append({
            "text": text,
            "author": author,
            "tags": tags
        })
        
    return quotes_list