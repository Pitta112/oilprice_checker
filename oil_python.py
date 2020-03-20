from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup

opt = webdriver.ChromeOptions()
opt.add_argument('headless') #hidden mode of chrome driver

driver = webdriver.Chrome(options = opt)

#url = 'https://www.google.com'
#search = driver.find_element_by_name('q') #search box
#search.send_keys('Mc Pit')
#search.send_keys(Keys.RETURN)

url = 'http://www.pttor.com/oilprice-capital.aspx'
driver.get(url) #open web
time.sleep(5)
#print(driver.page_source)

page_html = driver.page_source
driver.close()

data = soup(page_html,'html.parser') #scan data
table = data.findAll('table',{'id':'tbData'})
table = table[0].findAll('tbody')
rows = table[0].findAll('tr')
todayprice = rows[0].findAll('td')

oiltitle = ['วันที่',
            'Diesel Premium',
            'Diesel',
            'DieselB10',
            'DieselB20',
            'Benzene',
            'Gasohol95',
            'Gasohol91',
            'GasoholE20',
            'GasoholE85',
            'NGV']
oilprice = []

for ol in todayprice:
    oilprice.append(ol.text)

result = {}

for t,o in zip(oiltitle,oilprice):
    result[t] = o

from songline import Sendline
token = 'qdsJABjGrg86QA4K1Gmv5aYg9YEnmXV35L3ImCFZ7jj'

messenger = Sendline(token)
messenger.sendtext('ราคาดีเซลวันนี้: ' + result['Diesel'] + ' บาท')
messenger.sticker(12,1)
