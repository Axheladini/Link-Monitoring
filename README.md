# LinkMonitoring

Automated tool for monitoring important links for any website or web app.
Current version is available only for windows machines and I am planning to convert it to Linux and Mac as soon as I can. 

This is my first tool build with Python. If anyone finds any issue or a way to optimis feel free to contribute. 

In general LinkMonitoirng is a tool that helps for monitoring and controlling if important links of your website or any other 
web app  are working as expected. Actually, it's a pre or post deployment tool to check and control automatically your important links. Following the trend of DevOps and having in mind that human testings are not very effective, we tend to automate as much as we can. LinkMonitoirng tests a given link two times, at first it checks if a link is available at a given position (within DOM) for a specific page and then it checks for the http request status of the same link. 

## How it works

At first, you create a dataset with links that you need to test. There is no user interface for importing your important links with the current version, therefore you will need to add important links as python objects ( Check Usage section ). Python by using Selenium with headless chrome (browser) points to each page where we have our important links, finds each important link by using one out of four functions: check_by_parent_id, check_by_text, check_by_tittle, check_by_class, check_by_link_id. The link found is compared with the one in the dataset and at the end Python checks for the HTTP request code of the link. After all links are visited and controlled the tool  generates an in detail html report with the results for each link.

## Installation

1. If you

## Usage

TODO: Write usage instructions

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