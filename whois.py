import os
import sys

url = raw_input("Enter URL to resolve: ")

def whos(url):
    command = "whois " + url
    process = os.popen(command)
    results = process.read()
    return results
    
print (whos(url))
