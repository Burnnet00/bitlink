import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ['TOKEN']

def is_bitlink(url, token):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {
        "Authorization": token,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.text)
a = 'bit.ly/3KuFXqv'

is_bitlink(a, token)



# {"created_at":"2023-08-03T11:42:37+0000","id":"bit.ly/3KuFXqv","link":"https://bit.ly/3KuFXqv","custom_bitlinks":[],"long_url":"https://pymotw.com/3/urllib.parse/index.html","title":"urllib.parse — Split URLs into Components — PyMOTW 3","archived":false,"created_by":"burnnet","client_id":"a5e8cebb233c5d07e5c553e917dffb92fec5264d","tags":[],"deeplinks":[],"references":{"group":"https://api-ssl.bitly.com/v4/groups/Bn82bpRqty3"}}

# https://pymotw.com/3/urllib.parse/index.html
# https://bit.ly/3KuFXqv


# from urllib.parse import urlparse
#
# url = 'https://bit.ly/3KuFXqv'
# parsed = urlparse(url)
# print(parsed.netloc+parsed.path)