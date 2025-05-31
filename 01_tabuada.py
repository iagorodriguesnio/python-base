"""
Tabuada de multiplicação do 1 ao 10
"""

__version__ = "0.1.1"
__author__ = "Iago Rodrigues"


numeros = range(1,11)

for numero in numeros:
    print("{:-^20}".format(f"Tabuada do {numero}"))
    print()

    for numero_multi in numeros:
        resultado = numero * numero_multi
        print(f"{numero} * {numero_multi} = {resultado}")

    print()
