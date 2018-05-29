import requests
from bs4 import BeautifulSoup
r = requests.get('https://book.douban.com/subject/1084336/comments/')
soup =BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
  print(item.string)
