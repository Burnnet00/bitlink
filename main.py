import json
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


load_dotenv()
token = os.environ['TOKEN']


def shorten_link(token, url):
    payload = {
        "group_guid": "Bn82bpRqty3",
        "domain": "bit.ly",
        "long_url": url,
    }

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink


print("Enter your link: ")
try:
    user_link = input()
    url = user_link
    bitlink = shorten_link(token, url)
    print("Битлинк -", bitlink)
except requests.exceptions.HTTPError:
    print("Bad link")


def count_clicks(token, link):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    headers = {
        "Authorization": token,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.text
    return clicks_count


print("Enter short link: ")
try:
    user_short_link = input()
    parsed = urlparse(user_short_link)
    link = parsed.netloc + parsed.path
    link_count = count_clicks(token, link)
    dict_count = json.loads(link_count)["total_clicks"]
    print("our link has been followed", dict_count, "times")
except requests.exceptions.HTTPError:
    print("Bad link")

def is_bitlink(url):
    url = f"https: // api - ssl.bitly.com / v4 / bitlinks / {url}"
    return


# if __name__ == '__main__':
#     main()
