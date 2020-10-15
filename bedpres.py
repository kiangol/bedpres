from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime
from private import pushUrl

# URL for the event
url = "https://ifinavet.no/event/"
eventId = str(input("Enter event id (3 digits): "))
url += eventId
rate = input("Refresh rate in seconds: ")

# Variables
sendNotification = True
loop = True
if rate:
    rate = int(rate)
else:
    rate = 30
refresh_rate = rate # check every x seconds

# Use Pushcut app for notifications
# Modify URL to own notification URL 
# pushUrl = "https://api.pushcut.io/*****/notifications/******"

try:
    urlopen(pushUrl)
except:
    print("An exception occured with Pushcut service")


# Get initial value
try:
    html = urlopen(url)
except urllib.error.HTTPError as e:
    print(url)
    print(e)
    exit()

bsObj = BeautifulSoup(html)
reqContainer = bsObj.find("div", {"class": "event-infobox"})

contents = reqContainer.contents
availBox = contents[len(contents)-2]
initial = availBox.find("p").contents

# Store initial value in this list
valuesToCompare = []

lastElement = initial[-1]
# Add elements from result to comparision list
print(" ----- INITIAL -----")
for i in initial:
    if (type(lastElement) == type(i)):
        valuesToCompare.append(i)
print(valuesToCompare)


print(" ----- BEGIN -----")
while loop:
    freshValues = []
    try:
        html = urlopen(url)
        bsObj = BeautifulSoup(html)
        reqContainer = bsObj.find("div", {"class": "event-infobox"})

        contents = reqContainer.contents
        availBox = contents[len(contents)-2]

        curr = availBox.find("p").contents
    except :
        print("Error occured. Will try again next loop")
        continue
        
    for i in curr:
        if(type(lastElement) == type(i)):
            freshValues.append(i)

    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")   
    time_string = now.strftime("%H:%M:%S")
    if(freshValues == valuesToCompare):
        print("Checked:", dt_string)
    else:
        print("Available spot found! {}".format(time_string))
        if sendNotification:
            print("Sending notification ...")
            urlopen(pushUrl)
        sleep(1)
        break

    sleep(refresh_rate)

print("Done!")
