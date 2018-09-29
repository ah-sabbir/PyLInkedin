import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import sys
"""--------- Construction is  Running ------------"""
"""--------- Developed by Ahmmed Sabbir ------------"""
# start find Chrome webdriver path location
class AutoBrowser:
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
        #self.goto_nav()
        self.myNetwork()
    def myNetwork(self):
        #try:
        self.driver.get("https://www.linkedin.com/sales/search/people")
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_css_selector("div[data-test-filter-code='GE']").click()
        self.driver.implicitly_wait(15)
        time.sleep(15)

        
        self.myNetwork_filter()
    def myNetwork_filter(self):
        current_url_=self.driver.current_url
        names=[]
        urls=[]
        titles=[]
        linkedin_profiles=[]
        counter=1
        while True:
        # while still page running 
            pr_link=[]
            Geography=self.driver.page_source
            for profile_link in bs(Geography,"html.parser").find_all("a",{"class":'ember-view'}):
                if ("%3D%3D"in profile_link["href"]) and ("NAME_SEARCH" in profile_link["href"]):
                    p_link = ("https://www.linkedin.com"+profile_link['href'])
                    if (p_link in pr_link) or ("similar-leads" in p_link):
                        pass
                    else:
                        pr_link.append("https://www.linkedin.com"+profile_link['href'])

            for link_ in pr_link:
                self.driver.get(link_)
                self.driver.implicitly_wait(15)
                time.sleep(5) # via this goto profiles of every persons
                # do somthing in users profiles or get data from users profile
                try:
                    name=bs(self.driver.page_source,"lxml").find("span",{"class":"profile-topcard-person-entity__name"}).text
                    names.append(name)
                except:
                    print("name problem")
                    names.append("Not Found")
                try:
                    title_with_company=bs(self.driver.page_source,"lxml").find("dd",{"class":"mt2"}).text
                    titles.append(title_with_company)
                except:
                    titles.append("not found")
                try:
                    website=bs(self.driver.page_source,"lxml").find("dd",{"class":"mv2 nowrap-ellipsis mv2 Sans-14px-black-60%"})
                    urls.append(website.text)
                except:
                    urls.append("not found")
                try:
                    linkedin_pro = bs(self.driver.page_source,"lxml").find("a",{"class":"view-linkedin profile-topcard-actions__overflow-item link-without-visited-state Sans-14px-black-90%-bold block p2"})
                    linkedin_profiles.append(linkedin_pro)
                except:
                    linkedin_profiles.append("not found")
                print("-----------------------------")
                
            try:
                self.driver.get(current_url_)
                self.driver.implicitly_wait(15)
                self.driver.find_element_by_css_selector("[class=search-results__pagination-next-button]").click()
                time.sleep(10)
                current_url_ = self.driver.current_url
                print("goto next page")
            except:
                data_list={"names":names,"titles":titles,"urls":urls,"linkedin profiles":linkedin_profiles}
                writer = pd.ExcelWriter('linkedin_leads.xlsx', engine='xlsxwriter')
                dataframe= pd.DataFrame(data_list)
                self.driver.quit()
                sys.exit()
            pr_link=[]
            if counter==10:
                break
            counter+=1
        data_list={"names":names,"titles":titles,"urls":urls,"linkedin profiles":linkedin_profiles}
        writer = pd.ExcelWriter('linkedin_leads.xlsx', engine='xlsxwriter')
        dataframe= pd.DataFrame(data_list)
    def goto_nav(self):
        self.main_window=self.driver.current_window_handle
        try:
            sales_nav=self.driver.find_element_by_css_selector('a[class="nav-item__link ember-view"]')
            sales_nav.click()
            self.driver.implicitly_wait(10)
            self.main_window.close()
            #closed_window=self.driver.switch_to_window(self.main_window)
            closed_window.close()
        except:
            try:
                sales_nav = self.driver.find_element_by_css_selector('a[id="ember907"]')
                sales_nav.click()
            except:
                sales_nav = self.driver.find_element_by_css_selector('span[class="nav-item__icon svg-icon-wrap"]')
                sales_nav.click()

"""
this is the primary area to start program and call classes functions etc.
"""

#path=r'web_drivers\chromedriver.exe'  #  the path location of chromedriver.exe
#options.binary_location = path

#open_driver_path=webdriver.Chrome(executable_path=path)
#START = AutoBrowser(open_driver_path) # Call Class and give paramiter this 


