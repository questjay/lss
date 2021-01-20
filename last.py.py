from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from mylist import mmy
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    self.numb = 1
    self.ck = 1
    self.number = 1
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
  

  def myip(self):
      try:
         return "//a[@id='rNA3289_{n}_title']".format(n =random.randint(1,4))
        
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
  def get_random_string(self,length):
    gh =  ["https://player.fm/music/","https://player.fm/mix/",
      "https://player.fm/songs/","https://player.fm/videos/","https://player.fm/celebrities/",
     "https://player.fm/","https://player.fm/news/","https://player.fm/famouspeople/","https://player.fm/lyrics","https://player.fm/shows/3/",
                 "https://player.fm/movies/1/"]
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    result_str = ''.join(random.choice(letters) for i in range(length))
    fn = random.choice(gh) + result_str
    return fn
  
  def heckTi(self):
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
        
        if nu == 1:
           return (x['setup']).replace('?','')
        else:
            return (x['punchline']).replace('?','') 
    except Exception:
        
        return 'Latest Celebrities  News List'
      
  def chy(self, h,n):
    return random.randint(h,n)

  def stone(self,n):
    gh = ["humor-jokes/","trending/","chutkule/"]
    nu = random.randint(1,2)
    if nu == 1:
        return self.get_random_string(self.chy(6,20))
    else:
        return 'https://player.fm/' + random.choice(gh) + '-'.join(n.split())
      


  def scren(self):
    n= self.chy(1024,1920)
    gh = []
    b =self.chy(171,600)
    gh =[{"w":"1920","h":"1200"},{"w":"1024","h":"768"},{"w":"800","h":"600"},{"w":"1366","h":"768"},{"w":"1280","h":"1024"},
         {"w":"500","h":"171"},{"w":"300","h":"371"},{"w":"{n}".format(n=n),"h":"500"},
                                          {"w":"800","h":"{n}".format(n=b)}]
    
    return random.choice(gh)
  def lcm(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index('/f/')
      hj = oldURL[index:]
      return hj
    
  def lcs(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index(',')
      hj = oldURL[:index]
      return (hj).replace("'","")
    
  def lcf(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index("['")
      hj = oldURL[index:]
      n = (hj).replace("'","")
      if (n).startswith('O'):
        return 'go/'+(n[1:]).replace('O','')
      else:
       return 'dc/?id='+(n[1:]).replace('C','') 
    
  def lcl(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index(']')
      hj = oldURL[:index]
      return (hj).replace("'","")
    
  def h_vid(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index('vid=')
      hj = oldURL[index:]
      return hj
    
  def lcvi(self, url):
      oldURL = url
      index = 0
      newURL = oldURL
      index = oldURL.index('&')
      hj = oldURL[:index]
      return hj
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
        
        return 'Latest Celebrities  News List | player.fm'
  def heckSrcipt(self, nm):
    x =  BeautifulSoup(nm,'html.parser')
    return x.find_all("script")[1]['src']

  def heckAt(self, nm):
    x =  BeautifulSoup(nm,'html.parser')
    return len(x.find_all(class_ = "rna_ad")) - 1
  
  def Titlesion(self):
     jk = ''
     if self.driver.title == 'jay jay':
        time.sleep(3)
        self.Titlesion()
     else:
        jk = 'jkjkj'
     return jk
    
  def browsSart(self):
     try:
             sc = self.scren()
             #ip = self.Recursion(self.rad_c()) #proxy =self.serStart()
             pr = self.getAll()
             roxy = random.choice(pr)
             nser = random.choice(self.n)
             ns = random.choice(self.hola)
             roxy = random.choice(pr)
             cap = DesiredCapabilities().FIREFOX
             hrome_options = webdriver.ChromeOptions()
             profile = webdriver.FirefoxProfile()
             gph ={"url":"http://127.0.0.1:8000","n":1},{"url":"http://127.0.0.1:8000/m/twit/","n":2}
             ren = random.choice(gph)
             nums = int(ren["n"])
             options = Options()
             #options.add_argument("--headless")
             options.add_argument("--disable-web-security")
             #options.binary = self.binary
             #cap["marionette"] = True
             profile.set_preference("dom.push.enabled" ,True) 
             profile.set_preference("browser.link.open_newwindow" ,1)
             PROXY = self.h_ip(roxy)+':'+self.h_port(roxy) #"170.75.162.239:22222"
             print(PROXY)
             profile.set_preference("browser.link.open_newwindow" ,1)
             
 
             profile.set_preference("general.useragent.override",random.choice(self.n))
             pd = self.stone(self.heckTit())
             ip, port = PROXY.split(':')
             profile.set_preference('network.proxy.type', 1)
             profile.set_preference('network.proxy.socks', ip)
             profile.set_preference('network.proxy.socks_port', int(port))
             profile.update_preferences()
             self.driver = webdriver.Firefox(firefox_profile = profile,options=options, capabilities=cap, executable_path='geckodriver.exe')
             from selenium.webdriver.support import expected_conditions as ec
             from selenium.webdriver.common.action_chains import ActionChains
             from selenium_move_cursor.MouseActions import move_to_element
             import pyautogui
             #self.driver.maximize_window()
             self.driver.get(ren['url'])
             self.driver.set_page_load_timeout(10)
             nm = self.driver
             element_presen = EC.presence_of_element_located((By.XPATH, '//body'))
             WebDriverWait(self.driver,10).until(element_presen)
             self.driver.execute_script("window.stop();")
             #myElem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'rNA3290')))
             #self.driver.implicitly_wait(5)
             #time.sleep(10)
             current_url = self.driver.current_url
             print(current_url)
             nat =  self.heckSrcipt(self.driver.page_source)
             #nh = self.heckAt(self.driver.page_source)
             
             last_height = self.driver.execute_script("return document.body.scrollHeight")
             self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             print('ok')
             que = random.randint(0, self.heckAt(self.driver.page_source))
             print(que)
             
             if nums == 1:
               print('re1')
               myDiv =  'rNA3290_{n}_image'.format(n = que)
               myIv =  'rNA3290_{n}_title'.format(n = que)
               bnn = 'var x = document.createEvent("MouseEvent"); x.initMouseEvent("mouseover", true, true); document.getElementById("{n}").dispatchEvent(x);'.format(n = myDiv)
               bnQ = 'var x = document.createEvent("MouseEvent"); x.initMouseEvent("mouseover", true, true); document.getElementById("{n}").dispatchEvent(x);'.format(n = myIv)
               print(bnn)
               if self.numb == self.ck:
                  element_presen = EC.presence_of_element_located((By.ID, 'rNA3290_{n}_image'.format(n = que)))
                  WebDriverWait(self.driver,10).until(element_presen)
                  #pyautogui.mouseDown()
                  self.driver.execute_script(bnQ)
                  time.sleep(2)
                  self.driver.execute_script(bnn)
                  time.sleep(3)
                  self.driver.find_element_by_id( 'rNA3290_{n}_image'.format(n = que)).click()
                  self.driver.execute_script(bnQ)
                  time.sleep(1)
                  element_present = EC.presence_of_element_located((By.XPATH, '//body'))
                  WebDriverWait(self.driver, 5).until(element_present)
                  self.Titlesion()
                  self.numb = 1
                  self.ck = random.randint(2,3)
                  print(self.numb)
               else:
                  self.numb = self.numb + 1
                  print(self.numb)
             else:
               print('re2')
               myDiv =  'rNA3338_{n}_image'.format(n = que)
               myIv =  'rNA3338_{n}_title'.format(n = que)
               bnn = 'var x = document.createEvent("MouseEvent"); x.initMouseEvent("mouseover", true, true); document.getElementById("{n}").dispatchEvent(x);'.format(n = myDiv)
               bnQ = 'var x = document.createEvent("MouseEvent"); x.initMouseEvent("mouseover", true, true); document.getElementById("{n}").dispatchEvent(x);'.format(n = myIv)
               print(bnn)
               if self.numb == self.ck:
                  element_presen = EC.presence_of_element_located((By.ID, 'rNA3338_{n}_image'.format(n = que)))
                  WebDriverWait(self.driver,10).until(element_presen)
                  #pyautogui.mouseDown()
                  self.driver.execute_script(bnQ)
                  time.sleep(2)
                  self.driver.execute_script(bnn)
                  time.sleep(3)
                  self.driver.find_element_by_id( 'rNA3290_{n}_image'.format(n = que)).click()
                  self.driver.execute_script(bnQ)
                  time.sleep(1)
                  element_present = EC.presence_of_element_located((By.XPATH, '//body'))
                  WebDriverWait(self.driver, 5).until(element_present)
                  self.Titlesion()
                  self.numb = 1
                  self.ck = random.randint(2,3)
                  print(self.numb)
               else:
                  self.numb = self.numb + 1
                  print(self.numb)
             #ActionChains(self.driver).click(self.driver.find_element_by_id( 'rNA3330_0_image')).perform()
             #self.driver.find_element_by_id( 'rNA3330_0_title').click()
             self.driver.implicitly_wait(10)
             time.sleep(10)
             
             """self.driver.get(nat)
             gh = self.lcm(self.driver.page_source)
             g = self.lcs(gh)
             fg = self.lcl(self.lcf(gh))
             #las = 'http://nativeadmatch.com/'+fg +'&'+ self.lcvi(self.h_vid(nat))+ 'h='+str(self.chy(316,600))+','+str(self.chy(90,350))+','+sc['w']+','+sc['h']+',0.'+str(self.chy(150,2))
             #self.driver.get(las)
             iframe = self.driver.find_elements_by_id("rNA3330")
             print(len(iframe))
             if len(iframe) > 0:
               print(True)
               element_presen = EC.presence_of_element_located((By.XPATH, '//body'))
               WebDriverWait(self.driver,10).until(element_presen)
               #print(self.driver.page_source)
               print(2)
               if self.numb >= 1: #self.ck:
                 
                 por = self.driver.execute_script("return window.rNA_aGo();")
                 print(por)
                 self.driver.find_element_by_id( 'rNA3290_0_title').send_keys("\n")
                 ActionChains(self.driver).click(self.driver.find_element_by_id( 'rNA3290_0_title')).perform()
                 self.driver.implicitly_wait(20)
                 time.sleep(20)
                 element_prsent = EC.presence_of_element_located((By.XPATH, '//body'))
                 WebDriverWait(self.driver,10).until(element_prsent)
                 self.driver.implicitly_wait(1)
                 self.driver.refresh()
                 ActionChains(self.driver).click(self.driver.find_element_by_id( 'rNA3290_0_title')).perform()
                 self.driver.implicitly_wait(10)
                 self.numb = 1
                 self.ck = random.randint(2,5)
                 print(self.numb)
                 
               else:            
                 print('ok')
                 self.numb = self.numb + 1
                 print(self.numb)            
                 
             else:
               
               element_present = EC.presence_of_element_located((By.XPATH, '//body'))
               WebDriverWait(self.driver, 5).until(element_present)
               print(self.driver.title)
               time.sleep(10)"""
             if self.driver.title == 'Additional Verification':
                self.driver.refresh()
             print(self.driver.title)
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
              self.driver.quit()
          os.system('fuser -n tcp -k 1700')
          self.st = False
    
  
if __name__ == '__main__':
    
    miny = Miny()
    while True:
        miny.browsSart()
        time.sleep(1)
