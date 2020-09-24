from bs4 import BeautifulSoup
import requests


# url = input("url: ");

# Test url:
# http://namucoffee.com/
# https://sir.kr/
url = 'http://namucoffee.com/'
req = requests.get(url)
 
if req.ok:
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

# <from> </form> tag find_all
for form__tag in soup.find_all('form'):
    # <form action='출력' method='출력'></form>
    print(form__tag.get('action').replace(url, ''));

    form__method = form__tag.get('method');
    # <form method='출력'> method 선택자를 지정하지 않으면 기본값 get임.
    print(form__method == None and 'get' or form__method);
    
    # <input> </input> tag find_all
    for input__tag in form__tag.find_all('input'):
        # <input type='text, password 아니면 continue'></form>
        if (input__tag.get('type') != 'text') and (input__tag.get('type') != 'password'):
            continue;
        # <input name='출력' title='출력' placeholder='출력'></form>
        print(input__tag.get('name'),
              input__tag.get('title'),
              input__tag.get('placeholder'));
        
    print('------------------------------------------------------------------------------');
