# LinkMonitoring / Python + Selenium

Automated tool for monitoring important links for any website or web App<br>
This tool is useful for websites with high traffic, important business processes and important content which are updated at least once a day. On my daily work it monitors over 500 important links, execution time around 3 mins. We have incorporated it with Jenkins and the whole monitoring proccess is automated.

Current version is available only for windows machines. I have a plan to convert it for Linux and Mac but as usual it will take some time :) 

This is my first tool build with Python. If anyone finds issues or a way to optimise the code feel free to comment and  contribute. 

In general LinkMonitoring is a tool that helps for monitoring and controlling if important links of your website or any other 
web App are at a given place and working as expected. Actually, it's a pre or post deployment tool to check and control automatically your important links. Following the trend of DevOps and having in mind that human testings are not very effective we tend to automate as much as we can. LinkMonitoring checks a given link two times at first it checks if a link is available at a given position (within DOM) for a specific page and then it checks for the HTTP request status of the same link.  

## How it works

At first, you create a dataset with links that you need to monitor. There is no user interface for importing your important links, therefore you will need to add important links as python objects ( Check Usage section ). Python by using Selenium with headless chrome (browser) points to each page where we have our important links, finds each important link by using one out of four functions: <i><b>check_by_parent_id</b></i>, <i><b>check_by_text</b></i>, <i><b>check_by_tittle</b></i>, <i><b>check_by_class</b></i>, <i><b>check_by_link_id</b></i>. The link found is compared with the one in the dataset and afterwards Python checks for the HTTP request code of the link. When all links are visited and controlled the tool generates detailed HTML report with results for each link.

## Usage

1. If Python is not installed at your machine, dowanload it from <a href="https://www.python.org/downloads/">www.python.org/downloads/</a>, make sure you install PIP also. On my local machine i am using Python 3.6. After installing Python you will need to install these Python modules: 

* python -m pip install selenium
* python -m pip install requests
* python -m pip install urllib3


2. Selenium uses chrome browser in headless mode to point to each page and find all links of corresponding page. Therefore, you will need to download the chromdriver.exe based on your chrome browser version. Click <a href="https://chromedriver.chromium.org/" target="_blank">https://chromedriver.chromium.org/</a> and download the version related to your chrome browser. Copy the exe file to “<b>C:\linkmonitoring\chromedriver.exe</b>” ( this path is important because the tool expects it exactly there ).

3. Pull, clone or download the repository from GitHub <a href="https://github.com/Axheladini/Link-Monitoring" target="_blank">https://github.com/Axheladini/Link-Monitoring</a> The tool comes with pre-filed data (important links dataset) from wikibooks.org pages.
At this step from cmd point to your local repository and run the command:
<p></p> 
<b><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python index.py</i></b> 
<br>
<p></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>If Python is installed correctly the tool will start to monitor and controll all important links from the dataset. At the end the detailed HTML report will show up.</i> 


## Importing your important links ( the dataset )

1. This is the most important step, defining your dataset with important links. At this point it is an advantage if you have object oriented programming knowledge and skills but I will try to explain the whole process in details so any WebDev, DevOps or Webmaster can understand it. 

<i>Before going into details please check english.py and deutsch.py files under websites directory, the whole dataset logic is within these files.</i> 

