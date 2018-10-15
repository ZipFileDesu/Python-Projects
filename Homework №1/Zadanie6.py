from collections import Counter
from collections import defaultdict
import operator
import re
import os

def SplitTxt(x):
    return re.split(r'\W', re.sub(r'[-!\"#$%&\'()*+,./:;<=>?@[\\\]_\`{|}~[0-9\]]', '', x))

def CntWords(x):
    return Counter(x)

list_files = ("file" + str(i) + ".txt" for i in range (1,6))

for i in range(0,5):
    file = open(next(list_files), 'r')
    d = defaultdict(dict)
    words = SplitTxt(file.read())
    d[file.name] = CntWords(words).most_common()
    print ("Name Of Readable File: " + file.name + '\n' * 2 + 
            '\n'.join(map(str,d[file.name])) + '\n' * 2)
    None if (i == 4) else os.system("pause")