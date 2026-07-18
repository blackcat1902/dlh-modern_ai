#!/usr/bin/env python3
"""
Module for fetching HTML content from a given URL using the requests library.
"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """
    Fetches the HTML content of a web page.

    Args:
        url (str): The URL of the page to retrieve.
        headers (dict, optional): HTTP headers to send with the request.
        timeout (int): The number of seconds to wait before aborting.

    Returns:
        str: The full HTML content of the response as a string.
    """
    # Send the GET request with the optional headers and timeout
    response = requests.get(url, headers=headers, timeout=timeout)
    
    # Automatically raise an exception if the HTTP status code is >= 400
    response.raise_for_status()
    
    # Return the full HTML of the response as a string
    return response.text