* The whole dataset of important link is under websites directory.
* Do not update, change or modify __init__.py and config.py files, these are important files for the tool to run.
* I always create a separate dataset file for each language of the website. As you can see inside websites directory I have created engllish.py and deutsch.py. You can name these files as you wish but you must follow one convention: use only letters and no special characters (like: *&^%$#@!~_+-?/).
* Each dataset file should have the header code where some modules are imported. (Check the line that starts with DO NOT on english.py file).<br>
2. Create the object for the language of the pages where your important links are. First parameter is The name of the language and the second parameter is the ISO 2 code of a language/Country: 
    
    ```python
    lang = language.Language("English", "en")
    ```

3. Create the first page with important links. First parameter is the name of the page and the second parameter is the link of the page: 

    ```python
    page_1 = language.Page("Home page", "https://en.wikibooks.org/wiki/Main_Page")
    ```

4. Assign the page to the language:

    ```python
    lang.push_page(page_1)
    ```
5. This way you can add as much as you want pages for a given language or websites.
6. Define important links for a given page.

    ```python
     link1 = language.Linku("Featured Books", "https://en.wikibooks.org/wiki/Wikibooks:Featured_books", "", "0", "0", "0", "check_by_parent_id", "n-Featured-books", "")
    ```

###### Repeat this for all-important links that are present on page_1.  * 2nd, 7nth and 8th attributes you will need to find them within the source code of the page where your important links are
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Attributes:</b> 
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 1</b> – Link name / Add the link name<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 2</b> – link URL / Add the URL of the link (complete link including the https://)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 3</b> – Link that will be added by tool / Leave it empty<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 4</b> – http status of the link, added by LinkMonitoring / Initial value 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 5</b> – checked, 1 or 0 shows if link has been controlled or not, LinkMonitoring updates the value / Initial value 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 6</b> – status, 1 or 0 shows the status of the link, 1 if no errors and 0 if there is some error / Initial value 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 7</b> – LinkMonitoring has five functions which are helping on finding the URL of the link. Which value to add <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; depends on how your links are constructed. Available values: <i>check_by_parent_id</i>, <i>check_by_text</i>, <i>check_by_tittle</i>,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>check_by_class</i>, <i>check_by_link_id</i>

####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. check_by_parent_id
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```html <li id="parent_id"><a href="https://www.somedomain/somepath/">Link text</a></li> ```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkMonitoring will find and test the link based on parent id, in our example its <b>parent_id</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. check_by_text

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```html <p><a href="https://www.somedomain/somepath/">Sample</a></p>```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkMonitoring will find and test the link based on <b>link text</b> in this example its <b>Sample</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Check_by_tittle
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```html <p><a href="https://www.somedomain/somepath/" title="Some Link title">Link text</a></p>```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkMonitoring will find and test the link based on <b>title</b> attribute in this example is <b>Some Link title</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. check_by_class
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```html <p><a href="https://www.somedomain/somepath/" class="class_name_one class_name_two">
Link text</a></p>```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example, LinkMonitoring will find and test the link based on <b>class name</b>. Having in mind that CSS classes <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;are not unique, I would suggest adding two classes when you use <b>check_by_class</b> function to find the link.</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. check_by_link_id

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```html <p><a href="https://www.somedomain/somepath/" id="link_main_id">
Link text</a></p>```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example, LinkMonitoring will find and test the link based on <b>element id</b>. Current example: <b>link_main_id</b>

###### * Suggestion: If the way that the links are presented on the web depends on you, I would suggest adding unique id names or unique title attributes because these two functions can find the link in faster and better way.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 8</b> – This attribute depends from Attribute 7. You will need to find this value in the source code based on the function you will use on Attribute 7 (Check above examples)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 9</b> – Leave this empty, this field is used from LinkMonitoring to add details based on link status.<br>

6. Connect each important link with corresponding page :
     
     ```python
     page_1.push_link(link1)
     ```

Complete code on this stage for english.py would look like this: :

```python
#create the language object
lang = language.Language("English", "en") 

#create the object of the first page where important links are*
page_1 = language.Page("Home page", "https://en.wikibooks.org/wiki/Main_Page")

#push this page to language object
lang.push_page(page_1)

#create the first important link object
link1 = language.Linku("Featured Books", "https://en.wikibooks.org/wiki/Wikibooks:Featured_books", "", "0", "0", "0", "check_by_parent_id", "n-Featured-books", "")

#Assign first important link object to the first page
page_1.push_link(link1)
```

6. After you have added all pages and important links by repeating all sub steps on cmd point to your local repository and run the command: <b>python index.py</b> the automated process will start. The execution time will depend on the number of links. When the process will end a nice HTML report will show up with details for each link. Do not forget to update the dataset when you update or remove some important link from your website.

## Contributing

If you decide to try or use this tool in your daily work, I would really appreciate if you use the Issues page to add your suggestions, experiences, review comments etc. 
Also feel free to contribute for improving, adding new features etc. 

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

LinkMonitoring 1.0

## Credits

Agon Xheladini 
www.agonxheladini.com 

## License

FOSS