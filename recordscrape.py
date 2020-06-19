import requests
from bs4 import BeautifulSoup
import re
import os
import json


def get_data(noticia):
	result = []

	if noticia.find('h4',class_='seccao') != None:
		result.append(noticia.find('h4',class_='seccao').get_text().strip().encode('utf-8'))

	if noticia.find('h1') != None:
		result.append(noticia.find('h1').get_text().strip().encode('utf-8'))

	if noticia.find('p') != None:
		result.append(noticia.find('p').get_text().strip().encode('utf-8'))
	
	if noticia.find('figure') != None:
		imagem = noticia.find('figure')
		result.append("http:" + imagem.find('img')['data-src'].encode('utf-8'))

	if noticia.find('a') != None:
		link ="https://www.record.pt"+ noticia.find('a')['href']
		result.append(link.strip().encode('utf-8'))

	with open(file,'a') as fp:
		fp.write(';'.join(result))
		fp.write('\n')
	fp.close()


def get_Destaque(noticia):
	result = []

	if noticia.find('h4',class_='seccao') != None:
		result.append(noticia.find('h4',class_='seccao').get_text().strip().encode('utf-8'))

	if noticia.find('h1') != None:
		result.append(noticia.find('h1').get_text().strip().encode('utf-8'))

	if noticia.find('h2') != None:
		result.append(noticia.find('h2').get_text().strip().encode('utf-8'))
	
	if noticia.find('figure') != None:
		imagem = noticia.find('figure')
		result.append("http:" + imagem.find('img')['src'].encode('utf-8'))

	if noticia.find('a') != None:
		link ="https://www.record.pt"+ noticia.find('a')['href']
		result.append(link.strip().encode('utf-8'))

	with open(file,'a') as fp:
		fp.write(';'.join(result))
		fp.write('\n')
	fp.close()
 
page = requests.get('https://www.record.pt/ultimas-noticias')

soup = BeautifulSoup(page.text, 'html.parser')

destaque = soup.find('article', class_="canalDestaque")

articles = soup.find_all('article',class_='col-12 destaques showPicture destaques')

file = "record.csv"

if os.path.exists(file):
	os.remove(file)

if destaque != None:
	get_Destaque(destaque)

for article in articles:
	if article != None:
		get_data(article)



