
__version__ = "0.0.1"
__author__ = "Iago Rodrigues"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")


msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"

if current_language == "it_IT":
    msg = "Ciao, Mondo!"

if current_language == "es_SP":
    msg = "Hola, Mundo!"

if current_language == "fr_FR":
    msg = "Bonjour, Monde!"

print(msg)
