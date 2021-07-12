#!/usr/bin/python3

import requests, threading, argparse, socket, time, os, banners

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def get_arguments():
    banners.get_banner()  # Banner of This Tool
    parser = argparse.ArgumentParser(description=f'{RED}AAPFinder v1.0')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("-u", "--url", dest="target", help="Specify Target URL of Website.")  
    parser.add_argument("-d", "--delay", dest="delay", help="Specify Delay In Seconds after each Login Url Test.")
    parser.add_argument("-c", "--custom", dest="path", help="Specify Absolute Path of Custom Dictionary.")
    parser.add_argument("-f", "--fast", dest="threading", help="Use MultiThreading to Boost The Speed of Scan.", action="store_true")
    parser.add_argument("--targets", dest="targets_file", help="Scan Multiple Targets.")
    parser.add_argument("-o", "--output", dest="output", help="Save a Neat Result of Scan.")
  
    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("-t", "--type", dest="type", help="Set The Type i.e html, asp, php.")

    return parser.parse_args()

def check_internet_connection():
    print(f"\n{YELLOW}[*] Checking Your Internet Connection ...")
    REMOTE_SERVER = "www.google.com"
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()
        print(f"{GREEN}[+] We Are Connected to Internet : )")
        print("[!] Type python3 aapfinder.py -h or --help")
        
    except Exception:
        print(f"{RED}[!] Your are Offline Please Connect to Internet :(")
        print(f"{YELLOW}[*] Exting ...")
        quit()

def extract_target_from_file(targets_file):
    targets_list = []
    with open(targets_file, 'r') as f:
        tar_list = f.readlines()
        for target in tar_list:
            if target.strip() == "":
                pass
            else:
                targets_list.append(str(target.strip()))
    return targets_list            
                           
def set_protocal(url):
    url = url.replace('www.', '') #Removing "www." from url so we have "target.com" and not "www.target.com"
    protocal = None

    if url[:7] == "http://":
        protocal = "HTTP"
        target_url = url
        print(f"{GREEN}[+] Using Protocal : HTTP")        
    elif url[:8] == "https://":
        protocal = "HTTPS"
        target_url = url
        print(f"{GREEN}[+] Using Protocal : HTTPS")          
    else:
        while(protocal == None):
            choice = input(f"{WHITE}[?] Which Protocal You Want To Use i.e (1)HTTP or (2)HTTPS: (1/2): ") 
            if choice == "1":
                protocal = "HTTP"
                target_url = "http://" + url
                print(f"{GREEN}[+] Using Protocal : HTTP")
            elif choice == "2":
                protocal = "HTTPS"
                target_url = "https://" + url
            else:
                print(f"{RED}[!] Invalid Input, Please Try Again!")
   
    return target_url
    
def check_robots_file(target_url):
    try:
        print(f"\n{YELLOW}[*] Checking robots.txt File ...")
        r = requests.get(target_url + '/robots.txt') #Requests to target.com/robots.txt
        if '<html>' in r.text: # If there's an html error page then its not robots.txt
            print(f'{RED}[!] 404 not found: robots.txt')
        else:
            print(f'{GREEN}[+] Robots.txt Found. Check for any interesting entry')
            print(f"{YELLOW}\n[****************************************************************]\n")
            print(r.text)
            print(f"{YELLOW}\n[****************************************************************]\n")            
    except Exception as e:
        print(f'{RED}[!] Exception Raised While Checking robots.txt | Error : {e}')  

def get_paths(type, wordlist='wordlist.txt'):
    try:
        with open(wordlist,'r') as wordlist: # Opens wordlist.txt & grabs links according to the type arguemnt
            for path in wordlist:
                path = str(path.replace("\n",""))
                try:
                    if 'asp' in type:
                        if 'html' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'php' in type:
                        if 'asp' in path or 'html' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'html' in type:
                        if 'asp' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                except:
                    paths.append(path)
    except IOError:
        print(f"{RED}[!] Wordlist not found!")
        quit()

