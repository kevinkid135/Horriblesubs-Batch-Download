import time #used to pause script
import os #library used to open magnet link
from selenium import webdriver #use selenium

#global variables
driverLocation = "C:/Users/Kevin/Downloads/Browsers/chromedriver.exe"
url = "http://horriblesubs.info/shows/shigatsu-wa-kimi-no-uso/"
quality = "1080p"
download_format = "Magnet"

browser = webdriver.Chrome(driverLocation)
browser.get(url)
#time.sleep(1) # Let the user actually see something!

links = browser.find_elements_by_link_text(quality)
length = len(links)
print (str(length) + " episodes found")
counter = 1
for link in links:
    print("Clicking '{}': {}/{}".format(quality, counter, length))
    link.click()
    counter+=1
    time.sleep(0.1) #delay of animation
    #break # temp

print

links = browser.find_elements_by_link_text(download_format)
counter = 1
for link in links:
    print("Clicking '{}': {}/{}".format(download_format, counter, length))
    os.startfile(link.get_attribute("href"))
    counter+=1
    time.sleep(0.1) #not too fast...
    #break # temporary, only do first iteration

#time.sleep(5) # Let the user actually see something!
browser.quit()
