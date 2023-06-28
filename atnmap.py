import sys
import os

IP = raw_input("Enter IP to scan: ")
print "*" * 69
def whos(IP):
    option = str(input("Would you like to perform a (1)regular scan or (2)full scan?"))
    if option == '1':
        command = "nmap -sV " + IP
    elif option == '2':
        command = "nmap -p- -sV " + IP
    process = os.popen(command)
    results = process.read()
    return results

print (whos(IP))
