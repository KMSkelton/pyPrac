import requests
from bs4 import BeautifulSoup

def geturl():
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Canada"
    return url

# Create a function that allows you to pull out a tag (passed as an argument to your function) from any URL
# (also passed as an argument to your function)

def soup_function(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    return soup

def url_input(url,tag):
    soup = soup_function(url)
    lines = soup.find_all(tag)
    return lines


def meaningful_url_input(lines):
    mystuff=[]
    for line in lines:
        li_tag=line.find("li")
        if li_tag is not None:
            print(li_tag)
            mystuff.append(str(li_tag))
    return mystuff



def write_to_text(mystuff):
    with open('output.txt','w') as f:
        f.write(str(mystuff))


# Create a function that allows you to pull out a tag (passed as an argument to your function) from any URL
# (also passed as an argument to your function)
url=geturl()

myfunction = url_input(url, "div")
#print(myfunction)


# Create a function to format the output in a meaningful way
meaningful_output = meaningful_url_input(myfunction)
print(meaningful_output)


# Create a function to write the formatted results to a txt file
txt_file=write_to_text(meaningful_output)
