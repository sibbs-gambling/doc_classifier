import re
import json
import fileinput

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
y_dict = dict()  # Hashtable for incrementing
# *                 --> key for count of test instances
# <label_j>         --> key for count of label_i
# <label_j token_j> --> key for count of label_j label_j combinations
# <label_j *>       --> key for count of all tokens in instances with label i

for line in fileinput.input():
    tokenlist = tokenizeDoc(line)

    # Increment labels
    y_dict['*'] = y_dict.get('*', 0) + 1
    curr_labels = []  # bin for labels in instance j
    firstw_loc = findFirstW(tokenlist)
    for jlabel in tokenlist[0:(firstw_loc-1)]:
        if jlabel[-3:]=="CAT":  # Only care about labels ending in "CAT"
            y_dict[jlabel] = y_dict.get(jlabel, 0) + 1
            curr_labels.append(jlabel)

    # Increment tokens
    for jtoken in tokenlist[firstw_loc:]:
        for jlabel in curr_labels:  # sub-loop needed because there can be multiple labels
            key = jlabel + ' ' + jtoken
            y_dict[key] = y_dict.get(key, 0) + 1

    for jlabel in curr_labels:
        y_dict[jlabel + ' ' + '*'] = y_dict.get(jlabel + ' ' + '*', 0) + len(tokenlist[firstw_loc:])

# Saves data
dict_save = json.dumps(y_dict)
f = open("dict.txt", 'a')
f.write(dict_save)
f.close()

