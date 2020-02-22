<p align="center">
  <img src="https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/AAP%20Finder%20Logo.png" alt="AAP Finder Logo"/>
</p>

<h1 align="center">AAP Finder</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3-green.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/aapfinder/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/Technowlogy-Pushpender/aapfinder">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
  </a>
    <img src="https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20osx-lightgrey.svg">
  </a>    
</p>

                        This small python script can do really awesome work.
                        

AAP Finder (Advanced Admin Page Finder) is a tool written in Python3 with advanced functionalities, with more than **550+ Potential Admin Panels**. This Tool Can Easily Find Login Pages of Any Site & is also capable to detect *robots.txt* File.

## Features
- [x] Have more than **550+ Potential Admin Panels**
- [x] **MultiThreaded** 
- [x] Able to BruteForce Subdomain LoginPages i.e **login.target.com, admin.target.com, etc**
- [x] Large Dictionary
- [x] Supports Both **HTTP** & **HTTPS** 
- [x] BruteForce Multiple Domains at a time
- [x] Stops Scan when Valid LoginPage is found
- [x] Supports PHP, ASP and HTML extensions
- [x] Checks for **robots.txt**
- [x] Supports Custom Dictionary
- [x] Targets can be passed to this tool via File
- [x] Able to detect **EAR** (Execute After Redirect) **Vulnerability**
- [x] Saves the Scan with a Neat & Clean UI in a file
- [ ] Self Update [**Coming Soon**]
- [ ] Scan Via Tor & Proxy [**Coming Soon**]
- [ ] Random-Proxy [**Coming Soon**]
- [ ] Random-UserAgent [**Coming Soon**]

## Tools Overview
| Front View | Sample Feature	|
| ------------  | ------------ |
|![Index](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/AAP%20Finder1.PNG)|![f](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/AAPFinder2.PNG)

## Prerequisite
- [x] Python 3.X


## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - 2019.4**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/)](https://www.microsoft.com) **Windows 8,7,10**

## Installation

#### Linux
```

# Navigate to the /opt directory (optional)
$ cd /opt/

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/aapfinder.git

# Navigate to aapfinder folder
$ cd aapfinder

# Installing dependencies
$ apt-get update && apt-get install python3

# Give Executable Permission
$ chmod +x aapfinder.py

# Run it
$ python3 aapfinder.py --help

```

#### Windows
```
# Download & Extract 

# Navigate to aapfinder Directory
$ cd aapfinder

# Run it using python3
$ python okadminfinder.py
```

#### PentestBox
```
# Exactly Same Procedure as Linux Installation

# Create Alias by adding this Line to C://Pentestbox/bin/customtools/customaliases file
 aapfinder=py -3 "%pentestbox_ROOT%/bin/Path/to/aapfinder/aapfinder.py
 
# So you'll be able to launch it using: aapfinder
```

## Available Arguments 
* Optional Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
| -h          | --help    | show this help message and exit |
| -u TARGET   | --url TARGET | Specify Target URL of Website. |
| -d DELAY | --delay DELAY | Specify Delay In Seconds after each Login Url Test. |
|  -c PATH | --custom PATH | Specify Absolute Path of Custom Dictionary.|
| -f | --fast    |    Use MultiThreading to Boost The Speed of Scan. |
| | --targets TARGETS_FILE | Scan Multiple Targets. |
| -o OUTPUT | --output OUTPUT | Save a Neat Result of Scan. |

* Required Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
|  -t TYPE | --type TYPE |  Set The Type i.e html, asp, php.|


## Screenshots

#### Description : Adding Custom Potential Admin Panels Via File
#### Command Example : python3 aapfinder.py -u https://target.com **--custom my_dict.txt** -t php

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Add_Custom_Dictionary.PNG)


#### Description : Adding Multiple Targets Via File
#### Command Example : python3 aapfinder.py **--targets my_targets.txt** -t php 

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Scan_Targets_from_file.PNG)

#### Description : Saving Result In a File
#### Command Example : python3 aapfinder.py -u https://target.com **--output result.txt** -t php

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Add_Custom_Dictionary.PNG)

#### Description : Saved Result

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Saved_Result.PNG)

#### Description : Able to Find Subdomain Login Panels

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Subdomain_LoginPage.PNG)

![](https://github.com/Technowlogy-Pushpender/aapfinder/blob/master/img/Subdomain_LoginPage1.PNG)

## Contribute

* All Contributors are welcome, this repo needs contributors who will improve this tool to make it best.

## Contact

singhpushpender250@gmail.com 

## More Features Coming Soon...
