from bs4 import BeautifulSoup
import requests
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': 'You cookie'
}

urllist = []
for i in range(669):
    url = 'http://cszyedu.pocketuni.net/index.php?app=event&mod=School&act=rank&k=3&p={page}'.format(page=i)
    urllist.append(url)


for url in urllist:
    r=requests.get(url,headers = headers)
    urllist.append(r)
    soup=BeautifulSoup(r.content,'html.parser')
    print(soup.name)
    t = soup.find_all(re.compile('^td'))

    for title in t:
        print(title.string)
        with open("cszypu.txt", 'a', encoding='utf-8') as a:
            a.write(str(title.string)+'\n')
