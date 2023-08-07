import requests

t = "a639760e9b3a55ad3e92cef31ec5fd6ad7dc1b5a"
u = "https://python-scripts.com/json"

def shorten_link(token, url):
    payload = {
        "long_url": url,
    }

    headers = {
        "Authorization": f"Bearer {token}",
    }

    url = "https://api-ssl.bitly.com/v4/shorten"
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['link']
    print(bitlink)
    return bitlink

shorten_link(t,u)