import os
import re

list1 = []

xs = os.listdir()

for x in xs:
    list1.append(x)

padrao = re.compile(r'\.\w+$')

spam = set()

for list0 in list1:
    asd = padrao.search(list0)
    if not asd == None:
        aguia = asd.group()
        mw = aguia.replace(".","")
        if mw.isalpha() or mw == 'mp4':
            spam.add(mw)