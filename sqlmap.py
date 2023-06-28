"___Author___=@Miguellpz9"
import os
website = raw_input("Enter website: ")

def scan(url, options):
    command = "sqlmap -u " + url + options + " "
    process = os.popen(command)
    results = str(process.read())
    return results
print (scan(website, " "))

