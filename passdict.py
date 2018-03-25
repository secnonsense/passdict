#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, argparse
from itertools import product

fulldict={}

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--numbers", help="Substitute 0-9 for any single digit", action="store_true")
parser.add_argument("-u", "--upperlower", help="Subtitute lower/upper letters for each other", action="store_true")
parser.add_argument("-l", "--leet", help="Use leetspeak substitutions for dictionary", action="store_true")
parser.add_argument("-s", "--symbol", help="Specify a custom placeholder for symbol substitution", action="store", dest="symbol")
parser.add_argument("WORDLIST", help="Enter a wordlist and its path")
args = parser.parse_args()

leetdict = {'a': '4@', 'b': '8', 'e': '3', 'g': '6', 'h': '4', 'i': '1!', 'l': '1', 'o': '0', 's': '$5', 
't': '7', 'z': '2', 'A': '4@', 'B': '8', 'E': '3', 'G': '6', 'H': '4', 'I': '1!', 'L': '1','O': '0', 'S': '$5',
'T': '7', 'Z': '2'}

upperlowerdict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 
'i': 'I', 'j': 'J', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R','s': 'S', 
't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z', 'A': 'a', 'B': 'b','C': 'c', 
'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j','L': 'l', 'M': 'm', 'N': 'n',
'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
'Y': 'y','Z': 'z'}

symboldict = {args.symbol: '!@#$%^&*()_+=-`~;:"<>,./?\|[]\}\{\''} 

numberdict = {'1': '1234567890', '2': '1234567890', 
'3': '1234567890', '4': '1234567890', '5': '1234567890', '6': '1234567890', '7': '1234567890', '8':
'1234567890', '9': '1234567890', '0': '1234567890'}

if args.leet:
    fulldict.update(leetdict)

if args.symbol:
    fulldict.update(symboldict)

if args.upperlower:
    fulldict.update(upperlowerdict)

if args.numbers:
    fulldict.update(numberdict)


with open(args.WORDLIST) as infile:   
    data = infile.readlines()
data = [x.strip() for x in data]

def leet(inword):
    newword = [j + fulldict.get(j, "") for j in inword]
    for s in product(*newword):
        print("".join(s))

for word in data:
    leet(word)      
