from bs4 import BeautifulSoup

f = open('out.txt', 'w', encoding='utf-8')
soup = BeautifulSoup(f, 'lxml')

#NEED attributes:
#name
#brand
#size
#old price
#new price
#date posted
#date bumped


for tag in soup.find_all("div", {"class": "feed-item"}):
