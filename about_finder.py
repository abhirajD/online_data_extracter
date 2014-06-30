import os
import re
import simplejson
import mechanize
import unicodedata
import sys
import itertools

def find_about(link):
	br = mechanize.Browser()
	response = br.open(link)
	site_data = '<a href="/about" title="">About Us</a>'

	pattern = "<a.*?>about(.*?)</a>"
	li = re.search(pattern,site_data,re.I)

	pattern1 = "<a.*?>(.*?)</a>"
	match = li.group() ; match = re.findall(pattern1 , match) ; match = match[0]
	print match
	
	# for link in br.links(text='About Us'):
	# 	print link


find_about('http://www.gcoea.ac.in/home')