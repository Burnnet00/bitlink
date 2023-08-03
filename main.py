import json
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


load_dotenv()
token = os.environ['TOKEN']


def shorten_link(token, url):
    payload = {
        # "group_guid": "Bn82bpRqty3",
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
    print("Битлинк -", bitlink)
    return bitlink

def count_clicks(token, link):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    headers = {
        "Authorization": token,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.text
    dict_count = json.loads(clicks_count)["total_clicks"]
    print("our link has been followed", dict_count, "times")
    return clicks_count

def is_bitlink(url):
    parsed = urlparse(url)
    hostname = parsed.netloc
    path_host = parsed.netloc + parsed.path
    if hostname == "bit.ly":
        count_clicks(token,path_host)
    else:
        shorten_link(token, url)

print("Enter your link: ")
try:
    user_link = input()
    is_bitlink(user_link)

except requests.exceptions.HTTPError:
    print("Bad link")

# print("Enter link: ")
# user_link = input()
# is_bitlink(user_link)

# https://dev.bitly.com/docs/tutorials/shorten-customize-links/
# https://bitly.is/44UfyKP



# if __name__ == '__main__':
#     main()
