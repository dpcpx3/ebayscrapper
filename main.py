import requests
from bs4 import BeautifulSoup

search_url = "https://www.ebay-kleinanzeigen.de/s-zu-verschenken/{}".format("+".join(search_term.split()))
response = requests.get(search_url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the listings on the page
listings = soup.find_all("li", class_="ad-listitem")

# Print out the title and price of each listing
for listing in listings:
    title = listing.find("a", class_="ellipsis").get_text().strip()
    price = listing.find("div", class_="aditem-main--middle--price").get_text().strip()
    print("Title: {}\nPrice: {}\n".format(title, price))
