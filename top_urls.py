#!/usr/bin/env python
import requests
import sys
from bs4 import BeautifulSoup

BASE_URL='http://www.alexa.com/topsites/%s'


def generate_request_url(argv):

    formed_url = BASE_URL % ""

    if len(argv) > 1:
        # TODO: Argument for the Help
        request_type = sys.argv[1].lower()
        if request_type == 'category':
            category_type = argv[2]
            formed_url = BASE_URL % "category/Top/" + category_type

        elif request_type == 'countries':
            country_code = argv[2].upper()
            formed_url = BASE_URL % "countries/" + country_code

    return formed_url

if __name__ == '__main__':

    request_url = generate_request_url(sys.argv)
    response = requests.get(request_url)

    soup = BeautifulSoup(response.text, 'html5lib')
    table = soup.find_all(class_="listings table")
    site_listing = table[0].find_all(class_="tr site-listing")

    delimiter = ','
    for index in range(len(site_listing)):
        rank = site_listing[index].find(class_="td number").get_text()
        description = site_listing[index].find(class_="td DescriptionCell")
        url = site_listing[index].select(".DescriptionCell p a")[0].get_text()
        print('%s%s%s' % (rank, delimiter, url.lower()))
