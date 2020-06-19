import requests
from bs4 import BeautifulSoup
import re
import os
import json


def get_data(noticia):
	result = []

	if noticia.find('span',class_='hora') != None:
		result.append(str(noticia.find('span',class_='hora').get_text().strip().encode('utf-8')))

	if noticia.find('span',class_='tema') != None:
		result.append(str(noticia.find('span',class_='tema').get_text().strip().encode('utf-8')))

	if noticia.find('h4') != None:
		result.append(str(noticia.find('h4').get_text().strip().encode('utf-8')))

	if noticia.find('div',class_='media-texto hidden-xs') != None:
		result.append(str(noticia.find('div',class_='media-texto hidden-xs').get_text().strip().encode('utf-8')))

	if noticia.find(class_='media-img') != None:
		imagem = noticia.find(class_='media-img')
		url = str(imagem['style'])
		url = url.split("('", 1)[1].split("')")[0]
		sr = "https:"
		if sr in url:
			pass
		else:
			url = sr+url
		result.append(str(url.replace(' ',"").encode('utf-8')))

	if noticia.find('a') != None:
		result.append(str("https://www.abola.pt"+ noticia.find('a')['href']))

	with open(file,'a') as fp:
		fp.write(';'.join(result))
		fp.write('\n')
	fp.close()

page = requests.get('https://www.abola.pt/Nnh/Noticias')

soup = BeautifulSoup(page.text, 'html.parser')

news_group = soup.find_all(class_='mt-15')

file = "abola.csv"

if os.path.exists(file):
	os.remove(file)

for news in news_group:
	if news != None:
		get_data(news)




