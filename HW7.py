'''
* Create a function that allows you to pull out a tag (passed as an argument to your function)
from any URL (also passed as an argument to your function)
* Create a function to format the output in a meaningful way
* Create a function to write the formatted results to a txt file
'''

import requests
from bs4 import BeautifulSoup


def get_response(url):
    response = requests.get(url)
    dir(response)
    return response

def parse_response(response):
    content = response.content
    soup = BeautifulSoup(content, "lxml")
    return soup

# def format_response(soup):
#     all_td = soup.find_all("td")
#     for city in all_td:
#         city_info = city.find("a")
#         if city_info:
#          name = city_info.string
#         city_dict[name] = city_info
#         set(city_dict)
#     return city_dict

def format_response(soup):
    all_a = soup.find_all("a")
    for a in all_a:
        if a is not None:
            name = a.string
            data_dict[name] = a.get('href')
            set(data_dict)
    return data_dict

def make_txt(cities):
    with open('canada_cities.txt', "w") as outfile:
        for name, link in cities.items():
            outfile.writelines(f" name: {name}, link: {link}")
            outfile.write('\n')

if __name__ == "__main__":
    # url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Canada'
    url = input("Which page would you like to scrape? ")
    data_dict = {}
    response = get_response(url)
    soup = parse_response(response)
    data = format_response(soup)
    output = make_txt(data)