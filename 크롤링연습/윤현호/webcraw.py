from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import sys

def urlopen(url):
    global soup
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

def login():
    global soup
    ld = soup.find('input', attrs={'type': 'text'})
    pw = soup.find('input', attrs={'type': 'password'})
    print("[*]Login parameter")
    print(str(ld).split("name")[-1].split("\"")[1])
    print(str(pw).split("name")[-1].split("\"")[1])

def href():
    global soup
    href = soup.find_all('a')
    print("[*]href list")
    for list in href:
        href_list = str(list).split("href")[-1].split("\"")[1]
        print(href_list)

if __name__=="__main__":
    print("[*]plz Input url")
    url = input()
    urlopen(url)
    login()
    href()
