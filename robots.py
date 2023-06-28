import urllib.request
import io
import certifi

website = input("Enter target URL (include https://) : ")
def robots_pathway(url):
    if url.endswith("/"):
    	path = url
    else:
    	path = url + "/"
    	rqst = urllib.request.urlopen(path + "robots.txt", cafile=certifi.where())
    	data = io.TextIOWrapper(rqst, encoding="utf-8")
    return data.read()
print (robots_pathway(website))

