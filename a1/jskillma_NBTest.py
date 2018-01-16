import re
import fileinput
import json
import math

# Function defs
def tokenizeDoc(cur_doc):
    return re.findall('\\w+',cur_doc)

def anyLower(str):
    for c in str:
        if c.islower():
            return(True)
    return(False)

def findFirstW(lst):
    for stri in lst:
        if anyLower(stri):
            return(lst.index(stri))
    return(0) # if no real words were found

# Main routine
f = open("dict.txt", 'r')
dict_save = f.read()
f.close()
y_dict = json.loads(dict_save)

f = open("answers.txt", 'a', newline='\n')
for line in fileinput.input():
    tokenlist = tokenizeDoc(line)

    prob_dict = dict()
    firstw_loc = findFirstW(tokenlist)
    for jlabel in tokenlist[0:(firstw_loc-1)]:
        if jlabel[-3:]=="CAT":  # Only care about labels ending in "CAT"
            y_dict[jlabel] = y_dict.get(jlabel, 0) + 1
            prob_dict[jlabel] = prob_dict.get(jlabel, 0) +\
                                math.log(y_dict[jlabel]/y_dict['*'])
        else:
            continue
        for jtoken in tokenlist[firstw_loc:]:
            prob = 1
            if jtoken in y_dict:
                print(math.log((y_dict[jlabel + ' ' + jtoken] +
                                (1/len(tokenlist[firstw_loc:]))) / 1 + y_dict[jlabel + ' ' + '*']))
                prob_dict[jlabel] = prob_dict.get(jlabel, 0) + prob
    if not prob_dict:
        continue
    max_label = max(prob_dict, key=prob_dict.get)
    writeline = '[' + ",".join(tokenlist[0:(firstw_loc - 1)]) + ']' + '   ' + str(max_label) + '   ' + str(prob_dict[max_label])
    f.write(writeline + '\n')

f.close()


