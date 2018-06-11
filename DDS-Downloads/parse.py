import requests
from lxml import html # parser
from bs4 import BeautifulSoup

page = "http://www.digitalglobe.com/opendata/hurricane-harvey/post-event"

req = requests.get(page)
soup = BeautifulSoup(req.content, "html.parser")



for textarea in soup.findAll("textarea"):	
	links_file = open(str(textarea['id']).split('-')[1] + '.txt', 'w+')
	links = textarea.text.split()
	for link in links:
		links_file.write(link + '\n')
