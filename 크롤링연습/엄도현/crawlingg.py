from bs4 import BeautifulSoup
import urllib.request as req



def getphp(baseurl):
    #if response.status = 
    res = req.urlopen(baseurl)

    print("*** [System] Save the php address of the form... ***")
    phpu = []
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all('form'):
        phpu.append(tag['action']) #리스트 추가
        print("[find form] " + tag['action']) #리스트 출력

    return phpu
        






def getparm(baseurl):
    res = req.urlopen(baseurl)

    print("*** [System] Save the parameters sent to php. ***")
    parm = []
    soup = BeautifulSoup(res, 'html.parser')
    for tag in soup.find_all('form'):
        #print("[system] "+tag.get('action'))

        if 'login' in tag.get('action'):
            print("[system] login 존재")


            for logintag in tag.select('input'):
                print(logintag['name'])
                #print(logintag['name'])
                #parm.append(logintag['name']) #리스트 추가
                #parm.append(logintag) #리스트 추가
                #print("ggggggggggggggggg")


        else:
            parm.append(tag.find('input')['name']) #리스트 추가
            print("[find param] " + tag.find('input')['name']) #리스트 출력

    print("aaaaaaaaaaaaaaaaaa")
    print(parm)
    return parm





def getparm2(baseurl):
    res = req.urlopen(baseurl)

    print("*** [System] Save the parameters sent to php. ***")
    parm = []
    checkstring = ['id', 'pw', 'pass']
    soup = BeautifulSoup(res, 'html.parser')

    for tag in soup.find_all('form'):
        #print("[system] "+tag.get('action'))

        if 'login' in tag.get('action'):
            print("[system] login 존재")


            for logintag in tag.select('input'):
                print(logintag['name'])
                #print(logintag['name'])
                #parm.append(logintag['name']) #리스트 추가
                #parm.append(logintag) #리스트 추가
                #print("ggggggggggggggggg")


        else:
            parm.append(tag.find('input')['name']) #리스트 추가
            print("[find param] " + tag.find('input')['name']) #리스트 출력

    print("aaaaaaaaaaaaaaaaaa")
    print(parm)
    return parm







phpu = []
parm = []

baseurl = 'http://www.youtube.com'

phpu = getphp(baseurl)

#parm = getparm(baseurl)
parm = getparm(baseurl)

print("print php URL : " + str(phpu))
print("print parm : " + str(parm))


