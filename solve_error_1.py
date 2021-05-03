from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
        # title은 html.parser로 연 url에서 <body><h1></h1></body> 내용을 담고있음 

        title_without_tag = str(title)[4:-5]
        # 앞뒤로 <h1>과 </h1>을 자른 변수 
        
    except AttributeError as e:
        return None
    return title

title = getTitle('https://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)