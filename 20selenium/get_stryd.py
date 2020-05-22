import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from strydlogin import username, password

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)


web_browser = webdriver.Firefox()
# https://www.stryd.com/powercenterbeta/profile
web_browser.get('https://www.stryd.com/powercenter')



web_browser.find_element_by_class_name('facebook').click()
web_browser.find_element_by_id('email').send_keys(username)
web_browser.find_element_by_id ('pass').send_keys(password)
web_browser.find_element_by_id('loginbutton').click()
  



wait = WebDriverWait(web_browser, 10)
element = wait.until(EC.title_contains('Stryd PowerCenter'))
#web_browser.get(f'https://www.stryd.com/powercenter/calendar/?sid={web_browser.session_id}')


myreaponse = web_browser.execute_script("return document.getElementById('5782253728366592')")
print(myreaponse)

web_browser.get(f'https://www.stryd.com/powercenter/runs/5782253728366592/?sid={web_browser.session_id}')

wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h3'), 'Distance Splits'))

el = web_browser.find_elements_by_tag_name('p')
for items in el[:31]:
    print(items.text)


web_browser.quit()
