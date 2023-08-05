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
    split_link = split_domain_path(link)
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{split_link}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    print("Our link has been followed", clicks_count, "times")
    return clicks_count


def is_bitlink(url):
    split_url = split_domain_path(url)
    headers = {
        "Authorization": f"Bearer {token}",
    }
    endpoint = f"https://api-ssl.bitly.com/v4/bitlinks/{split_url}"
    response = requests.get(endpoint, headers=headers)
    status_code = response.status_code
    return status_code


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
        check_url = is_bitlink(user_link)
        if check_url == 200:
            count_clicks(token, user_link)
        else:
            shorten_link(token, user_link)



    except requests.exceptions.HTTPError:
        print("Bad link")
