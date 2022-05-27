from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("C:/Users/Ritika Sharma/Desktop/Module3/C127/C127/chromedriver.exe")
time.sleep(1)
browser.get(start_url)
headers = ["name","distance", "mass", "radius"]
starData = []
def webScrape():
    
    soup = BeautifulSoup(browser.page_source,"html.parser")
    temp_list = []
    for trtags in soup.find_all("tr"):
        tdTags = trtags.find_all("td")
        for index,tdtag in enumerate(tdTags):
            try:
                if(index == 0):
                    temp_list.append(tdtag.find_all("a")[0].contents[0])
                else:
                    temp_list.append(tdtag.contents[0])
            except:
                temp_list.append("")
        starData.append(temp_list)
    with open("stars.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(starData)
webScrape()
