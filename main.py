import requests
token = "Bearer a649aa3e3ce528d1d3f42b594cbff90731a0d0ba"

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

    url = 'https://api-ssl.bitly.com/v4/shorten'
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['link']
    return bitlink

print('Enter your link: ')
try:
    user_link = input()
    url = user_link
    bitlink = shorten_link(token, url)
    print('Битлинк -', bitlink)
except requests.exceptions.HTTPError:
    print('Bad link')
'''https://bit.ly/3KMO1TV - bit.ly/3KMO1TV'''

def count_clicks(token, link):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {
        "Authorization": token,
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    clicks_count = response.text#need take 3 key
    return clicks_count
print('Enter short link')
user_short_link = input()
link = user_short_link
link_count = count_clicks(token,link )
print('our link has been followed', link_count)




# bitlink = url.format("bit.ly/43Sloer")
# params = {"unit": "day", }



# your link has been followed four times
# # if __name__ == '__main__':
# #     main()