from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


web_browser = webdriver.Firefox()
# https://www.stryd.com/powercenterbeta/profile
# https://www.seleniumeasy.com/test/basic-first-form-demo.html
web_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


assert "Selenium Easy Demo" in web_browser.title
show_message_button = web_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))


assert "Show Message" in web_browser.page_source
user_button = web_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button)
user_message = web_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am cool in Python')

# show_message_button.click()
# output_message = web_browser.find_element_by_id('display')
# assert 'I am cool in Python' in output_message.text

wait = WebDriverWait(web_browser, 100)
element = wait.until(EC.text_to_be_present_in_element((By.ID, 'display'), ('aaa')))
print(element)
web_browser.quit()
