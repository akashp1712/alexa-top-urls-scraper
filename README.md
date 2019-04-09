# Alexa_top_urls_scraper
Scrap the urls from the Alexa website (Parsing HTML Template as of April 2017)

This script will scrap the content from the Alexa (http://www.alexa.com/topsites) and fetch the top URLs.
Alexa provides two options to see the urls 1.category and 2.countries.
It provides 50 urls for free(demo) in each category/sub-category and country.


requirements: Python 2.7 and libraries: BeautifulSoup, html5lib


<b>Usage:</b>
> python top_urls.py [category|country] [<category_tyoe>|<country_code>]


example of usage:
1. Using country<br /> 
  ```> python top_urls.py country US```

2. Using category<br /> 
  ```> python top_urls.py category Arts```

  - using subcategory<br /> 
    ```> pytohn top_urls.py category Arts/Animation```

3. Default<br /> 
  ```> python top_urls.py```
  ```# This will print the top 50 websites of the world.```


<b>TODO:</b>
 1. Method to populate all the subcategory for the given category
 2. Method to populate all the available country codes.
