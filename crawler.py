from lxml import html
import requests


class Crawler():

    """ Crawls quotes from certain websites using given urls and xpath """

    def __init__(self, *url_xpath_tuples):

        """ Constructor

        Keyword arguments:
        url_xpath_tuples -- tuple(s) of (url, xpath)
        """

        self.url = []
        self.xpath = []

        for url, xpath in url_xpath_tuples:
            if not isinstance(url, str):
                raise ValueError
            if not isinstance(xpath, str):
                raise ValueError
            self.url.append(url)
            self.xpath.append(xpath)

    def add_url_xpath(self, url, xpath):

        """ Add a url and xpath to crawl

        Keyword arguments:
        url -- url of a website
        xpath -- the xpath of the elements in the website
            read https://www.w3schools.com/xml/xpath_intro.asp if unsure.
        """

        self.url.append(url)
        self.xpath.append(xpath)

    def crawl(self):

        """ Crawl through the given websites and return the elements found
            at the given xpath.
        """

        result = []

        for i, url in enumerate(self.url):
            xpath = self.xpath[i]
            # Fetch HTML from url
            page = requests.get(url)
            tree = html.fromstring(page.content)
            elements = tree.xpath(xpath)
            for element in elements:
                if element.text:
                    result.append((element.text, url))
        return result
