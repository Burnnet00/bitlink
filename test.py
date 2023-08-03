from urllib.parse import urlparse

url = 'https://bit.ly/3KuFXqv'
parsed = urlparse(url)
print(parsed.netloc+parsed.path)