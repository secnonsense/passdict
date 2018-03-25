# passdict

Python script for generating custom password dictionaries

usage: passdict.py [-h] [-n] [-u] [-l] [-s SYMBOL] WORDLIST

positional arguments:
  WORDLIST              Enter a wordlist and its path (Example: /users/joe/words.txt)

optional arguments:

  -h, --help            - show this help message and exit
  
  -n, --numbers         - Substitute 0-9 for any single digit appearing in the words from the wordlist
  
  -u, --upperlower      - Subtitute lower/uppercase letters for each other
  
  -l, --leet            - Use leetspeak substitutions in the generated dictionary
  
  -s SYMBOL, --symbol SYMBOL - Specify a custom placeholder for symbol substitution and substitute symbols
                        
