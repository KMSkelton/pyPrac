import requests
from bs4 import BeautifulSoup

# url = "https://wiki.python.org/moin/IntroductoryBooks"

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"

response = requests.get(url)
dir(response)

print(response.headers)
content = response.content
soup = BeautifulSoup(content, "lxml")
#print(soup.prettify())

all_a = soup.find_all("li", {"class": "gallerybox"})

craters = {}
for initial in all_a:
    crater_info = initial.find("div", "gallerytext")
    link = crater_info.find("a")
    name = link.string
    craters[name] = link
print(craters)

with open('crater_scrape.csv', "w") as outfile:
    for name, link in craters.items():
        outfile.writelines(f"{name}:{link}")
        outfile.write(',')