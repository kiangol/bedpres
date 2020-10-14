from urllib.request import urlopen
import urllib.error
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

# URL for the event
url = "https://ifinavet.no/event/325"

# Variables
sendNotification = True
loop = True
refresh_rate = 30 # check every x seconds

# Use Pushcut app for notifications
pushUrl = "https://api.pushcut.io/g6V-0NfXxpldSJqfvMgTK/notifications/Bedpres"
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

# Used to check for type (add string only)
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
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    reqContainer = bsObj.find("div", {"class": "event-infobox"})

    contents = reqContainer.contents
    availBox = contents[len(contents)-2]

    curr = availBox.find("p").contents
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