def subdomain_login_scan(target_url):
    subdomain_result = "Subdomain LoginPage NOT FOUND"
    if arguments.delay == None:
        delay = 0
    else:
        delay = arguments.delay

    if os.path.exists("wordlist_subdomain.txt"):
        final_path_list = []
        with open("wordlist_subdomain.txt", "r") as f:
            total_paths = f.readlines()
            for path in total_paths:
                if path.strip() == "":
                    pass
                else:
                    final_path_list.append(str(path.strip()))
                
        if target_url[:7] == "http://":
            target_url = target_url[7:]
            target_url = "http://" + "subdomain." + target_url

        elif target_url[:8] == "https://":
            target_url = target_url[8:]
            target_url = "https://" + "subdomain." + target_url  
        
        print(f"{GREEN}[*] Initiating Subdomain LoginPage Scan, Total URL to be Checked : {len(final_path_list)}")
        print(f"{YELLOW}[=================================================================================]")
        total_looping = len(final_path_list)
        link_index = 0
        while(total_looping != 0):
            link = target_url.replace("subdomain.", final_path_list[link_index]+".")
            try:
                r = requests.get(link)
                http = r.status_code
                if http == 200: # If its 200 the url points to valid resource i.e. admin panel
                    print(f"{GREEN}[+] Admin panel found: {link}")
                    subdomain_result = link
                    choice = input(f"{WHITE}[?] Want to Continue Scan for Finding EAR (Execution After Redirect) vulnerability ? (y/n): ")
                    if choice.lower() == "n":
                        break
                    elif choice.lower() == "y":
                        continue
                elif http == 404: #404 means not found
                    print(f"[-] 404 NOT FOUND : {link}")
                elif http == 302: #302 means redirection
                    print(f"[+] Found Potential EAR vulnerability : {link}")
            except:
                print(f"[-] 404 NOT FOUND : {link}")
                
            link_index += 1
            total_looping -= 1
            
            time.sleep(int(delay)) 
        
        print(f"{YELLOW}[=================================================================================]")
        
    else:
         print(f"{RED}\n[!] 404 NOT FOUND : {WHITE}wordlist_subdomain.txt")
         print(f"{YELLOW}[*] Skipping Subdomain LoginPage Scan i.e {WHITE}login.target.com")
        
    return subdomain_result

def start_scanning(links, target_url):
    result = "AdminPanel NOT FOUND"
    if arguments.delay == None:
        delay = 0
    else:
        delay = arguments.delay

    total_looping = len(links)
    link_index = 0
    while(total_looping != 0):  
        link = target_url + links[link_index]
        r = requests.get(link)
        http = r.status_code
        if http == 200: # If its 200 the url points to valid resource i.e. admin panel
            print(f"{GREEN}[+] Admin panel found: {link}")
            result = link
            choice = input(f"{WHITE}[?] Want to Continue Scan for Finding EAR (Execution After Redirect) vulnerability ? (y/n): ")
            if choice.lower() == "n":
                break
            elif choice.lower() == "y":
                continue
        elif http == 404: #404 means not found
            print(f"[-] 404 NOT FOUND : {link}")
        elif http == 302: #302 means redirection
            print(f"[+] Found Potential EAR (Execution After Redirect) vulnerability : {link}")
            
        link_index += 1
        total_looping -= 1
        
        time.sleep(int(delay))  

    return result

def create_result_file(output_file_name):
    with open(output_file_name, "w") as f:
        f.write("[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]\n")
        f.write("   SCAN RESULT  - Created BY AAPFinder (Advanced AdminPage Finder)\n") 
        f.write("              AUTHOR      : Pushpender Singh\n") 
        f.write("              TOOL NAME   : AAPFinder\n") 
        f.write("              WRITTEN IN  : Python 3\n") 
        f.write("[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]\n")
        if arguments.threading:
            f.write("\n\tScan Type : Fast (Using Thread)")        
        else:
            f.write("\n\tScan Type : Normal (Without Using Thread)")
        f.write(f"\n\tCustom Dictionary : {arguments.path}") 
        
def save_result(output_file_name, target, result, subdomain_result):
    with open(output_file_name, "a") as f:
        f.write(f"\n\n\tTarget : {target}")  
        f.write(f"\n\tScan Result : {result}") 
        f.write(f"\n\tSubdomain LoginPage Scan Result : {subdomain_result}") 

