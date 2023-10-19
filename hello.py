#!/usr/bin/env python3
"""Hello world mult language

Depende da Lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

    Ou informe atraves do CLI argument `--lang`

Execução:

    python3 hello.py
    ou
    ./hello.py

"""

#dunder
__version__ = "0.1.2"
__author__ = "Gabriel Victor"
__license__ = "Unlincese"

import os
import sys

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    current_language= os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a Language: ")

current_language = current_language[:5]

# sets (hash table) --> O(1) --> constante
# dicts (hash table)

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}



#Ordem complexidade O(n)
"""
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, MOndo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
"""
print(
    msg[current_language] * int(arguments["count"])
      )