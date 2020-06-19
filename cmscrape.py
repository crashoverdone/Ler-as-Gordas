import requests
from bs4 import BeautifulSoup
import re
import os

def get_data(noticia):
	result = []

	if noticia.find('span',class_='dateTime') != None:
		result.append(noticia.find('span',class_='dateTime').get_text().strip().encode('utf-8'))

	if noticia.find('h2') != None:
		result.append(noticia.find('h2').get_text().strip().encode('utf-8'))
		
	if noticia.find('span',class_='lead') != None:
		result.append(noticia.find('span',class_='lead').get_text().strip().encode('utf-8'))
	
	if noticia.find('h2') != None:
		h = noticia.find('h2')
		link =h.find('a')['href']
		result.append("https://www.cmjornal.pt"+ link.strip().encode('utf-8'))

	i = news.find('figure')

	if i == None:
		result.append("cm.png")
	else:
		result.append("http:" + i.find('img')['data-src'].strip().encode('utf-8'))

	with open(file,'a') as fp:
		fp.write(';'.join(result))
		fp.write('\n')
	fp.close()

page = requests.get('https://www.cmjornal.pt/cm-ao-minuto?ref=geral_MenuHeader')

soup = BeautifulSoup(page.text, 'html.parser')

main_group = soup.find(class_='aominutoMain')

news_group = main_group.find_all('article')

file = "cmjornal.csv"

if os.path.exists(file):
	os.remove(file)

for news in news_group:
	if news != None:
		get_data(news)


