#! /usr/bin/env python3
"""
 Multiplas Línguas

"""
__version__ = "0.0.1"
__author__  = "Iago Rodrigues"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"



if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"
elif current_language == "es_SP":
    msg = "Hola, Mundo"
elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print(msg) 

#if __name__ == "__main__":
 #   main()


