from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

bs_parser = BeautifulSoup(html.read(), 'html.parser')
print(bs_parser.h1)

try:
    #html = urlopen("https://pythonscraping.com/pages/error.html")
    html = urlopen("https://pythonscrapingthisurldoesnotexit.com")
except HTTPError as e: # "404", "500"...
    print(e)
    # return null/ use break/ other things..
except URLError as e: # if can't find the url or page
    print('The server could not be found!')
else:
    # run this program until break it
    # if you use return or break in "except"
    # you don't need this "else"
    print('It worked!')