
__version__ = "0.1.3"
__author__ = "Iago Rodrigues"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    key, value = arg.split("=")
    key = key.strip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value
        

current_language = arguments["lang"]

if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else: 
        current_language = input("Escolha um Idioma: ")

current_language = current_language[:5]

msg =  {
     "en_US": "Hello, World",
     "pt_BR": "Olá Mundo!",
     "it_IT": "Ciao, Mondo!",
     "es_SP": "Hola, Mundo!",
     "fr_FR": "Bonjour, Monde!",
}
 

print(msg[current_language] * int(arguments["count"]))
