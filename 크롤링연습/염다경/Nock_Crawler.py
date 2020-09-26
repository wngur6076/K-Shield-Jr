import requests
from bs4 import BeautifulSoup

loing_url = 'http://namucoffee.com/.' #로그인 처리 페이지 주소 입력
craw_url = 'http://namucoffee.com/' #마일리지값이 있는 페이지 주소 입력

session = requests.session()

p = dict()
p['my_id'] = 'admin' #ID입력
p['my_pw'] = 'password' #PW입력
#p 변수에 계정정보 할당.

res = session.post(login_url, data = p)
res.rase_for_status()

print(res.headers)
print(session.cookies.get_dict())
#헤더와 쿠키로 넘어가는 값 출력

res = session.get(craw_url)
soup = BeautifulSoup(res.content, 'html.p')
data = soup.select('a');

for item in data:
    print(item['href'])
