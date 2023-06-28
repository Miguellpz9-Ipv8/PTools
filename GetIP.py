import os

website = input("Enter target URL: ")
def Get_IP (url):
    cmnd = "host " + url
    procs = os.popen(cmnd)
    reslt = str(procs.read())
    mark = reslt.find("has address") + 12
    return reslt[mark:].splitlines()[0]
print (Get_IP(website))

