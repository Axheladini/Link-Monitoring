#-DO NOT update, modify or change this part of the code --------------------------------
import os, sys                                                                #---------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  #---------
import language                                                               #---------
#---------------------------------------------------------------------------------------


#Create the object for the language of the pages where your important links are. 
#First parameter is The name of the language and the second parameter is the ISO 2 code of a languge/Country
lang = language.Language("Deutsch", "de")

#Create the first page with important links
#First parameter is the name of the page and the second paramenter is the link of the page
#Add first page for the given language
page_1 = language.Page("Home page", "https://de.wikibooks.org/wiki/Hauptseite")
#Add second page for the given language
page_2 = language.Page("Elektrotechnik", "https://de.wikibooks.org/wiki/Regal:Elektrotechnik")

#Assign the page to a given language. 
#this way you can assign as much pages as you wish. 
lang.push_page(page_1)
lang.push_page(page_2)

#Define important links for a given page
#Check english.py file for more instructions about the attributes
 
link1 = language.Linku("Wikibooks-Portal", "https://de.wikibooks.org/wiki/Wikibooks:Portal", "", "0", "0", "0", "check_by_parent_id", "n-portal", "")
link2 = language.Linku("Main Logo", "https://de.wikibooks.org/wiki/Hauptseite", "", "0", "0", "0", "check_by_class", "mw-wiki-logo", "")
link3 = language.Linku("Elektrotechnik", "https://de.wikibooks.org/wiki/Regal:Elektrotechnik", "", "0", "0", "0", "check_by_text", "Elektrotechnik", "")
link4 = language.Linku("Kleiner Führer zu Burgen", "https://de.wikibooks.org/wiki/Kleiner_F%C3%BChrer_zu_Burgen,_Schl%C3%B6ssern_und_Rittersitzen:_Essen_und_Umgebung", "", "0", "0", "0", "check_by_tittle", "Kleiner Führer zu Burgen, Schlössern und Rittersitzen: Essen und Umgebung", "")

#Assign each important link to page_1
page_1.push_link(link1)
page_1.push_link(link2)
page_1.push_link(link3)
page_1.push_link(link4)

#Add links for page_2
link5 = language.Linku("Kategorie:Regal", "https://de.wikibooks.org/wiki/Kategorie:Regal", "", "0", "0", "0", "check_by_tittle", "Kategorie:Regal", "")
link6 = language.Linku("Links auf diese Seite", "https://de.wikibooks.org/wiki/Spezial:Linkliste/Regal:Elektrotechnik", "", "0", "0", "0", "check_by_text", "Links auf diese Seite", "")
link7 = language.Linku("Algorithms", "https://de.wikibooks.org/wiki/Spezial:Spezialseiten", "", "0", "0", "0", "check_by_text", "Spezialseiten", "")
link8 = language.Linku("Wikimedia Foundaition", "https://wikimediafoundation.org/", "", "0", "0", "0", "check_by_parent_id", "footer-copyrightico", "")
link9 = language.Linku("Mediawiki", "https://www.mediawiki.org/", "", "0", "0", "0", "check_by_parent_id", "footer-poweredbyico", "")


#Assign each important link to page_2
page_2.push_link(link5)
page_2.push_link(link6)
page_2.push_link(link7)
page_2.push_link(link8)
page_2.push_link(link9)