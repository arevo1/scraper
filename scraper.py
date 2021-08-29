from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from plyer import notification
import time

header = {"User-Agent":"Mozilla"}
req = Request("https://www.worldometers.info/coronavirus/country/us/", headers = header)
html = urlopen(req)

obj = bs(html,'html.parser')
new_cases = obj.find("li", {"class":"news_li"}).strong.text.split()[0]
new_deaths = list(obj.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

while True:
   notification.notify(title="COVID-19 Update"
                      ,message="new Cases - " + new_cases +"\nnew Deaths - "+ new_deaths)
   time.sleep(20)


