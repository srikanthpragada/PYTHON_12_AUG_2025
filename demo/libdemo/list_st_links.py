import requests
from bs4 import BeautifulSoup

website = "https://www.w3schools.com"
resp = requests.get(website)

if resp.status_code != 200:
    print('Sorry! Could not get details')
    exit(1)


soup = BeautifulSoup(resp.text, 'html.parser')
links = soup.find_all("a")

hrefs = []
for link in links:
    href = link['href']
    if href.startswith('javascript'):
        continue

    if not href.startswith('http'):
        href = website + href

    if href not in hrefs:
        hrefs.append(href)

for href in hrefs:
    print(href)

print('Link Count :', len(hrefs))


