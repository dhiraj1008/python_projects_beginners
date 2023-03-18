# site connectivity checker 
# import urlib
# use   urlib.request (An extensible library for opening URLs using a variety of protocols) 
# write a function that takes url
# return response or print the response

import urllib.request as urllib

def main(url):
    print("checking connectivity ")
    response1 = urllib.urlopen(url) 
    print("Connect to ",url," successfully")
    print("The reponse cod was :",response1.getcode())


print("This is a site connectivity checker program ")
url = input("enter the url :\n")
main(url)