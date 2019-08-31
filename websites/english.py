#-DO NOT update, modify or change this part of the code --------------------------------
import os, sys                                                                #---------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #---------
import language                                                               #---------
#---------------------------------------------------------------------------------------


#Create the object for the language of the pages where your important links are. 
#First parameter is The name of the language and the second parameter is the ISO 2 code of a languge/Country
lang = language.Language("English", "en")

#Create the first page with important links
#First parameter is the name of the page and the second paramenter is the link of the page
#Add first page for the given language
page_1 = language.Page("Home page", "https://en.wikibooks.org/wiki/Main_Page")
#Add second page for the given language
page_2 = language.Page("Department:Computing", "https://en.wikibooks.org/wiki/Department:Computing")

#Assign the page to a given language. 
#this way you can assign as much pages as you wish. 
lang.push_page(page_1)
lang.push_page(page_2)

#Define important links for a given page
#
# * 2nd, 7nth and 8th attributes you will need to find them inside the source code of the page where your important links are 
#
# Attribute 1 = Link name 
# Attribute 2 = link url 
# Attribute 3 = Link that will be found from linkChecker / It should stay empty
# Attribute 4 = http status of the link found linkchecker adds it / Add 0 
# Attribute 5 = checked, 1 or 0 shows if link has been controlled or not, LinkChecker updates the value / Add 0
# Attribute 6 = status, 1 or 0 shows the status of the link, 1 if it passes all the tests and 0 if there is some issue / Add 0 
# Attribute 7 = LinkChecker has 5 functions which help on finding the url of the link. Which one to use depends on the way your links are constructud.
#               Available values: check_by_parent_id, check_by_text, check_by_tittle, check_by_class, check_by_link_id
#
#
#				1 - check_by_parent_id
#                   html block example: <li id="parent_id"><a href="https://www.somedomain/somepath/">Link text</a></li>
#                   In this example LinkChecker will find and control the link based on parent id which in our example is  parent_id
#				2 - check_by_text
#                   html block example: <p><a href="https://www.somedomain/somepath/">Link text</a></p>
#                   In this example LinkChecker will find and control the link based on linl text in this example it is Link text 
#				3 - check_by_tittle
#                   html block example: <p><a href="https://www.somedomain/somepath/" title="Some Link title">Link text</a></p>
#                   In this example LinkChecker will find and control the link based on title attribute in this example it's Some Link title 
#				4 - check_by_class
#                   html block example: <p><a href="https://www.somedomain/somepath/" class="class_name_one class_name_two">Link text</a></p>
#                   In this example LinkChecker will find and control the link based on class name. Having in mind that  css classes can be used more than once in your source code 
#                   I would suggest to add two classes when you use this function to find the link.
#				5 - check_by_link_id
#                   html block example: <p><a href="https://www.somedomain/somepath/" id="id_of_the_link">Link text</a></p>
#                   In this example LinkChecker will find and control the link based on the id of the link in this example we have id_of_the_link
#
#    * Suggestion: If the way how the links are represented on the web depends on you i would suggest to add unique id names or 
#      unique title atttribues because those two functions can find the link in faster way. 
#
# Attribute 8 = This attribute depends from  Attribute 7. You will need to find this value in the source code based on the function you will use on Attribute 7 (Check above examples)
# Attribute 9 = Leave this empty, this field is used from linkChecker to add details based on link status. 


link1 = language.Linku("Featured Books", "https://en.wikibooks.org/wiki/Wikibooks:Featured_books", "", "0", "0", "0", "check_by_parent_id", "n-Featured-books", "")
link2 = language.Linku("Main Logo", "https://en.wikibooks.org/wiki/Main_Page", "", "0", "0", "0", "check_by_class", "mw-wiki-logo", "")
link3 = language.Linku("Engineering", "https://en.wikibooks.org/wiki/Department:Engineering", "", "0", "0", "0", "check_by_text", "Engineering", "")
link4 = language.Linku("Reading room", "https://en.wikibooks.org/wiki/Wikibooks:Reading_room", "", "0", "0", "0", "check_by_tittle", "Discuss Wikibooks-related questions and concerns with others", "")

#Assign each important link to page_1
page_1.push_link(link1)
page_1.push_link(link2)
page_1.push_link(link3)
page_1.push_link(link4)

#Add links for page_2
link5 = language.Linku("Category: Book:Wikibooks Stacks/Departments", "https://en.wikibooks.org/wiki/Category:Book:Wikibooks_Stacks/Departments", "", "0", "0", "0", "check_by_tittle", "Category:Book:Wikibooks Stacks/Departments", "")
link6 = language.Linku("Ada Programming", "https://en.wikibooks.org/wiki/Ada_Programming", "", "0", "0", "0", "check_by_text", "Ada Programming", "")
link7 = language.Linku("Algorithms", "https://en.wikibooks.org/wiki/Algorithms", "", "0", "0", "0", "check_by_text", "Algorithms", "")
link8 = language.Linku("Wikimedia Foundaition", "https://wikimediafoundation.org/", "", "0", "0", "0", "check_by_parent_id", "footer-copyrightico", "")
link9 = language.Linku("Mediawiki", "https://www.mediawiki.org/", "", "0", "0", "0", "check_by_parent_id", "footer-poweredbyico", "")


#Assign each important link to page_2
page_2.push_link(link5)
page_2.push_link(link6)
page_2.push_link(link7)
page_2.push_link(link8)
page_2.push_link(link9)