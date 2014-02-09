# -*- coding: iso-8859-1 -*-

# Name:             Project 1
# Purpose:          CSC 4243
# Author:           Benjamin K Guitreau
# Copyright:
# Licence:          GPL

# OS dev:           Windows 7 & Funtoo Linux
# Python dev:       2.7
# Revision:         1.00

# Dependencies:     Python 2.7 32-bit, Beautiful Soup 4

from bs4 import BeautifulSoup
import urllib2
from sets import Set

def getSource(url):
        url = urllib2.urlopen(url)
        source = url.read()
        return source

def scrapeStart():
    recipes = []
    default_dict = {}

    base_url = "http://allrecipes.com/"
    long_url = "search/default.aspx?qt=k&wt=Gumbo&rt=r&origin=Search%20Results&vm=l&p34=SR_ListView&hb=80"
    real_url = base_url + long_url
    source = getSource(real_url)

    soup = BeautifulSoup(source)

    for link in soup.find_all('a'):
        a = str(link.get('href'))
        if len(a) < 28:
            pass
        elif a[:29] == "http://allrecipes.com/recipe/":
            val = a.find("/de")
            b = a[29:val]
            if b.find("/reviews") != -1:
                pass
            else:
                recipes.append(b)
        else:
            pass
    recipes = sorted(set(recipes))

    for obj in recipes:
        key = obj
        value = []
        value.append("http://allrecipes.com/Recipe/")
        value.append(obj)
        value.append("/Detail.aspx")
        val = ''.join(value)
        default_dict[key] = val

    return default_dict
