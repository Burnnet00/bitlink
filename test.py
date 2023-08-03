import json
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ['TOKEN']

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
a = "bitly.is/44UfyKP"
count_clicks(token, a)

# def is_bitlink(url, token):
#     url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
#     headers = {
#         "Authorization": token,
#     }
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     print(response.text)
# a = 'bitly.is/44UfyKP'
#
# is_bitlink(a, token)



# {"created_at":"2023-08-03T11:42:37+0000","id":"bit.ly/3KuFXqv","link":"https://bit.ly/3KuFXqv","custom_bitlinks":[],"long_url":"https://pymotw.com/3/urllib.parse/index.html","title":"urllib.parse — Split URLs into Components — PyMOTW 3","archived":false,"created_by":"burnnet","client_id":"a5e8cebb233c5d07e5c553e917dffb92fec5264d","tags":[],"deeplinks":[],"references":{"group":"https://api-ssl.bitly.com/v4/groups/Bn82bpRqty3"}}

# https://pymotw.com/3/urllib.parse/index.html
# https://bit.ly/3KuFXqv







#
# load_dotenv()
# token = os.environ['TOKEN']
#
#
# def shorten_link(token, url):
#     payload = {
#         # "group_guid": "Bn82bpRqty3",
#         "domain": "bit.ly",
#         "long_url": url,
#     }
#
#     headers = {
#         "Authorization": token
#     }
#
#     url = "https://api-ssl.bitly.com/v4/shorten"
#     response = requests.post(url, json=payload, headers=headers)
#     response.raise_for_status()
#     bitlink = response.json()['link']
#     return bitlink
#
#
# print("Enter your link: ")
#
# user_link = input()
# url = user_link
# bitlink = shorten_link(token, url)
# print("Битлинк -", bitlink)












# pip freeze > requirements.txt