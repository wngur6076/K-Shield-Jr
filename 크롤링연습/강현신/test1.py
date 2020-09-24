from bs4 import BeautifulSoup as bs
import requests , json

URL = "sir.kr"
# URL = "www.wikipedia.org"
# URL = "www.naver.com"
# URL = "www.daum.net"



with requests.Session() as s:
    req = s.post("https://"+URL)

    hd = req.headers
    # print ("server info : "+hd['Server']+" | "+hd['X-Powered-By'])
    
    soup = bs(req.text,'html.parser')
    linklist = []
    reslist = []
    for link in soup.findAll("a") :
        if 'href' in link.attrs:
            tmp = link.attrs['href']
            if tmp in linklist :
                pass
            else :
                tmp = tmp.split(URL)
                if len(tmp) == 2 :
                    tmp = tmp[1]
                else :
                    tmp = tmp[0]

                tmp = tmp.split("?")[0]
                n = tmp.rfind('/')
                if tmp[n+1:].isdigit() : 
                    tmp = tmp[:n]

                if len(tmp) > 1 : 
                    if tmp[-1] == "/" : 
                        tmp = tmp[:-1]
                    if tmp[0] == '#' or tmp == '/' or tmp[0] == ' ' :
                        pass
                    else : 
                        linklist.append(tmp)

            # print (link.attrs['href'])
    for res in linklist :
        if res in reslist :
            pass
        else:
            reslist.append(res)

    print ("-----link lists ---- ")

    # print(linklist)
    for res in reslist :
        print (res)
    
    print ("-----inputs lists  ---- ")

    for inputs in soup.findAll("input"):
        if (inputs.attrs['type']) == "text" : 
            getpar = inputs.find_parent('form')['action']
            print ("URL : " + getpar + "  | id : " +inputs.attrs['id'])
            # print (inputs.parent)
            # print (inputs)
    