# Name: Rakesh Deshalli Ravi
# Date: 18 Oct 2023
# Honor statement: I have not given or received any unauthorized assistance on this assignment
# YouTube link:https://youtu.be/oYek3_lIalM
# Assignment 0602: Surf CDM

from collections import Counter
from urllib.request import urlopen, Request
from html.parser import HTMLParser
from urllib.parse import urlsplit, urljoin
import urllib
import re
import html

class UrlCollector(HTMLParser):
    def __init__(self, base_url='https://www.cdm.depaul.edu/'):
        """
        Initialize the UrlCollector instance.

        Args:
            base_url (str): The base URL to start collecting links from.
        """
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.links = []  # List to store collected URLs
        self.words_lst = []  # List to store collected words
        self.in_script = False  # Flag to track if inside <script> tag
        self.in_style = False  # Flag to track if inside <style> tag

    def handle_starttag(self, tag, attrs):
        """
        Handle the start tag of an HTML element.

        Args:
            tag (str): The HTML element tag.
            attrs (list): A list of attribute-value pairs for the tag.
        """
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    # Check if the URL is relative and not already in the list
                    if urlsplit(attr[1]).netloc == '' and urljoin(self.base_url, attr[1]) not in self.links:
                        if not '@cdm.depaul.edu' in attr[1]:
                            self.links.append(urljoin(self.base_url, attr[1]))
        if tag == 'script':
            self.in_script = True
        if tag == 'style':
            self.in_style = True

    def handle_endtag(self, tag):
        """
        Handle the end tag of an HTML element.

        Args:
            tag (str): The HTML element tag.
        """
        if tag == 'script':
            self.in_script = False
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        """
        Handle the data within HTML elements.

        Args:
            data (str): The data content within HTML elements.
        """
        if not self.in_script and not self.in_style:
            # Use a regular expression to remove HTML tags and decode HTML entities
            clean_text = re.sub(r'[a-zA-Z];', ' ', data)
            self.words_lst.extend(clean_text.split())

    def get_collected_urls(self):
        """
        Get the collected URLs from the web page.

        Returns:
            list: A list of collected URLs.
        """
        return self.links

    def get_collected_words(self):
        """
        Get the collected words from the web page.

        Returns:
            list: A list of collected words.
        """
        return self.words_lst

def recursive_url_collection(target_url, urls_lst, counter=0):
    """
    Recursively collect URLs from web pages.

    Args:
        target_url (str): The URL to start collecting from.
        urls_lst (list): A list to store collected URLs.
        counter (int): The recursion counter.

    Returns:
        tuple: A tuple containing collected URLs, recursion count, and error URLs.
        """
    error_url_lst = []  # List to store error URLs
    counter += 1
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = Request(target_url, headers=headers)
        response = urlopen(req)
        html_response = response.read()
        html = html_response.decode()
        collector = UrlCollector()
        collector.feed(html)
        urls_lst.extend(collector.get_collected_urls())
        urls_lst = list(set(urls_lst))
    except urllib.error.URLError:
        error_url_lst.append(target_url)

    if len(urls_lst) > tgtLstLen:
        return (urls_lst[:tgtLstLen], counter, error_url_lst)
    else:
        return recursive_url_collection(urls_lst[counter - 1], urls_lst, counter)

def find_frequent_words(urls_lst):
    """
    Find the most frequent words from a list of URLs.

    Args:
        urls_lst (list): A list of URLs to analyze.

    Returns:
        list: The top 25 most frequent words and their frequencies.
    """
    words_lst = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    for url in urls_lst:
        try:
            req = Request(url, headers=headers)
            response = urlopen(req)
            html_response = response.read()
            html = html_response.decode()
            collector = UrlCollector()
            collector.feed(html)
            words_lst.extend(collector.get_collected_words())
        except urllib.error.URLError:       
            pass

    word_counter = Counter(words_lst)
    return word_counter.most_common(25)

cdm_start_url = 'https://www.cdm.depaul.edu/'
collected_urls = []  # List to store collected URLs
tgtLstLen = 10  # Target length of collected URLs list
collected_urls, recursion_count, error_urls = recursive_url_collection(cdm_start_url, collected_urls, counter=0)

frequent_words_list = find_frequent_words(collected_urls)

print('Top 25 words on the CDM website:')
print('Words and their respective frequencies:')
print(frequent_words_list)
