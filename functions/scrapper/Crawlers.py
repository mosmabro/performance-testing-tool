import sys
import traceback
import urllib.request
from bs4 import BeautifulSoup
# ---------------------------------------------------------------------------------------------------------
# Description: ImagesCrawler is a website bot that scans for images URLs.
# Usage: The constructor takes 2 params:
#           1. website: the URL at which the crawler will start scanning
#           2. depth: the links depth. If higher than 1, stories or news pages will be scanned for images
# ---------------------------------------------------------------------------------------------------------
class ImagesCrawler:
    
    def __init__(self, website, depth):
        self.baseUrl = website
        self.depth = depth
        self.visitedUrls = []
        self.imagesUrls = []
    
    def crawle(self, url='', depth=1):
        page=urllib.request.urlopen(self.baseUrl+url)
        #If http status is not 200, stop crawling
        if page.status!=200:
            return
        soup = BeautifulSoup(page.read(),features="html.parser")
        # Getting images uris that starts with /images to avoid capturing static (headers, footers.. etc) or ads images
        self.imagesUrls += [link.get('src') for link in soup.find_all('img') if link.get('src') != None and link.get('src').startswith('/images')]
        # Getting stories links in the home page
        links = [link.get('href') for link in soup.find_all('a') if link.get('href')!=None and link.get('href').startswith('/') and 'stories' in link.get('href')]
        # Storing the visited urls to avoid revisiting them again
        self.visitedUrls.append('/')
        # Resursively calling the crawling logic
        for link in links:
            if link != None and link not in self.visitedUrls:
                print('Crawling URL: '+link)
                self.visitedUrls.append(link)
                links.append(recursiveUrl(self,link,depth+1))
        return links.append(links)