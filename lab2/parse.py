import requests
from bs4 import BeautifulSoup

HTTPS = 'https://yandex.ru'
DEEP = 1
DOCTYPE = ['.pdf', '.docx', '.xlsx', '.doc', '.xls']
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

def chek_reference(href):
    if href.find('https://') != -1:
        return True
    if href.find('http://') != -1:
        return True
    return False
            
def get_links(html, site):
    soup = BeautifulSoup(html, features="html.parser")
    
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']

        if href.find('//') == 0:
            href = "https:" + href
        elif href.find('/') == 0:
            href = site + href
        elif not chek_reference(href):
            continue

        links.append(href)
        
    return list(set(links))

def check_file(link):
    for type in DOCTYPE:
        if link.find(type) != -1:
            return True
    return False

def parser(session, respons, site, deep):
    links = get_links(respons.text, site)
    
    file, subsite = [], []
    for link in links:
        try:
            print(link)
            if check_file(link):
                respons = session.head(link, timeout=1)
                if respons.ok:
                    file.append({
                        'file' : link,
                        'type' : respons.headers['Content-Type'],
                        'size' : respons.headers['Content-Length'] })

            elif deep > 0:
                respons = session.get(link, timeout=1)
                if respons.ok:
                    sub_file , sub_subsite = parser(session, respons, link, deep - 1)
                    subsite.append({
                        'site' : link,
                        'file' : sub_file,
                        'subsite' : sub_subsite })
        except:
            pass
    
    return file, subsite

def parse(site, deep):
    session = requests.Session()
    session.headers.update(user_agent)
    respons = session.get('https://' + site)

    file, subsite = [], []
    if respons.ok:
        file , subsite = parser(session, respons, site, deep)
        
    return {
        "site" : site,
        "file" : file,
        "subsite" : subsite
    }

# print (parse(HTTPS, DEEP))  
