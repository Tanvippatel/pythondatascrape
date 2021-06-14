
import re


str = 'Date: 2004 - 2010'

chunks = re.split('[:-]',str)

for chunk in chunks:
    print(chunk)

