from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class' : 'green'})
# findAll을 이용하면 첫 번째 태그뿐만 아니라 페이지의 태그 전체를 찾아 태그 리스트로 만든다
# <span class="green"></span> 태그가 들어있는 텍스만 선택해서 고유명사로 이루어진 파이썬 리스트를 추출
# print(nameList)
# nameList에는 태그가 붙어있는 채로 들어간다.

# for name in nameList:
#     print(name.get_text())
#     # get_text()를 사용하면 갖종 태그를 제거하고 내용물만 볼 수 있다.

head_tag = bs.findAll({'h1', 'h2', 'h3', 'h4', 'h5', 'h6'})
span_color_tag = bs.findAll('span', {'class': {'green', 'red'}})
# 문서의 모든 헤더 태그 태그 레스트를 반환
# 속성을 목록처럼 넘기면(파이썬 딕셔너리) 그 중 하나에 일치하는 태그를 찾아 모두 반환 ==> or 처럼 처리

print(len(bs.findAll(text = 'the prince')))
# 태그에 둘러싸인 'the prince'와 일치하는 갯수

# .finaAll()에 keyword를 사용하면 매개변수는 and로 처리