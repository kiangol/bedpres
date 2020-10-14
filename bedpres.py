from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

# URL for the event
url = "https://ifinavet.no/event/327"

# Use Pushcut app for notifications
pushUrl = "https://api.pushcut.io/g6V-0NfXxpldSJqfvMgTK/notifications/Bedpres"

# Get initial value
html = urlopen(url)
bsObj = BeautifulSoup(html, features="lxml")
reqContainer = bsObj.find("div", {"class": "event-infobox"})

contents = reqContainer.contents
availBox = contents[len(contents)-2]
initial = availBox.find("p").contents

# Store initial value in this list
valuesToCompare = []

# Used to check for type
lastElement = initial[-1]

print(" ----- INITIAL -----")
for i in initial:
    if (type(lastElement) == type(i)):
        valuesToCompare.append(i)
print(valuesToCompare)

loop = True

print(" ----- BEGIN -----")
while loop:
    freshValues = []
    html = urlopen(url)
    bsObj = BeautifulSoup(html, features="lxml")
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

    if(freshValues == valuesToCompare):
        print("Checked:", dt_string)
    else:
        print("Available spot found!")
        print("Sending notification ...")
        urlopen(pushUrl)
        sleep(1)
        break

    sleep(5)

print("Done!")
