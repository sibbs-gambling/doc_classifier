import re
import sys

# Function defs

buffersize = 10000
buff_count = 0
counter = 0
y_dict = dict()
for line in sys.stdin:
    tokenint = line.split("|")

    if counter==0:
        prev_key = tokenint[0]
    if prev_key != tokenint[0]:
        buff_count = 0
        for key, count in y_dict.items():
            print('{}{}'.format(key, "|" + str(count)))
        y_dict = dict()

    prev_key = tokenint[0]
    counter += 1
    buff_count += 1

    y_dict[tokenint[0]] = y_dict.get(tokenint[0], 0) + int(tokenint[1])




