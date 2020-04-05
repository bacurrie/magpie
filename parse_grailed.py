from bs4 import BeautifulSoup

soup = BeautifulSoup(open('out.txt', 'r', encoding='utf-8'), 'lxml')

# NEED attributes:
# name
    # <div class="listing-metadata"> --> <p class="truncate listing-title">
# brand
    # <div class="listing-metadata"> --> <>
# size
# old price
# new price
# date posted
# date bumped
# (later) origin site

#TODO sizing guide for subscribers?

for tag in soup.find_all("div", {"class": "feed-item"}):
    print('==========')
    title = tag.find('p', {"class": "truncate listing-title"})
    designer = tag.find('p', {'class': 'listing-designer truncate'})
    size = tag.find('p', {'class': 'listing-size sub-title'})
    ogPrice = tag.find('p', {'class': 'sub-title original-price'})
    oldPrice = tag.find('p', {'class': 'sub-title original-price strike-through'})
    newPrice = tag.find('p', {'class': 'sub-title new-price'})
    bump = tag.find('span', {'class': 'date-ago'})
    origin = tag.find('span', {'class': 'bumped date-ago'})
    
    print(title.string)
    print(designer.string)
    print(size.string)

    if ogPrice == None:
        print("was: " + oldPrice.string)
        print("now: " + newPrice.string)
    else:
        print(ogPrice.string)
    if origin == None:
        print("posted " + bump.string)
    else:
        print("bumped " + bump.string)
        print("listed " + origin.string)