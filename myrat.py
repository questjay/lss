import socks
import socket
import time
import random
import json
import ipaddress
import os
from datetime import date, datetime,timedelta
from urllib.request import Request, urlopen, build_opener
import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
from mechanize import Browser
from fake_useragent import UserAgent
from mylist import mmy
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver


class Miny(object):
  def __init__(self):
    self.ua = UserAgent()
    self.ma = self.get_prox()
    self.name = 0
    self.cou = 0
    self.driver = None
    self.GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    self.CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    #def gtprox():
    #    return self.get_prox()
    #https://gretaith.com/?l=XKmG8ooqkNkREHl&s=188425821503886060&z=2747633
    #http://deloplen.com/afu.php?zoneid=1407888&var=2747633
    #https://propu.sh/ntfc.php?p=2747613&r=h&trace_id=1272ce92-2afa-4d09-b0ce-490206f8ddd4&pov=1&tagl=pushlat.com&landId&zoneId=2747613&oaid=d5b787382fdf5289fa9d693a7d5d8456#!
    """def mailguner(much):
    key = ''
    sanbx =''
    rqseat = 'questjayjay@gmail.com'
    request_url = 'https://api.mailgun.net/v3/{n}/messages'.format(n = sanbx)
    requests.post(request_url,auth=('api'= key),data{
        'from':'questjayjay@gmail.com',
        'to':rqseat,
        'subject':'quest its me 2000',
        'text':'we have hit {m}'.format(m = much)} )
    return None"""
  def prox(self, n):
    pro =   0
    if n == 'ProxyMoxy':
        pro = 54383
    elif n == 'Xorg':
        pro = 47267
    elif n == 'DexterProxy':
        pro = 0
    elif n == 'Defender':
        pro = 65295
    elif n == 'HttpSocks':
        pro = 764
    elif n == 'Socks':
        pro = 7744
    elif n == 'BigProxy':
        pro = 11642
    elif n == 'Agile':
        pro = 0
    elif n == 'GrubMe':
        pro = 3380
    elif n == 'Polymorth':
        pro = 17986
    elif n == 'BigGoodProxy':
        pro = 11642
    elif n == 'Xinemara':
        pro = 11642
    elif n == 'BigBlind':
        pro = 11642
    elif n == 'NineBeforeZero':
        pro = 38697
    elif n == 'SmallProxy':
        pro = 31653
    elif n == 'DontGrubMe':
        pro = 2219
    elif n == 'SmallBlind':
        pro = 56458
    else:
        pro = 0
    return pro

  def port(self, n):
    
    mimi = n.replace('\n\n          //<![CDATA[\n            document.write(','')
    mi = mimi.replace(');\n          //]]>\n          \n','')
    sg =','.join(mi.split('^'))
    h = sg.split(',')
    m = self.prox(h[0])^self.prox(h[1])^int(h[2])
    return m    

  def create_t(self):
    headers = {'User-Agent':self.ua.random}
    image = []
    n = r.get('https://sockslist.net/', headers = headers)
    sop = BeautifulSoup(n.content,'html.parser')
    p = sop.find(class_="proxytbl")
    so = p.find_all('tr')
    for i in range(1,len(so)-1):
        image.append({'ip':so[i].find(class_="t_ip").get_text(),'port': self.port(so[i].find(class_="t_port").get_text())})
    
    return image

  def read_cs():
    r = open('UsIP.json', "r" )
    m = json.loads(r.read())
    ip = []
    try:
        for n in list(ipaddress.ip_network(m[random.randint(1,len(m))]['network']).hosts()):
            ip.append({'ip': str(n)})
        return str(ip[random.randint(1,len(ip))]['ip']) 
        
    except Exception as e:
        return str(ip[1]['ip'])

  def free_prox(self):
    headers = {'User-Agent':self.ua.random}
    image = []
    n = r.get('https://free-proxy-list.net/', headers = headers)
    sop = BeautifulSoup(n.content,'html.parser')
    p = sop.find("tbody")
    so = p.find_all('tr')
    for i in range(len(so)):
        image.append({'ip': so[i].find_all('td')[0].string,'port':so[i].find_all('td')[1].string})
    return image

  def get_prox(self):
    gn = []
    for i in self.create_t():
        gn.append(i)
    """for n in self.free_prox():
        gn.append(n)"""
    return gn

  def connection(self,n):
    m = 1
    try:
       m = random.randint(0,len(n)-1)
    except Exception as e:
       m = 1
    #sock.send(b'GET /miners/get?file=BFGMiner-3.99-r.1-win32.zip HTTP/1.1\nUser-Agent:MultiMiner/V3\nHost: azenv.net\n\n')
    return m
    # add username and password arguments if proxy authentication required.
  def startter(self, agent):
    ip = self.read_cs()
    #self.driver = None
    m = self.connection(self.ma)
    print(self.ma[m])
    try:
        
        #profile = webdriver.FirefoxProfile()
        #profile.set_preference("network.proxy.type", 1)
        #profile.set_preference("network.proxy.http" ,PROXY_HOST )
        #profile.set_preference( "network.proxy.http_port" ,int(PROXY_PORT))
        #profile.set_preference( "general.useragent.override" ,"'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_6)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.95 Safari/537.36'" )
        path1 = 'chromedriver76.exe'
        options = {
          'proxy':{
            'http':'http://{iip}:{port}'.format(iip = ip, port = self.ma[m]['port']),
            'https':'https://{iip}:{port}'.format(iip = ip, port = self.ma[m]['port'])
            #'no_proxy':'localhost,127.0.0.1,dev_server:8080'
            }
          }
        self.driver = webdriver.Chrome(executable_path = path1)
        vn = {'X-Forwarded-For': '{iip}'.format(iip = ip), 'Referer': 'www.000webhostapp.com','User-Agent':agent}
        self.driver._client.set_header_overrides(headers = vn)
        self.driver.get('http://azenv.net')
        time.sleep(10)
        self.driver.refresh()
        #self.driver.save_screenshot( "mk\{s}.png".format(s = random.randint(1098, 10000476)) )
        #self.driver.close()
        #driver.save_screenshot( "mk\{s}.png".format(s = random.randint(1098, 10000476)) )
        #driver.close()
        self.driver.delete_all_cookies()
        self.driver.quit()
        """if len(self.ma) <=1:   
            self.ma = self.get_prox()
            self.cou = 0   
        else:
            self.cou += 1
            print(self.cou)
            print(self.ma[m])
            del self.ma[m]
            time.sleep(2)"""
            
    except Exception as e:
        if self.driver != None:
            self.driver.close()
            self.driver.quit()
        """print(e)
        if len(self.ma) <=1 or self.cou >= 10:
               
            self.ma = self.get_prox()
            self.cou = 0 """  
        """else:
            self.cou += 1
            print(self.ma[m])
            del self.ma[m]
            time.sleep(2)"""
           
if __name__ == '__main__':
    n = mmy
    miny = Miny()
    name = 0
    while True:
        m = n[miny.connection(n)]
        print(m)
        #name +=1
        miny.startter(m)
        randrange(10) 
        time.sleep(2)
