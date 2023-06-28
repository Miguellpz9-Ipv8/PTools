import subprocess

def execute_program(option):
    if option == '1':
        subprocess.call(['python3', 'GetIP.py'])
    elif option == '2':
        subprocess.call(['python3', 'robots.py'])
    elif option == '3':
        subopt = input("Would you like to use (1)custom scanner or (2)nmap")
        if subopt == '1':
            subprocess.call(['python', 'prtscn.py'])
        elif subopt == '2':
            subprocess.call(['python', 'atnmap.py'])
    elif option == '4':
        subprocess.call(['python3', 'sqlmap.py'])
    elif option == '5':
        subprocess.call(['python', 'whois.py'])
    elif option == '6':
        subprocess.call(['python3', 'revshl.py'])
    # Add more options as needed
    else:
        print("Invalid option!")

def display_menu():
    print(" ")
    print("Github: https://github.com/miguellpz9-ipv8")
    print("*" * 69)
    print("Multi-use script to perform various tasks for web-penetration testing.")
    print("*" * 69)
    print("Select an option:\n")
    print("	1. Get target IP")
    print("	2. scan robots.txt")
    print("	3. scan ports(custom)")
    print("	4. sqlmap")
    print("	5. whois")
    print("	6. WinReverseShell")
    # Add more options as needed
    print("0. Exit")

def main():
    while True:
        display_menu()
        option = input("Enter your choice (0 to exit): ")
        if option == '0':
            break
        execute_program(option)

if __name__ == '__main__':
    main()

