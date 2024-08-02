import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/2024_Summer_Olympics#Medal_table"
page = requests.get(url)

doc = BeautifulSoup(page.text, "html.parser")

olympics_medal_table = doc.find(class_="wikitable sortable notheme plainrowheaders jquery-tablesorter")

south_korea_in_medal_table = olympics_medal_table.find_all(string="South Korea")
medals = south_korea_in_medal_table[0].parent.parent.parent

#finding the tags where the medal # are, and then turning them into strings

medals_and_rank_in_text = medals.find_all("td")
korea_rank = medals_and_rank_in_text[0].string
korea_gold = medals_and_rank_in_text[1].string
korea_silver = medals_and_rank_in_text[2].string
korea_bronze = medals_and_rank_in_text[3].string
korea_total_medals = medals_and_rank_in_text[4].string


#user input
question = input("Type Gold, Silver, Bronze, or Total to see how many medals South Korea has in each category ")


if question == "Gold" or question == "gold":
    print("Gold Medals: " + korea_gold)
if question == "Silver" or question == "silver":
    print("Silver Medals: " + korea_silver)
if question == "Bronze" or question == "bronze":
    print("Bronze Medals: " + korea_bronze)
if question == "Total" or question == "total":
    print("Total Medals: " + korea_total_medals)

print("Korea is ranked " + korea_rank + "th")