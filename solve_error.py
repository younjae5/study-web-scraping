from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bs_parser = BeautifulSoup(html.read(), 'html.parser')
print(bs_parser.h1)
# print(bs_parser.nonExistentTag)
# print(bs_parser.nonExistentTag.someTag)
# AttributeError: 'NoneType' --> someTag

try:
    #html = urlopen("https://pythonscraping.com/pages/error.html")
    #html = urlopen("https://pythonscrapingthisurldoesnotexit.com")
    badContent = bs_parser.nonExistentTag.anotherTag
except HTTPError as e: # "404", "500"...
    print(e)
    # return null/ use break/ other things..
except URLError as e: # if can't find the url or page
    print('The server could not be found!')
except AttributeError as e:
    print("Tag was not found")
else:
    # run this program until break it
    # if you use return or break in "except"
    # you don't need this "else"
    # print('It worked!')

    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)