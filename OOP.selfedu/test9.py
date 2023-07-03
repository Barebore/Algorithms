import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.content

def count_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_tags = soup.find_all()
    total_tags = len(all_tags)
    return total_tags

def count_tags_with_attrs(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_tags = soup.find_all()
    tags_with_attrs = 0
    for tag in all_tags:
        if tag.attrs:
            tags_with_attrs += 1
    return tags_with_attrs

if __name__ == '__main__':
    url = 'https://jetlend.ru'
    html = get_html(url)
    total_tags = count_tags(html)
    tags_with_attrs = count_tags_with_attrs(html)
    print(f'Количество HTML тегов на странице: {total_tags}')
    print(f'Количество HTML тегов с атрибутами на странице: {tags_with_attrs}')