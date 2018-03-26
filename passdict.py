#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from itertools import product

fulldict={}
template=[]
lowyear=1950
highyear=2019
ksymbol=''


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--template", help="Specify a custom template for all words of your wordlist.  ", action="store", dest="template")
parser.add_argument("-n", "--numbers", help=" Substitute 0-9 for any single digit appearing in the words from the wordlist", action="store_true")
parser.add_argument("-u", "--upperlower", help="Subtitute lower/uppercase letters for each other", action="store_true")
parser.add_argument("-l", "--leet", help="Use leetspeak substitutions in the generated dictionary", action="store_true")
parser.add_argument("-s", "--symbol", help="Specify a custom placeholder for symbol substitution and substitute symbols", action="store", dest="symbol")
parser.add_argument("WORDLIST", help="Enter a wordlist and its path")
args = parser.parse_args()

if args.symbol:
    ksymbol=args.symbol

leetdict = {'a': '4@', 'b': '8', 'e': '3', 'g': '6', 'h': '4', 'i': '1!', 'l': '1', 'o': '0', 's': '$5', 
't': '7', 'z': '2', 'A': '4@', 'B': '8', 'E': '3', 'G': '6', 'H': '4', 'I': '1!', 'L': '1','O': '0', 'S': '$5',
'T': '7', 'Z': '2'}

upperlowerdict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 
'i': 'I', 'j': 'J', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R','s': 'S', 
't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z', 'A': 'a', 'B': 'b','C': 'c', 
'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j','L': 'l', 'M': 'm', 'N': 'n',
'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
'Y': 'y','Z': 'z'}

symboldict = {ksymbol: '!@#$%^&*()_+=-`~;:"<>,.\/?|[]{}\''} 

numberdict = {'1': '1234567890', '2': '1234567890', '3': '1234567890', '4': '1234567890', '5': '1234567890',
'6': '1234567890', '7': '1234567890', '8': '1234567890', '9': '1234567890', '0': '1234567890'}

if args.upperlower:
    fulldict.update(upperlowerdict)

if args.leet and args.upperlower:
    for key, value in leetdict.iteritems():
       if fulldict.get(key, None):
            fulldict[key]=value+fulldict[key]

elif args.leet and not args.upperlower:
    fulldict.update(leetdict)

if args.symbol:
    fulldict.update(symboldict)

if args.numbers:
    fulldict.update(numberdict)


with open(args.WORDLIST) as infile:   
    data = infile.readlines()
data = [x.strip() for x in data]

def leet(inword):
    newword = [j + fulldict.get(j, "") for j in inword]
    for s in product(*newword):
        if args.template:
            template=args.template.split('+')
            loc = template.index("WORD")
            template[loc] = ("".join(s))
            if "YYYY" in template:
                idx = template.index("YYYY")
                for YYYY in range(lowyear, highyear): 
                    template[idx] = str(YYYY)
                    print("".join(template))  
                
        else:    
            print("".join(s))

for word in data:
    leet(word)      
