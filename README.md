# LinkMonitoring

Automated tool for monitoring important links for any website or web app.
Current version is available only for windows machines. I want to convert it for Linux and Mac but it will take some times :) 

This is my first tool build with Python. If anyone finds any issue or a way to optimis feel free to contribute. 

In general LinkMonitoirng is a tool that helps for monitoring and controlling if important links of your website or any other 
web app  are working as expected. Actually, it's a pre or post deployment tool to check and control automatically your important links. Following the trend of DevOps and having in mind that human testings are not very effective, we tend to automate as much as we can. LinkMonitoirng tests a given link two times, at first it checks if a link is available at a given position (within DOM) for a specific page and then it checks for the http request status of the same link. 

## How it works

At first, you create a dataset with links that you need to test. There is no user interface for importing your important links with the current version, therefore you will need to add important links as python objects ( Check Usage section ). Python by using Selenium with headless chrome (browser) points to each page where we have our important links, finds each important link by using one out of four functions: <i><b>check_by_parent_id</b></i>, <i><b>check_by_text</b></i>, <i><b>check_by_tittle</b></i>, <i><b>check_by_class</b></i>, <i><b>check_by_link_id</b></i>. The link found is compared with the one in the dataset and at the end Python checks for the HTTP request code of the link. After all links are visited and controlled the tool  generates an in detail html report with the results for each link.

## Usage

1. If Python is not installed at your machine, dowanload it from <a href="https://www.python.org/downloads/">www.python.org/downloads/</a> . I have installed Python 3.6

2. Selenium uses chrome browser in headless mode to point to each page and find all links. Therefore, you will need to download the chromdriver.exe version based on your chrome browser version. Click on this <a href="https://chromedriver.chromium.org/" target="_blank">link</a> and download the version corresponding to your chrome browser. Copy the exe file to “<b>C:\linkmonitoring\chromedriver.exe</b>” (this path is important because the tool expects it exactly in this location).

3. Pull, clone or download the repository from GitHub <a href="https://github.com/Axheladini/Link-Monitoring" target="_blank">Link</a> The tool comes with pre-filed data (important links dataset) from altervista.org pages.
At this step from cmd point to your local repository and run the command:
<p></p> 
<b><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python index.py</i></b> 
<br>
<p></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>If Python is installed correctly the tool will start to monitor and controll all important links from the dataset.</i> 


## Importing your important links ( the dataset)

1. This is the most important step, defining your dataset with important links. At this point, it is an advantage if you have object oriented programming knowledge and skills but I will try to explain the whole process in details so any WebDev, DevOps or Webmaster can understand it. 
<i><br>Before going into details and reading bellow steps please check english.py and deutsch.py files under websites directory, the whole dataset logic is within these files.</i> 

    * The whole dataset of important link is under websites directory.
    * Do not update, change or modify __init__.py and config.py files, these are important files for the tool to run.
    * I always create a separate dataset file for each language of the website for which I need to test important links. If you can see inside websites directory I have created engllish.py, deutsch.py … You can name these files as you wish but you must follow one convention: use only letters, no special characters (like: *&^%$#@!~_+-?/).
    * Each dataset file should have the header code where some modules are imported. (Check the line that starts with DO NOT on english.py file).

2. Create the object for the language of the pages where your important links are. First parameter is The name of the language and the second parameter is the ISO 2 code of a language/Country: 

    `lang = language.Language("English", "en")`


3. Create the object for the language of the pages where your important links are. First parameter is The name of the language and the second parameter is the ISO 2 code of a language/Country: 

    `page_1 = language.Page("Home page", "https://en.wikibooks.org/wiki/Main_Page")`

4. Assign the page to the language:

    `lang.push_page(page_1)`

5. This way you can add as much as you want pages for a given language or websites.
6. Define important links for a given page.

    `link1 = language.Linku("Featured Books", "https://en.wikibooks.org/wiki/Wikibooks:Featured_books", "", "0", "0", "0", "check_by_parent_id", "n-Featured-books", "")`

###### Repeat this for all-important links that are present on page_1.  * 2nd, 7nth and 8th attributes you will need to find them inside the source code of the page where your important links are
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 1</b> – Link name / Add the link name
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 2</b> – link URL / Add the URL of the link (complete link including the https://)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 3</b> – Link that will be added by linkChecker / Must stay empty
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 4</b> – http status of the link, added by linkChecker adds it / Add 0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 5</b> – checked, 1 or 0 shows if link has been controlled or not, LinkChecker updates the value / Add 0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 6</b> – status, 1 or 0 shows the status of the link, 1 if it passes all the tests and 0 if there is some issue / Add 0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b>Attribute 7</b> – LinkMonitoring has five functions which help on finding the URL of the link. What value to add here<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; depends on how your links are constructed. Available values: <i>check_by_parent_id</i>, <i>check_by_text</i>, <i>check_by_tittle</i>,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i>check_by_class</i>, <i>check_by_link_id</i>

####  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. check_by_parent_id
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li id="parent_id"><a href="https://www.somedomain/somepath/">Link text</a></li>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkChecker will find and control the link based on parent id, in our example its <b>parent_id</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. check_by_text

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<p><a href="https://www.somedomain/somepath/">Sample</a></p>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkChecker will find and control the link based on <b>link text</b> in this example its <b>Sample</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Check_by_tittle
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<p><a href="https://www.somedomain/somepath/" title="Some Link title">Link text</a></p>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example LinkChecker will find and control the link based on <b>title</b> attribute in this example is <b>Some Link title</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. check_by_class
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<p><a href="https://www.somedomain/somepath/" class="class_name_one class_name_two">
Link text</a></p>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example, LinkChecker will find and control the link based on <b>class name</b>. Having in mind that CSS classes are not unique, I would suggest adding two classes when you use <b>check_by_class</b> function to find the link.</b>

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. check_by_link_id

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DOM block example:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<p><a href="https://www.somedomain/somepath/" id="link_main_id">
Link text</a></p>`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example, LinkChecker will find and control the link based on <b>element id</b>. Current example: <b>link_main_id</b>

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license