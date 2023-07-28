from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPDigestAuth

URL = "https://tds.ms/CentralizeSP/BtwScheduling/Lessons?SchedulingTypeId=1"
page = requests.get(URL, auth=HTTPDigestAuth('user', 'pass'))
#page = requests.get(URL, auth=('user', 'pass'))
#page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="divAvailabilityCalenderShow")
open_slots = results.find_all("div", class_=" ui-state-available")
for open_slot in open_slots:
    print(open_slot, end="\n"*2)

#print(results.prettify())
#print(results)
print(page.text)
