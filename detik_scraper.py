import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')
popular_area = soup.find(attrs={'class': 'grid-row list-content'})

print('\n"Mengambil data "Judul" pada class "media__title" dan dicetak berupa list/array"')
titles = popular_area.findAll(attrs={'class': 'media__title'})
for tt in titles:
    print(tt.text)

print('\n"Mengambil data judul pada class media__image dan dicetak beruapa array"')
print('')
images = popular_area.findAll(attrs={'class': 'media__image'})
for image in images:
    print(image.find('a').find('img')['title'])

#print(images)

