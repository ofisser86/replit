from  selenium import webdriver

web_browser = webdriver.Chrome()
web_browser.get('http://seleniumhq.org/')
# assert "Selenium " in web_browser.title
web_browser.find_element_by_class_name('container')