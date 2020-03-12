import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
import sys, argparse, time

#TODO parsing scheme for grailed listings
#TODO develop universal JSON format

parser = argparse.ArgumentParser("Process list")
parser.add_argument('-l', '--list', nargs='+', type=str, help='<Required> set flag', required=True)
args = parser.parse_args()
driver = webdriver.Firefox()
f = open('out.txt','w')
def chewFeed(name):
    url = "https://www.grailed.com/designers/"+name
    driver.get(url)
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    #TODO see if can get count of flex items in div, scroll until all are visible...
        #compare to total num of listings in designer cat.
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    feed = driver.find_element_by_xpath(".//*[@class='feed']")
    #source = feed.get_attribute("outerHTML")
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')
    f.write(source)

designerLst = args.list
designerLst = [name.replace(" ", "-").lower().split(",") for name in designerLst]
designerLst = designerLst[0] #list is within a list, so have to extract it like this
print(designerLst)
for designer in designerLst:
    chewFeed(designer)
    