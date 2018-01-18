# -*- coding: utf-8 -*-

import urllib2
import urlparse
from bs4 import BeautifulSoup

class News(object):
	def __init__(self):
		self.results = []
		self.searches = []
		self.categories = []
		self.news_array = ''
		self.url = ''
		

class BBC(News):
	def __init__(self):
		super(BBC, self).__init__()
		self.url = "http://www.bbc.com/news"

	def search(self, searches=[]):
		self.searches = searches
		self.bbc_news_results = []

		page = urllib2.urlopen(self.url)
		soup = BeautifulSoup(page.read(), "lxml")
		top_news = soup.findAll("div", attrs={"class":"nw-c-top-stories"})
		news = soup.findAll("div", attrs={"class":"nw-c-top-stories__secondary-item"})
		
		self.bbc_news_results += self.__parseResults__(top_news)
		self.bbc_news_results += self.__parseResults__(news)

		print self.bbc_news_results


	def __parseResults__(self, news):
		result = []
		for item in news:
			current_result = {}
			try:
				image_src = unicode(item.img["src"])
				promo = item.find(attrs={"class":"gs-o-list-inline"})
				# How long the new has been in the air
				time = unicode(promo.findAll("li")[0].text)
				# The region of the news
				region = unicode(promo.findAll("li")[1].text)
				title = unicode(item.find(attrs={"class":"gs-c-promo-heading"}).text)
				summary = unicode(item.find(attrs={"class":"gs-c-promo-summary"}).text)
				href = unicode(item.find("a", attrs={"class":"gs-c-promo-heading"})['href'])

				# Put everything into the dictionary
				current_result["img_src"] = image_src
				current_result["time"] = time
				current_result["region"] = region
				current_result["title"] = title
				current_result["summary"] = summary
				current_result["href"] = href

				result.append(current_result)

			except:
				pass

		return result





def main():
	bbc = BBC()
	bbc.search()

if __name__ == "__main__":
	main()