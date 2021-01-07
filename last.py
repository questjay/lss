from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from mylist import mmy
from selenium.webdriver.support.ui import WebDriverWait
import time
import socks
import socket
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from revenuehit import questJay
import os
import json
from bs4 import BeautifulSoup
import ipaddress
import requests
import random
#from browsermobproxy import Server
#from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Miny(object):
  def __init__(self):
    self.path1 = "/home/jay/dev/geckodriver"
    self.driver = None
    self.server = None
    self.st = False
    self.binary = r'/usr/bin/firefox'
    self.proxy = None
    self.n = mmy
    self.number = 1
    self.numb = 1
    self.ck = 1
    self.hola = ['37.235.52.73','170.78.75.55','45.114.116.123','170.75.162.239','181.119.30.44',
                      '89.164.99.14','89.187.143.24','185.134.30.248','5.172.196.36','194.71.130.15',
                     '45.114.118.103','217.78.5.128','83.136.106.159','201.131.125.180','217.170.204.88',
                       '188.123.123.115','31.40.251.195','151.236.23.55','46.246.28.154','178.209.51.166',
                       '31.210.91.240','201.211.227.249']
  def rad_c(self):
    
    try:
        r = open('UsIP.json', "r" )
        m = json.loads(r.read())
        ip = []
        for n in list(ipaddress.ip_network(m[random.randint(1,len(m))]['network']).hosts()):
            ip.append({'ip': str(n)})
        return str(ip[random.randint(1,len(ip))]['ip']) 
        
    except Exception as e:
        return str(ip[0]['ip'])
      
  def ter(self, url):
    np = []
    sop =  BeautifulSoup(url,'html.parser')
    old = BeautifulSoup((str(sop.find_all(id="SC_TBlock_810057")).replace('[','')).replace(']',''),'html.parser')
    print(old) 
    n = old.find_all('a')
    print(n)
    for i in range(len(n)):
            np.append(n[i]['class'])
    
    return "//a[@class='{n}']".format(n = (str(random.choice(np)).replace("['",'')).replace("']",''))
  
  def tser(self, url):
    np = []
    sop =  BeautifulSoup(url,'html.parser')
    old = BeautifulSoup((str(sop.find_all(id="SC_TBlock_810057")).replace('[','')).replace(']',''),'html.parser')
    print(old) 
    n = old.find_all('a')
    print(n)
    for i in range(len(n)):
            np.append(n[i]['href'])
    
    return (str(random.choice(np)).replace("['",'')).replace("']",'')
  
  def myip(self, n):
      try:
        sop =  BeautifulSoup(n,'html.parser')
        x = sop.find_all(class_="rna_ad")
        return "rNA3218_{n}_title".format(n =random.randint(1,4))
      except Exception as e:

        pass
  def heckProxy(self,nm):
    try:
        url ='https://awebanalysis.com/en/ip-lookup/{n}/'.format(n =nm)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
         'Accept': '*/*',
         'Connection': 'keep-alive',
         'True-Client-IP': '3.6.114.227',
         'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        x = requests.get(url, headers= header)
        x =  BeautifulSoup(x.content,'html.parser')
        pr= x.find_all(id="ipdetails")[1].span.get_text()
        if pr == 'Proxy Detected':
           return True
        else:
            return False
    except Exception:
        print('bad error CheckProxy')
        return True

  def Recursion(self,k):
     py = self.heckProxy(k)
     jk =''
     if py:
        jk = self.Recursion(self.rad_c())
     else:
        jk = k 
     return jk 
  def serStart(self):
      if self.st:
          return self.proxy
      else:
          #self.server =Server(self.hen)
          #self.server.start()
          #self.proxy = self.server.create_proxy(params={'port':1700,'trustAllServers':'true'})
          self.st  = True
          return self.proxy
  def lcm(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index('?')
      hj = '/ntclcm'+oldURL[index:]
      
  def Recl(self, kl):
    try:
     sop = kl 
     f = ''
     p=  json.loads(sop) 
     for i in range(len(p)):
         
         if p[i]['rinfo']['rw']:
             f = p[i]['rinfo']['rw']
             
     return {'ur':  self.lcm(random.choice(p)['ads'][0]['uf']),'ipm':f, 'which':True}
     
    except Exception as e:
     print(e)
     return {'ur': '','ipm':'','which':False}

  def getProxyscan(self):
    try:
        url = "https://www.proxyscan.io/Home/FilterResult"
        proxy = []
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
       'Accept': '*/*',
       'Accept-Encoding': 'gzip, deflate, br',
       'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
       'X-Requested-With': 'XMLHttpRequest',
        'Content-Length': '108',
        'Connection': 'keep-alive',
        'True-Client-IP': '3.6.114.227',
        'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        myobj = {'status':'1',
                'ping':"",
                'selectedType':'SOCKS5',
                'SelectedAnonymity':'Anonymous',
                'sortPing':'false',
                'sortTime':'true',
                'sortUptime':'false'}

        x = requests.post(url, headers= header, data = myobj)
        
        x =  BeautifulSoup(x.text,'html.parser')
        x = x.find_all('tr')
        for i in range(  len(x)):
          if str(x[i].find_all('td')[7].get_text()).endswith('seconds'):
              proxy.append(x[i].th.get_text()+':'+x[i].td.get_text())
        
    
        return proxy
    except Exception as e:
        pass
    
  def RecD(self, k):
    try:
     sop = BeautifulSoup(k,'html.parser')
     url = ((sop.find('script').get_text()).replace('window.location = ','')).replace('"','')
     
     return url
     
    except Exception as e:
     print(e)
     return ''
  def questRe(self, url):
    try:
        
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
         'Accept': '*/*',
         'Connection': 'keep-alive',
         'True-Client-IP': '3.6.114.227',
         'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        myobj = {'status':'1',
                'ping':"",
                'selectedType':'SOCKS5',
                'SelectedAnonymity':'Anonymous',
                'sortPing':'false',
                'sortTime':'true',
                'sortUptime':'false'}

        
        x = requests.get(url, headers= header)
        print(x.content)
        return proxy
    except Exception as e:
        pass
  def getroxyscan(self):
    
    url = 'https://hidemy.name/en/proxy-list/?country=ALARAMAUBDBABWBRBGKHCACLCOCDCRHRCZDKECFIFRGEDEGRHNHKHUINIDIRIQIEITJPKZKEKRLALVLBLRLYLTMKMWMYMXMDMNMMNPNLNINGPKPSPEPHPLPTPRRORURSSGSKSOZAESSECHSYTWTJTHTRUAGBUSVN&type=5#list'
    try:
        proxy = []
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
         'Accept': '*/*',
         'Connection': 'keep-alive',
         'True-Client-IP': '3.6.114.227',
         'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        myobj = {'status':'1',
                'ping':"",
                'selectedType':'SOCKS5',
                'SelectedAnonymity':'Anonymous',
                'sortPing':'false',
                'sortTime':'true',
                'sortUptime':'false'}

        
        x = requests.get(url, headers= header)
        
        x =  BeautifulSoup(x.content,'html.parser')
        x = x.find(class_="table_block").find('tbody')
        
        x = x.find_all('tr')
        for i in range(len(x)):
           if str(x[i].find_all('td')[6].get_text()).endswith('seconds'):
                proxy.append(x[i].td.get_text()+':'+x[i].find_all('td')[1].get_text())
    
        return proxy
    except Exception as e:
        pass
  def h_ip(self,url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index(':')
      hj = (oldURL[:index]).replace(':','')
      return hj
  def lcm(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index('?')
      hj = '/ntclcm'+oldURL[index:]
      return hj
  def h_port(self,url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index(':')
      hj = (oldURL[index:]).replace(':','')
      return hj
  def getAll(self):
    movie = []
    
    n = self.getroxyscan()
    if n is not None:
        for i in range(len(n)):
            movie.append(n[i])
    n = self.getProxyscan()
    if n is not None:
        for i in range(len(n)):
            movie.append(n[i])
    return movie[+1:]
  
  def get_random_string(self, length):
    gh =  ["https://player.fm/music/","https://player.fm/mix/",
      "https://player.fm/songs/","https://player.fm/videos/","https://player.fm/celebrities/",
     "https://player.fm/","https://player.fm/news/","https://player.fm/famouspeople/","https://player.fm/lyrics","https://player.fm/shows/3/",
                 "https://player.fm/movies/1/"]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-/'
    result_str = ''.join(random.choice(letters) for i in range(length))
    fn = random.choice(gh) + result_str
    return fn
  def heckTit(self):
    try:
        url ='https://official-joke-api.appspot.com/jokes/random'
        nu = random.randint(1,2)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
         'Accept': '*/*',
         'Connection': 'keep-alive',
         'True-Client-IP': '3.6.114.227',
         'Forwarded': 'for="3.6.114.227',
         'Pragma': 'no-cache',
         'Cache-Control': 'no-cache'}
        x = requests.get(url, headers= header)
        x =  x.json()
        print(x)
        if nu == 1:
           return (x['setup']).replace('?','')
        else:
            return (x['punchline']).replace('?','') 
    except Exception:
        
        return 'Latest Celebrities  News List '  
  
  def browsSart(self):
     try: 
          
             ip = '' #self.Recursion(self.rad_c()) #proxy =self.serStart()
             pr = self.getAll()
             #roxy = random.choice(pr)
             ns = random.choice(self.hola)
             print(ns)
             ptions = {
                 'proxy': {
                    'https': 'https://170.75.162.239:22222'.format(ns = ns),
                    'http': 'http://170.75.162.239:22222'.format(ns = ns),
                     'custom_authorization': 'Basic dXNlci11dWlkLTJjYzAwMzIwZDU3NWQ1NDZiYzBiNDJhNzUxYTFmZDQ3OmRjOGVjYzVhODM4YQ=='
                    },
                 'connection_timeout':None,
                 'connection_keep_alive': True  
                 } 
             #print(roxy)
             
             cap = DesiredCapabilities().FIREFOX
             hrome_options = webdriver.ChromeOptions()
             profile = webdriver.FirefoxProfile()
             uio = ['https://player.fm/news','https://player.fm/famouspeople','https://player.fm/lyrics','https://player.fm/shows/3',
                 'https://player.fm/movies/1']
             
             
             
             options = Options()
             #options.add_argument("--headless")
             options.add_argument("--disable-web-security")
             #options.binary = self.binary
             cap["marionette"] = True
             
             profile.set_preference("browser.link.open_newwindow" ,1)
             
 
             profile.set_preference("general.useragent.override",random.choice(self.n))
             
             
             self.driver = webdriver.Firefox(firefox_profile = profile,firefox_options=options, capabilities=cap, executable_path='geckodriver.exe')
             from selenium.webdriver.support import expected_conditions as ec
             from selenium.webdriver.common.action_chains import ActionChains
             #self.driver.get('https://p393158.clksite.com/adServe/banners?tid=393158-772142-POPUNDER&tagid=2')
             self.driver.get('http://127.0.0.1:8000/about')
             #print((self.driver.page_source.strip()))
             #questJay(self.driver.page_source)
             #self.driver.get(questJay(self.driver.page_source))
             por = self.driver.execute_script("return window.rNA_gVID();")
             tim = self.driver.execute_script("return Date.now();")
             print(por)
             print(tim)
             self.driver.implicitly_wait(10)
             self.driver.delete_all_cookies()
             self.driver.execute_script('window.localStorage.clear();')
             self.driver.execute_script('window.sessionStorage.clear();')
             self.driver.quit()
             print('good')
             if self.number >= 30:
               
                self.number = 1
                print(self.number)
             else:
                self.number = self.number + 1
                print(self.number)
     except Exception as e:
          print(e)
          if self.driver:
              pass #self.driver.quit()
          os.system('fuser -n tcp -k 1700')
          self.st = False

if __name__ == '__main__':
    
    miny = Miny()
    while True:
        miny.browsSart()
        time.sleep(1)
