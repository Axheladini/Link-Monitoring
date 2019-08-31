class Language():

       
    def __init__(self, languageName, languageCode):

        self.name = languageName
        self.code = languageCode
        self.pages = []
        
    def push_page(self, page):      
        self.pages.append(page)

class Page():
      def __init__(self, name, link):
          self.name = name
          self.link = link
          self.links = []
          
      def push_link(self, link):
          self.links.append(link)

class Linku():

      def __init__(self, link_text, link_url, link_url_found, http_status, checked, status, check_by, check_by_value, link_message):

          self.link_text = link_text
          self.link_url = link_url
          self.link_url_found = link_url_found
          self.http_status = http_status
          self.checked = checked
          self.status = status
          self.check_by = check_by
          self.check_by_value = check_by_value
          self.link_message = link_message

       
      









        
    
