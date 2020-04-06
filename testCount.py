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

def chewFeed(name):
    url = "https://www.grailed.com/designers/"+name
    driver.get(url)
    SCROLL_PAUSE_TIME = 1

    count = driver.find_element_by_xpath(".//*[@class='ais-Panel-body']").text
    count_value = count.split()
    count_int = int(count_value[0])
    print(count_int)
    feedCount = 0
    while feedCount != count_int:
            
        feed = driver.find_element_by_xpath(".//*[@class='feed']")
        feedCount = len(driver.find_elements_by_xpath(".//*[@class='feed']/div"))
        print(feedCount)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

designerLst = args.list
designerLst = [name.replace(" ", "-").lower().split(",") for name in designerLst]
designerLst = designerLst[0] #list is within a list, so have to extract it like this
print(designerLst)
for designer in designerLst:
    chewFeed(designer)
driver.quit()
    