if __name__ == '__main__':
    arguments = get_arguments()    
    
    if arguments.target and arguments.targets_file:
        print(f"\n{RED}[!] Either Specify URL or TargetsFile, Not Both!")
        print(f"{YELLOW}[*] Type --help to see Manual Guide")
        quit()
    
    check_internet_connection()
    
    # Scanning targets one by one for --targets flag
    if arguments.targets_file:
        if arguments.output:   # If Output Flag is given, Create Result Template file
            create_result_file(arguments.output)
            
        targets_list = extract_target_from_file(arguments.targets_file)
        for target in targets_list:
            print(f"{YELLOW}[Target] : {WHITE}{target}")
        print(f"\n{YELLOW}[*] Scanning One at a Time ...")
    
        for target in targets_list:
            try:        
                target_url = set_protocal(target)
                if target_url[len(target_url)-1:] == "/":
                    target_url = target_url[:-1] #Removing "/" from url so we have "target.com" and not "target.com/"

                print(f"{GREEN}[+] Target URL : {WHITE}{target_url}")
                 
                check_robots_file(target_url)

                paths = [] # List of paths (URL) 
                if arguments.path:
                    print(f"{YELLOW}[*] Adding Custom URLs In Path List")
                    if os.path.exists(arguments.path):
                        get_paths(arguments.type, arguments.path)
                        print(f"{GREEN}[+] Added Successfully\n")
                    else:
                        print(f"{RED}[!] Your Custom Dictionary does not exist! Using Default Dict.\n")
                    
                get_paths(arguments.type) 
                                 
                subdomain_result = subdomain_login_scan(target_url)
                
                if arguments.threading == True:  # Checking, If MultiThreading Is Enabled
                    print(f"\n{GREEN}[*] Initiating Scan, Total Admin URL to be Checked : {len(paths)}")
                    print(f"{YELLOW}[=================================================================================]")
                    paths1 = paths[:int(round(len(paths)/2))]
                    paths2 = paths[int(round(len(paths)/2)):]
                    def scan_part1():
                        result = start_scanning(paths1, target_url)
                    def scan_part2():
                        result = start_scanning(paths2, target_url) 
                    t1 = threading.Thread(target=scan_part1) # Calling scan_part1() Function via Thread
                    t2 = threading.Thread(target=scan_part2) # Calling scan_part2() Function via Thread
                    t1.start()
                    t2.start()
                    t1.join()
                    t2.join()
                        
                else:  # Else, do normal scan, without thread 
                    print(f"\n{GREEN}[*] Initiating Scan, Total Admin URL to be Checked : {len(paths)}")
                    print(f"{YELLOW}[=================================================================================]") 
                    result = start_scanning(paths, target_url)    
                    print(f"{YELLOW}[=================================================================================]")
            
            except KeyboardInterrupt:
                print(f"\n{YELLOW}[*] Exting ... CTRL + C Detected")

        if arguments.output:
            save_result(arguments.output, target_url, result, subdomain_result)            
            
    
    # Scanning target for --url flag
    elif arguments.target:
        try: 
            if arguments.output:   # If Output Flag is given, Create Result Template file
                create_result_file(arguments.output)
                
            target_url = set_protocal(arguments.target)
            if target_url[len(target_url)-1:] == "/":
                target_url = target_url[:-1] #Removing "/" from url so we have "target.com" and not "target.com/"

            print(f"{GREEN}[+] Target URL : {WHITE}{target_url}")
             
            check_robots_file(target_url)

            paths = [] # List of paths (URL) 
            if arguments.path:
                print(f"{YELLOW}[*] Adding Custom URLs In Path List")
                if os.path.exists(arguments.path):
                    get_paths(arguments.type, arguments.path)
                    print(f"{GREEN}[+] Added Successfully\n")
                else:
                    print(f"{RED}[!] Your Custom Dictionary does not exist! Using Default Dict.\n")
                    
            get_paths(arguments.type) 
            
            subdomain_result = subdomain_result = subdomain_login_scan(target_url)
            
            if arguments.threading == True:  # Checking, If MultiThreading Is Enabled
                print(f"\n{GREEN}[*] Initiating Scan, Total Admin URL to be Checked : {len(paths)}")
                print(f"{YELLOW}[=================================================================================]")
                paths1 = paths[:int(round(len(paths)/2))]
                paths2 = paths[int(round(len(paths)/2)):]
                def scan_part1():
                    result = start_scanning(paths1, target_url)
                def scan_part2():
                    result = start_scanning(paths2, target_url) 
                t1 = threading.Thread(target=scan_part1) # Calling scan_part1() Function via Thread
                t2 = threading.Thread(target=scan_part2) # Calling scan_part2() Function via Thread
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                    
            else:  # Else, do normal scan, without thread 
                print(f"\n{GREEN}[*] Initiating Scan, Total Admin URL to be Checked : {len(paths)}")
                print(f"{YELLOW}[=================================================================================]") 
                result = start_scanning(paths, target_url)    
                print(f"{YELLOW}[=================================================================================]")
        
        except KeyboardInterrupt:
            print(f"\n{YELLOW}[*] Exting ... CTRL + C Detected")

        if arguments.output:
            save_result(arguments.output, target_url, result, subdomain_result)         
    
