# LinkMonitoring

Automated tool for monitoring important links for any website or web app.
Current version is available only for windows machines. I want to convert it for Linux and Mac but it will take some times :) 

This is my first tool build with Python. If anyone finds any issue or a way to optimis feel free to contribute. 

In general LinkMonitoirng is a tool that helps for monitoring and controlling if important links of your website or any other 
web app  are working as expected. Actually, it's a pre or post deployment tool to check and control automatically your important links. Following the trend of DevOps and having in mind that human testings are not very effective, we tend to automate as much as we can. LinkMonitoirng tests a given link two times, at first it checks if a link is available at a given position (within DOM) for a specific page and then it checks for the http request status of the same link. 

## How it works

At first, you create a dataset with links that you need to test. There is no user interface for importing your important links with the current version, therefore you will need to add important links as python objects ( Check Usage section ). Python by using Selenium with headless chrome (browser) points to each page where we have our important links, finds each important link by using one out of four functions: check_by_parent_id, check_by_text, check_by_tittle, check_by_class, check_by_link_id. The link found is compared with the one in the dataset and at the end Python checks for the HTTP request code of the link. After all links are visited and controlled the tool  generates an in detail html report with the results for each link.

## Usage

1. If Python is not installed at your machine, dowanload it from <a href="https://www.python.org/downloads/">www.python.org/downloads/</a> . I have installed Python 3.6

2. Selenium uses chrome browser in headless mode to point to each page and find all links. Therefore, you will need to download the chromdriver.exe version based on your chrome browser version. Click on this <a href="https://chromedriver.chromium.org/" target="_blank">link</a> and download the version corresponding to your chrome browser. Copy the exe file to “C:\linkmonitoring\chromedriver.exe” (this path is important because the tool expects it exactly in this location).

3. Pull, clone or download the repository from GitHub <a href="https://github.com/Axheladini/Link-Monitoring" target="_blank">Link</a> The tool comes with pre-filed data (important links dataset) from altervista.org pages.
At this step from cmd point to your local repository and run the command:
<p></p> 
<b><i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;python index.py</i></b> 
<br>
<p></p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If Python is installed correctly the tool will start to monitor and controll all important links from the dataset. 


## Importing your important links ( the dataset)

1. This is the most important step, defining your dataset with important links. At this point, it is an advantage if you have object oriented programming knowledge and skills but I will try to explain the whole process in details so any WebDev, DevOps or Webmaster can understand it.

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