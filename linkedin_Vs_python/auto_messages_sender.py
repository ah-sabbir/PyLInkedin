import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import sys
"""--------- Construction is  Running ------------"""
"""--------- Developed by Ahmmed Sabbir ------------"""
# start find Chrome webdriver path location

msg='''
this is a raw string write here your message which you wanna to send 
'''

class AutoSender:
    # end find Chrome webdriver path location
    def __init__(self,driver): 
        self.driver=driver
        self.driver.get("https://www.linkedin.com") # start open an url link
        self.driver.implicitly_wait(10)# start waitting until all data is loaded properlly
        self.browser_settings()
        self.collect_login_data()
# end of initialization panel 
    def browser_settings(self):
        # start setup browser settings
        options= webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=500*320')
        # end setup browser settings
    def collect_login_data(self):
        # start login to the linkedin
        # start collecting login information 
        self.email = self.driver.find_element_by_css_selector('input[class=login-email]')
        self.password = self.driver.find_element_by_css_selector('input[class=login-password]')
        self.login = self.driver.find_element_by_css_selector('input[type="submit"]')
        # end collecting login information 
        self.login_proccess()
    def login_proccess(self):
        # set user name and password then click login
        self.email.send_keys('linkedin user email here')
        self.password.send_keys('linkedin password here')
        self.login.click()
        # end login proccess into the linkedin
        # start waitting until all data is loaded properlly 
        self.driver.implicitly_wait(10)
        self.send_messages()
    def send_messages(self):
    	self.driver.get("https://www.linkedin.com/in/ahmmed-sabbir-848014161/")
    	self.driver.implicitly_wait(10)
    	src=self.driver.find_element_by_css_selector("input[role='combobox']").send_keys("Arafin Islam")
    	self.driver.find_element_by_css_selector("button[class='search-typeahead-v2__button typeahead-icon']").click()
    	self.driver.find_element_by_css_selector("span[class='name-and-distance']").click()
    	#self.driver.find_element_by_css_selector("button[class='pv-s-profile-actions pv-s-profile-actions--message button-primary-large mr2 mt2']").click()
    	#print(self.driver.find_element_by_css_selector(""))
    	"""self.driver.find_element_by_css_selector("div[role='textbox']").send_keys(msg.replace("f_name","first name"))
    	try:
    		self.driver.find_element_by_css_selector("button[class='msg-form__send-button button-tertiary-small']").click()
    	except:
    		self.driver.find_element_by_css_selector("button[class='msg-form__send-button button-tertiary-small']").send_keys(Keys.ENTER)
    	#   start sending url only 
    	self.driver.find_element_by_css_selector("div[role='textbox']").send_keys(site_link)
    	try:
    		self.driver.find_element_by_css_selector("button[class='msg-form__send-button button-tertiary-small']").click()
    	except:
    		self.driver.find_element_by_css_selector("button[class='msg-form__send-button button-tertiary-small']").send_keys(Keys.ENTER)"""


#path=r'web_drivers\chromedriver.exe'  #  the path location of chromedriver.exe
#options.binary_location = path

#open_driver_path=webdriver.Chrome(executable_path=path)
#START = AutoSender(open_driver_path)
