# Bitly URL shortener

The program allows you to reduce the length of the link to send over the network, 
when you enter a short link, the program will show the number of clicks on this link.

The program works with api interface is written in python and contains constants [token].

Also functions shorten_link to shorten a link, count_clicks to count the number of clicks on a given link 
and is_bitlink to determine the type of link.

## How to install


To get the token you need to register at (https://app.bitly.com)
Then go to the settings/api (https://app.bitly.com/settings/api/) and generate a token using your password,
and enter the received token into the program in the token field.
Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
Enter your token:

```
token = "****************************************"
```

Run the program and enter your link - the program will give you bitlink. If you enter a bitlink, 
the program will show you the number of clicks on it.




