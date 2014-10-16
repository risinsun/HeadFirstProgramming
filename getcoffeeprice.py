__author__ = 'risinsun'

import urllib

def get_title():
    page = urllib.urlopen("http://www.google.com")
    text = page.read()#.decode("utf8")
    title_index = text.find("<title>")
    end_index = text.find("</title>")
    title = text[title_index + 7 : end_index]

    print(title)

get_title()