
"""
Hello World Multi Linguas

Dependendo da linguagem configurada no ambiente o programa exibe a correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex: 
   
    export LANG=pt_BR

Execução: 

    python main.py

"""
__version__ = "0.0.1"
__author__ = "Iago Rodrigues"
__license__ = "Unlicense"

current_language = "en_US"

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)