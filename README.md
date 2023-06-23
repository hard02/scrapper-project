# scrapper-project
The provided Python script automates the process of downloading voter lists from the Maharashtra CEO Election website. By leveraging the requests library for making HTTP requests and the BeautifulSoup library for HTML parsing, the script enables users to conveniently retrieve voter lists for their desired district.

The script begins by launching the website and navigating to the targeted page. It locates the district dropdown form field using HTML parsing and searches for the specified district option. Upon finding the district option, the script extracts the corresponding value associated with it.

Next, the script submits the form with the selected district, using the extracted value as a form parameter. This triggers the website to process the request and return a response. The response can be further utilized for subsequent actions, depending on the specific requirements.

To complete the automation process, additional steps need to be implemented to navigate the website, select the desired constituencies, and initiate the PDF downloads. These steps should be tailored according to the structure and functionality of the website.
