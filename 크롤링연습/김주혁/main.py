from bs4 import BeautifulSoup
from test import *
import requests

def get_form_list(url):
    req = requests.get(url)
     
    if req.ok:
        html = req.text
        soup = BeautifulSoup(html,'html.parser')

    from_list = [];
    # <from> </form> tag find_all
    for form_tag in soup.find_all('form'):
        # <input> </input> tag find_all
        input_list = [];
        for input_tag in form_tag.find_all('input'):
            # <input type='submit' and disabled='disabled' continue'></input>
            if (input_tag.get('type') == 'submit') or (input_tag.get('disabled') == 'disabled'):
                continue;
            input_list.append([input_tag.get('name'), input_tag.get('value')]);

        form_method = form_tag.get('method');
        form_method == None and 'get' or form_method;
        from_list.append(Form(form_tag.get('action'), form_method, dict(input_list)));
        
    return from_list;


if __name__=="__main__":
    # url = input("url: ");

    # Test url:
    # http://namucoffee.com/
    # https://sir.kr/
    url = 'http://namucoffee.com/'
    form_list = get_form_list(url);

    for form in form_list:
        print(form.action);
        print(form.method);
        print(form.parameter);
