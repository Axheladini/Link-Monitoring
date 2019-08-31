import time
import queue
import os
import webbrowser
import tldextract
from os import listdir
import selenium
from selenium.common.exceptions import NoSuchElementException
from websites import *
import functions
import json
from datetime import datetime
import requests
import http.client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


startTime = datetime.now()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')

chrome_driver = config.chromdrive
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)



module_list = os.listdir(os.getcwd()+"\websites")

languagess = []
languages_json = {}
for lang in module_list:
    module_name = lang[:-3]
    if module_name != "__init__" and module_name != "__pycach" and module_name != "config":
           languagess.append(eval(module_name))
           module_object = eval(module_name)
           temp_item = {module_object.lang.code: module_object.lang}
           languages_json.update(temp_item)


for language in languagess:

  print("Checking-> "+language.lang.name)
  
  for page in language.lang.pages:
    session = requests.Session()
    session.trust_env = False
    
    page_code = functions.gethttpstatuscode(page.link, session)
    
    if page_code == 404:
     print("--> "+page.name+" Does not exist")
    else:
     driver.get(page.link)
     for link in page.links:
        if link.check_by == "check_by_parent_id":
          
           functions.check_by_parent_id(driver, link, session)
           if(link.status == "1"):
             print("-------------> "+link.link_text+"-> OK")
           else:
             print("-------------> "+link.link_text+"-> ERROR")

        elif link.check_by == "check_by_text":

           functions.check_by_a_text(driver, link, session)
           if(link.status == "1"):
             print("-------------> "+link.link_text+"-> OK")
           else:
             print("-------------> "+link.link_text+"-> ERROR")
        elif link.check_by == "check_by_tittle":

           functions.check_by_title_attr(driver, link, session)
           if(link.status == "1"):
             print("-------------> "+link.link_text+"-> OK")
           else:
             print("-------------> "+link.link_text+"-> ERROR")

        elif link.check_by == "check_by_class":

           functions.check_by_class_name(driver, link, session)
           if(link.status == "1"):
             print("-------------> "+link.link_text+"-> OK")
           else:
             print("-------------> "+link.link_text+"-> ERROR")

        elif link.check_by == "check_by_link_id":

           functions.check_by_link_id(driver, link, session)
           if(link.status == "1"):
             print("-------------> "+link.link_text+"-> OK")
           else:
             print("-------------> "+link.link_text+"-> ERROR")
        

     print("--> "+page.name+" -> Checked")

json_data_en = json.dumps(languages_json, default=lambda o: o.__dict__, indent=4)


a = open("rrenja.js", 'w')
a.write("var result = ["+json_data_en+"]")
a.close()

print("..................")
print("Execution time:")
print(datetime.now() - startTime)


webbrowser.open(os.getcwd()+"\index.html")
	
time.sleep(15)
driver.close()
driver.quit()
          





