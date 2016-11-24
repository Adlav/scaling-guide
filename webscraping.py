from bs4 import BeautifulSoup
from urllib2 import urlopen

base = raw_input("Please insert website link:")

def make_soup(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    return soup


def cat_links(url):
    el1 = raw_input("Navigation element:")
    class1 = raw_input("Navigation class:")
    el2 = raw_input("Link element:")
    class2 = raw_input("Link class:")
    soup = make_soup(base)
    cats = soup.find(el1, class1)
    links = [base + i["href"] for i in cats.findAll(el2, class2)]
    return links

links = cat_links(base)

def product(lst):
    Cel = raw_input("Container Element:")
    Cclass = raw_input("Container Class:")
    el3 = raw_input("Element 1:")
    class3 = raw_input("Class 1:")
    el4 = raw_input("Element 2:")
    class4 = raw_input("Class 2:")
    for url in lst:
        soup = make_soup(url)
        container = soup.find(Cel, Cclass)
        x1 = [x.string for x in container.find(el3, class3)]
        x2 = [basic.string for basic in container.find(el4, class4)]
    return {"Name": x1, "Element": x2}

print product(links)
