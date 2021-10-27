import requests
from bs4 import BeautifulSoup

DOCTYPE = ['.pdf', '.docx', '.xlsx', '.doc', '.xls']
BAD_DOCTYPE = ['.xml', '.jpg']
user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

def chek_reference(href):
    return 'https://' in href or 'http://' in href

def bad_refrence(href, site):
    if not site in href: return True
    for type in BAD_DOCTYPE:
        if type in href: return True

    if href.replace(site, '') == '': return True
    if href.replace(site, '') == ' ': return True
    if href.replace(site, '') == '#': return True
    return False

def get_links(html, site):
    soup = BeautifulSoup(html, features="html.parser")

    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        
        if href == '' or href == ' ' or href == '/' or href == '/ ': continue
        elif chek_reference(href):
            if bad_refrence(href, site): continue
        else:
            if href[0] == '/':
                href = site + href
            else: 
                href = site + '/' + href

            if bad_refrence(href, site): continue
        
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
                respons = session.head(link, timeout=2)
                if respons.ok:
                    file.append({
                        'file' : link,
                        'size' : respons.headers['Content-Length']})

            elif deep > 0:
                respons = session.get(link, timeout=2)
                if respons.ok:
                    subsite.append(link)
                    sub_file , sub_subsite = parser(session, respons, site, deep - 1)
                    for item_file in sub_file:
                        if not item_file in file:
                            file.append(item_file)
                    for item_subsite in sub_subsite:
                        if not item_subsite in subsite:
                            subsite.append(item_subsite)
        except:
            pass
    
    return file, subsite

def parse(site, deep):
    session = requests.Session()
    session.headers.update(user_agent)
    respons = session.get(site)

    file, subsite = [], []
    if respons.ok:
        file , subsite = parser(session, respons, site, deep)
    
    return {
        "site" : site,
        "file" : file,
        "subsite" : subsite
    }