import re

def tokenizeDoc(cur_doc):
    return re.findall(’\\w+’,cur_doc)