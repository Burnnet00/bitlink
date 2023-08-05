import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


def shorten_link(token, url):
    payload = {
        "domain": "bit.ly",
        "long_url": url,
    }

    headers = {
        "Authorization": f"Bearer {token}",
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
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    print("our link has been followed", clicks_count, "times")
    return clicks_count


# def is_bitlink(url):
#     parsed = urlparse(url)
#     hostname = parsed.netloc
#     path_host = f"{parsed.netloc}{parsed.path}"
#     if hostname == "bit.ly":
#         count_clicks(token, path_host)
#     else:
#         shorten_link(token, url)


def is_bitlink(url):
    split_url = split_domain_path(url)
    print(split_url)
    headers = {
        "Authorization": f"Bearer {token}",
    }
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{split_url}"
    response = requests.get(endpoint, headers=headers)
    print(response.status_code)

# https://python-scripts.com/json
# https://bit.ly/3QkQvwd

def split_domain_path(url):
    parsed = urlparse(url)
    domain_path = f"{parsed.netloc}{parsed.path}"
    return domain_path

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    print("Enter your link: ")
    try:
        user_link = input()
        is_bitlink(user_link)

    except requests.exceptions.HTTPError:
        print("Bad link")
