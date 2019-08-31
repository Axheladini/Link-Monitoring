from selenium.common.exceptions import NoSuchElementException
import requests
from websites import config
from requests.auth import HTTPBasicAuth
import json
import base64
import http.client
import tldextract
import time


#Function to find the href value by the parent id of the <a> element.check_by_value = check_by_parent_id
def check_by_parent_id(drive, the_object, req):

     try:
           find_the_element = drive.find_element_by_id(the_object.check_by_value)
           a = find_the_element.find_element_by_tag_name('a')
           the_href = a.get_attribute("href")
           if the_href == the_object.link_url:
              the_object.link_url_found = the_href
              the_object.http_status = gethttpstatuscode(the_href, req)
              the_object.checked = "1"
              the_object.status = "1"
              the_object.link_message = "Link found and is equal"
           else:
              the_object.link_url_found = the_href
              #r = req.get(the_object.link_url, stream=True)
              the_object.http_status = "wrong"
              the_object.checked = "1"
              the_object.status = "2"
              the_object.link_message = "Link found but is not equal with the one in the dataset"

     except NoSuchElementException as exception:
          
            the_object.link_url_found = "Selenium was not able to find the elemen, check details"
            the_object.http_status = "#"
            the_object.checked = "0"
            the_object.status = "3"
            the_object.link_message = "Element not found, please check if you inserted wrong element parent id or html output is updated"



#Function to find the href value by the text of a element. check_by_value = check_by_text
def check_by_a_text(drive, the_object, req):

    try:
         find_the_element = drive.find_elements_by_partial_link_text(the_object.check_by_value)
          
         if (len(find_the_element) > 0):
           for i in range(len(find_the_element)):
                 if i == 0:
                    a = find_the_element[i].get_attribute("href")
                    if a == the_object.link_url:
                       the_object.link_url_found = a 
                       the_object.http_status = gethttpstatuscode(a, req)
                       the_object.checked = "1"
                       the_object.status = "1"
                       the_object.link_message = "Link found and is equal"
                    else:
                       the_object.link_url_found = a
                       #r = req.get(the_object.link_url, stream=True)
                       the_object.http_status = "wrong"
                       the_object.checked = "1"
                       the_object.status = "2"
                       the_object.link_message = "Link found but is not equal with the one in the dataset"
         else:
           the_object.link_url_found = "Link text wrong"
           the_object.http_status = "Error"
           the_object.checked = "1"
           the_object.status = "0"
           the_object.link_message = "Link text not equal with the one in dataset. Check if link was updated on your web app!"

    except NoSuchElementException as exception:
          
            the_object.link_url_found = "Selenium was not able to find the element, check details"
            the_object.http_status = "#"
            the_object.checked = "0"
            the_object.status = "3"
            the_object.link_message = "Element not found, please check if you inserted wrong 'Link Text' or html output is updated"


#Function to find the href value by the tittle attribute. check_by_value = check_by_tittle
def check_by_title_attr(drive, the_object, req):
    
    try:
            name = the_object.check_by_value
            find_the_element = drive.find_element_by_xpath("//a[@title='" + name + "']")
            a = find_the_element.get_attribute("href")
            if a == the_object.link_url:
                       the_object.link_url_found = a
                       the_object.http_status = gethttpstatuscode(a, req)
                       the_object.checked = "1"
                       the_object.status = "1"
                       the_object.link_message = "Link found and is equal"
            else:
                       the_object.link_url_found = a
                       the_object.http_status = "wrong"
                       the_object.checked = "1"
                       the_object.status = "2"
                       the_object.link_message = "Link found but is not equal with the one in the dataset"

    except NoSuchElementException as exception:
          
            the_object.link_url_found = "Selenium was not able to find the elemen, check details"
            the_object.http_status = "#"
            the_object.checked = "0"
            the_object.status = "3"
            the_object.link_message = "Element not found, please check if you inserted wrong 'tittle attribute' or html output is updated"




#Function to find the href value by the class name,preffered two class names. check_by_value = check_by_class
def check_by_class_name(drive, the_object, req):

   try:
        name = the_object.check_by_value
        clas_name = name.split(' ')

        if(len(clas_name)==1):
            find_the_element = drive.find_element_by_xpath("//a[contains(@class, '" + clas_name[0] + "')]")

        elif(len(clas_name)==2):
            find_the_element = drive.find_element_by_xpath("//a[contains(@class, '" + clas_name[0] + "') and contains(@class, '" + clas_name[1] + "')]")
        a = find_the_element.get_attribute("href")
        a = a.split('&_ga')[0]
        if a == the_object.link_url:
                   the_object.link_url_found = a
                   the_object.http_status = gethttpstatuscode(a, req)
                   the_object.checked = "1"
                   the_object.status = "1"
                   the_object.link_message = "Link found and is equal"
        else:  
                   the_object.link_url_found = a
                   #r = req.get(the_object.link_url, stream=True)
                   the_object.http_status = "wrong"
                   the_object.checked = "1"
                   the_object.status = "2"
                   the_object.link_message = "Link found but is not equal with the one in the dataset"

   except NoSuchElementException as exception:

        the_object.link_url_found = "Selenium was not able to find the elemen, check details"
        the_object.http_status = "#"
        the_object.checked = "0"
        the_object.status = "3"
        the_object.link_message = "Element not found, please check if you inserted wrong 'Class names' or html output is updated"



#Function to find the href value by element ID name, check_by_value = check_by_link_id
def check_by_link_id(drive, the_object, req):
      try:
           find_the_element = drive.find_element_by_id(the_object.check_by_value)
           the_href = find_the_element.get_attribute("href")
           if the_href == the_object.link_url:
              the_object.link_url_found = the_href
              the_object.http_status = gethttpstatuscode(a, req)
              the_object.checked = "1"
              the_object.status = "1"
              the_object.link_message = "Link found and is equal"
           else:
             the_object.link_url_found = the_href
             #r = req.get(the_object.link_url, stream=True)
             the_object.http_status = "wrong"
             the_object.checked = "1"
             the_object.status = "2"
             the_object.link_message = "Link found but is not equal with the one in the dataset"
       
      except NoSuchElementException as exception:
          
           the_object.link_url_found = "Selenium was not able to find the elemen, check details"
           the_object.http_status = "#"
           the_object.checked = "0"
           the_object.status = "3"
           the_object.link_message = "Element not found, please check if you inserted wrong 'element id' or html output is updated"




# Function for finding the http status code
def gethttpstatuscode(link, session):
    
    
    response = session.head(link)
    code = response.status_code
    return code