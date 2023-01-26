from bs4 import BeautifulSoup
import requests

url = 'https://vk.com/dorliongarage'
page = requests.get(url)
print(page.status_code)

filteredNews = []
allNews = []



soup = BeautifulSoup(page.text, "html.parser")
# print(soup)
allNews = soup.findAll('div', class_='pi_text')
print(allNews)
for data in allNews:
    if data.find('span', class_='time2 time3') is not None:
        filteredNews.append(data.text)