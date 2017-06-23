import time #used to pause script
import os #library used to open magnet link
from selenium import webdriver #use selenium

#global variables (CHANGE THESE)
driverLocation = "" #Location of your chrome driver
url = "http://horriblesubs.info/shows/shigatsu-wa-kimi-no-uso/" # link to your desired anime
quality = "1080p" # the quality that you want to download
download_format = "Magnet" # format you want to download
# end global variables

# open the chrome driver
browser = webdriver.Chrome(driverLocation)
browser.get(url)
#time.sleep(1) # Let the user actually see something!

# find the episode elements and click the quality, then download format.
# This will loop through all episodes
links = browser.find_elements_by_link_text(quality)
length = len(links)
print (str(length) + " episodes found")
counter = 1
for link in links:
    print("Clicking '{}': {}/{}".format(quality, counter, length))
    link.click()
    counter+=1
    time.sleep(0.1) # delay of animation. Can be changed if animation takes longer or different systems

print # newline

links = browser.find_elements_by_link_text(download_format)
counter = 1
for link in links:
    print("Clicking '{}': {}/{}".format(download_format, counter, length))
    os.startfile(link.get_attribute("href"))
    counter+=1
    time.sleep(0.1) # allows some time for the next action to be done.

#time.sleep(5) # Let the user actually see something!
browser.quit()
