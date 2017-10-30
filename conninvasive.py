from bs4 import BeautifulSoup
import requests, re, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url ="https://plants.usda.gov/java/noxious?rptType=State&statefips=09"
noxious = requests.get(url, verify = False)
if noxious.status_code != 200:
    print('error', url)

page_html = noxious.text
soup = BeautifulSoup(page_html, "html.parser")

td_articles = soup.find_all("tr", attrs ={"class": "rowon"})
#the below code gives me everything within ghe first <td> tag
#data = ]
#for an_article in td_articles:
    #state = an_article.find('td')
    #state_text = state.text

            #print("---------")


            #print(state.text)
#now I am going to try to turn this into a list so that I can capture diferent td elements
td_list = td_articles.find("td")
  # Python starts counting list items from 0, not 1
print(td_list[0].text)
print(td_list[3].text)
