# https://www.youtube.com/watch?v=d5jHpPSp5uI&ab_channel=egoroff_channel
# https://pythobyte.com/python-create-json-44caee86/

import json
import openpyxl

book = openpyxl.open("English.xlsx", read_only=True)
sheet = book.active


kek = {'a': {},
       'b': {},
       'c': {},
       'd': {},
       'e': {},
       'f': {},
       'g': {},
       'h': {},
       'i': {},
       'j': {},
       'k': {},
       'l': {},
       'm': {},
       'n': {},
       'o': {},
       'p': {},
       'q': {},
       'r': {},
       's': {},
       't': {},
       'u': {},
       'v': {},
       'w': {},
       'x': {},
       'y': {}
       }


for k in range(1, 1001):
    key = sheet[k][0].value
    val = sheet[k][1].value
    kek[key[0].lower()][key] = val

# jsonString = json.dumps(kek, indent=4, ensure_ascii=False)

print(kek)

with open('dictionary.json', 'w', encoding="utf-8") as outfile:
    json.dump(kek, outfile, ensure_ascii=False)
