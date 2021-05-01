from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

# using html.parser
bs_parser = BeautifulSoup(html.read(), 'html.parser')
print(bs_parser.h1)

# using lxml
# good at 'dirty' html, little bit faster than parser
bs_lxml = BeautifulSoup(html.read(), 'lxml')

# using html5lib
# can fix many kind of errors than lxml
# slower than lxml, parser
bs_h5lib = BeautifulSoup(html.read(), 'html5lib')

