import requests
from bs4 import BeautifulSoup

def get_tiobe_top10():
    url = "https://www.tiobe.com/tiobe-index/"
    resp = requests.get(url)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find the table or section containing the top rankings
    # From inspection, the top 10 are in a table with class "table-top20" (or similar)
    table = soup.find("table", attrs={"id": "top20"})
    if not table:
        raise RuntimeError("Could not find TIOBE top 20 table on page")

    top10 = []
    for row in table.tbody.find_all("tr")[:10]:
        cols = row.find_all("td")
        # Pos, Last Year Pos, Change, icon,  Lang, Rating
        lang = cols[4].text
        rating = cols[5].text
        top10.append((lang, rating))

    return top10

top10 = get_tiobe_top10()
for lang, rating in top10:
   print(f"{lang:30}  {float(rating.strip('%')):5.2f}")
