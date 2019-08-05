from bs4 import BeautifulSoup
import time
import os
import sys
sys.path.insert(0,os.path.abspath('..'))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--disable-features=NetworkService')
chrome_options.add_argument("--window-position=0,0");
# chrome_options.add_argument('--headless')
# warnings from recaptcha
import datetime
from src.data_saver import DataSaver
from src.duplicate_post_idx_exception import DuplicatePostIdxException
from multiprocessing import Pool, cpu_count
import multiprocessing
import threading
    
class WhispersScraper():
    """
    A web scraper designed to scrape NUSWhispers's website
    
    Attributes
    ----------
    url : str
        root url to NUSWhispers's website

    Methods
    -------
    scrape_posts()
        Scrapes for all the desired posts
    empty_post_content()
        Empties post_content dictionary
    """
    
    def __init__(self):
        """
        Variables
        ---------
        url : str
            The prefix of the URL to be scraped 
            (default is 'https://nuswhispers.com/tag/')
        chrome_driver : selenium.webdriver.chrome.webdriver.WebDriver
            The Chrome Driver used to scrape webpages
        post_content : dictionary
            Dictionary where the keys are post indices of str type 
            and values are post contents of str type

        """
        self._url = 'https://nuswhispers.com/tag/'
        self._chrome_driver = webdriver.Chrome(chrome_options = chrome_options)
        self.post_content = {}
    
    def empty_post_content(self):
        """
        Empties post_content dictionary 
        """
        self.post_content = {}

    def scrape_posts(self, start_idx, end_idx):    
        """
        Scrapes for all the posts between start_idx and end_idx (inclusive)
        
        Parameters
        ----------
        start_idx : int
            The index of the first post that will be scraped
        end_idx : int
            The index of the last post that will be scraped
        
        """
        for idx in range(start_idx, end_idx + 1):
            self._scrape_post(idx)
        self._chrome_driver.quit()

    def _scrape_post(self, post_idx):
        """
        Scrapes for the content of a single post

        Parameters
        ----------
        post_idx : int
            Index of the post that will be scraped
        Raises
        ------
        DuplicatePostIdxException
            When adding a new post into post_content and the post index
            already exists in post_content
        """
        if post_idx in self.post_content:
            raise DuplicatePostIdxException("The post index already exist.")
        full_url = self._get_full_url(post_idx)
        self._set_url(full_url)
        posts_html = self._get_html()
        post_category, post_text, num_likes, num_comments, post_age , post_num_favs \
                = self._get_post_contents(posts_html)
        if not post_text:
            return
        self.post_content[post_idx] = \
                (post_category, post_text, num_likes, num_comments, post_age, post_num_favs)

    def _get_full_url(self, post_idx):
        """
        Gets the full url of the post that will be scraped
        
        Parameters
        ----------
        post_idx : int
            Index of the post that will be scraped
        """
        return self._url + str(post_idx)
    
    def _set_url(self, full_url):
        """
        Sets URL in Google Chrome

        Parameters
        ----------
        full_url : str
            The full URL of the webpage that we want to get

        """
        self._chrome_driver.get(full_url)
    
    def _get_html(self):
        """
        Gets html from webpage 
        
        Returns
        -------
        html : str
            The HTML of the webpage, converted to str
        """
        time.sleep(1)
        # wait for post to load
        self._load_all_posts()
        html = self._chrome_driver\
                .execute_script('return document.documentElement.outerHTML')
        return html

    def _load_all_posts(self):
        """
        Scrolls down to bottom of the page to ensure all the posts 
        have loaded
        """
        self._chrome_driver.execute_script(\
                "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def _get_post_contents(self, posts_html):
        """
        Gets the contents of the post
        
        Parameters
        ----------
        posts_html : str
            The HTML of the webpage

        Returns
        -------
        post_text : str
            Textual content of the post
        """
        soup = BeautifulSoup(posts_html, 'lxml')
        posts = soup.findAll('div', {'class':'post ng-scope'})
        # All posts with the index in their content is obtained. Thus,
        # posts may contain posts that we may not want.
        post_category, post_text, post_num_likes, post_num_comments, post_age = None, None, None, None, None 
        if not posts:
            return post_category, post_text, num_likes, num_comments, post_age
        desired_post_html = posts[-1] 
        post_category = self._get_post_category_from_html(desired_post_html)
        post_text = self._get_post_text_from_html(desired_post_html)
        num_likes = self._get_post_num_likes_from_html(desired_post_html)
        num_comments = self._get_post_num_comments_from_html(desired_post_html)
        post_age = self._get_post_age_from_html(desired_post_html)
        post_num_favs = self._get_post_num_favourites_from_html(desired_post_html)
        return post_category, post_text, num_likes, num_comments, post_age, post_num_favs

    def _get_post_text_from_html(self, post_html):
        """
        Gets the textual content of the post
        
        Parameters
        ----------
        post_html : str
            The HTML of a post

        Returns:
        -------
        post_text : str
            Textual content of the post
        """
        post_text = ''
        post_content_html = post_html.find('span', 
                {'class':'post-text ng-binding'})
        if post_content_html.string is None:
            # occurs when the post starts with a link
            post_text += (str(post_content_html.find('a')) + " ")
            post_text += (post_content_html.text + '\n')
        else: 
            # usual behaviour
            post_text += (str(post_content_html.string) + '\n')
        return post_text

    def _get_post_num_likes_from_html(self, post_html):
        num_likes_html = post_html.find('a', {'class': 'post-media-action-btn fb-likes ng-binding'})
        num_likes = str(num_likes_html.string)
        return num_likes

    def _get_post_num_comments_from_html(self, post_html):
        num_comments_html = post_html.find('a', {'class': 'post-media-action-btn show-comments-btn ng-binding'})
        num_comments = str(num_comments_html.text)
        return num_comments

    def _get_post_age_from_html(self, post_html):
        post_age_html = post_html.find('span', {'class':'post-time'})
        post_age = str(post_age_html.string)
        return post_age

    def _get_post_category_from_html(self, post_html):
        post_category_html = post_html.findAll('a', {'class':'ng-binding'})[:-4]
        post_category = ''
        for category in post_category_html:
            post_category += (str(category.string) + ' ')
        return post_category
    
    def _get_post_num_favourites_from_html(self, post_html):
        # 13, 62701, 62704
        post_num_favourites_html = post_html.find('a', {'class':'post-media-action-btn favs-count ng-binding'})
        post_num_favourites = str(post_num_favourites_html.string)
        return post_num_favourites


