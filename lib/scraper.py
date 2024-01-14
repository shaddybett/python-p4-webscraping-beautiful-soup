from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://Moringaschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

print(doc.select('.heading-60-black.color-black.mb-20'))



courses = doc.select('.heading-60-black.color-black.mb-20')[0]
name = doc.select('.heading-60-black.color-black.mb-20')[0].name
doc.select('.heading-60-black.color-black.mb-20')[0].attrs