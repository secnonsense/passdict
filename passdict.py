#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, argparse
from itertools import product

parser = argparse.ArgumentParser()
#parser.add_argument("-v", "--malware", help="Use known bad User Agent malware", action="store_true")
#parser.add_argument("-o", "--openvas", help="Use known bad User Agent OpenVAS", action="store_true")
#parser.add_argument("-z", "--meterpreter", help="Use known hacking tool User Agent Meterpreter", action="store_true")

#parser.add_argument("-f", "--save", help="Save the body to a file", action="store_true")
#parser.add_argument("-p", "--proxy", help="Specify the IP address and port of proxy - 127.0.0.1:8080", action="store", dest="proxy")
parser.add_argument("-s", "--symbols", help="Specify a custom placeholder for symbol substitution", action="store", dest="symbol")
parser.add_argument("WORDLIST", help="Enter a wordlist and its path")
args = parser.parse_args()

leetdict = {'a': '4@A', 'b': '8B', 'c': 'C', 'd': 'D', 'e': '3E', 'f': 'F', 'g': '6G', 'h': '4H', 
'i': '1!I', 'j': 'J', 'l': '1L', 'm': 'M', 'n': 'N', 'o': '0O', 'p': 'P', 'q': 'Q', 'r': 'R','s': '$5S', 
't': '7T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': '2Z', 'A': 'a4@', 'B': 'b8','C': 'c', 
'D': 'd', 'E': 'e3', 'F': 'f', 'G': 'g6', 'H': 'h4', 'I': 'i1!', 'J': 'j','L': 'l1', 'M': 'm', 'N': 'n',
'O': 'o0', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's$5', 'T': 't7', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
'Y': 'y','Z': 'z2', args.symbol: '!@#$%^&*()_+=-`~;:"<>,./?\|[]\}\{\'', '1': '1234567890', '2': '1234567890', 
'3': '1234567890', '4': '1234567890', '5': '1234567890', '6': '1234567890', '7': '1234567890', '8':
'1234567890', '9': '1234567890', '0': '1234567890'}

with open(args.WORDLIST) as infile:   
    data = infile.readlines()
data = [x.strip() for x in data]

def leet(inword):
    newword = [j + leetdict.get(j, "") for j in inword]
    for s in product(*newword):
        print("".join(s))

for word in data:
    leet(word)      
