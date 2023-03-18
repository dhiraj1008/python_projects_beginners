# web scriping-> geting or extracting particular data from website..!
# we need two libraries 1)request(is used for sending the data) and
#  2)beautiful soup(bs4)(is used to filter our data)
# 3)lxml (parser library)
# pip install requests bs4 lxml
# Requests is an HTTP library, written in Python, for human beings. Basic GET usage:
# tp://www.crummy.com/software/BeautifulSoup/

"""Beautiful Soup uses a pluggable XML or HTML parser to parse a (possibly invalid) document 
into a tree representation. Beautiful Soup provides methods and Pythonic idioms that make it easy 
to navigate, search, and modify the parse tree.
"""
import requests
from bs4 import BeautifulSoup

# url to which u need to send the request
url = "https://www.codewithtomi.com/"

#send the request if the return status code is 200 then request is successfully sent

r = requests.get(url)

soup = BeautifulSoup(r.content,'lxml')

# tell python what we are looking for ,i mean what data from the website we need ..
title = soup.find_all('h2',{'class':'post-title'})
print("scriping sub titles of the website:")
for t in title:
   print(t.getText())




