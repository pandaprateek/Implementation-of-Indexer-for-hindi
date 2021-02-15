import os
import re
import sys
import time

# list of  stop words  #

stopwords=['अत', 'अपना', 'अपनी', 'अपने', 'अभी', 'अंदर', 'आदि', 'आप', 'इत्यादि', 'इन ', 'इनका', 'इन्हीं', 'इन्हें', 'इन्हों', 'इस', \
           'इसका', 'इसकी', 'इसके', 'इसमें', 'इसी', 'इसे', 'उन', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हीं', 'उन्हें', 'उन्हों', 'उस', \
           'उसके', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'ऐसे', 'और', 'कई', 'कर', 'करता', 'करते', 'करना', 'करने', 'करें', 'कहते', \
           'कहा', 'का', 'काफ़ी', 'कि', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर', 'किस', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', \
           'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा', 'जितना', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', \
           'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थी', 'थे', 'दबारा', 'दिया', \
           'दुसरा', 'दूसरे', 'दो', 'द्वारा', 'न', 'नके', 'नहीं', 'ना', 'निहायत', 'नीचे', 'ने', 'पर', 'पहले', 'पूरा', 'पे', 'फिर', 'बनी', \
           'बही', 'बहुत', 'बाद', 'बाला', 'बिलकुल', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यही', 'या', 'यिह', \
           'ये', 'रखें', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वग़ैरह', 'वर्ग', 'वह', 'वहाँ', 'वहीं', 'वाले', 'वुह', 'वे', \
           'सकता', 'सकते', 'सबसे', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'संग', 'ही', 'हुआ', 'हुई', 'हुए', 'है', 'हैं', \
           'हो', 'होता', 'होती', 'होते', 'होना', 'होने', '']

#---- Indexer Creation-------#

from collections import Counter
from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input


#------------ Parshing Text-------------------#

content={}
def parsetexts(fileglob='C:\\Users\\Prateek\\Documents\\NLP Assignment\\inputFiles\\*.txt'):
    texts = {}
    words=[]
    for txtfile in glob(fileglob):
        per_file_words=[]
        arr=[]
        f=open(txtfile, encoding='utf-8-sig')
        txt = f.read()
        arr=txt.split("।")
        for i in arr:
            i=i.replace(',','')
            i=i.replace('.','')
            i=i.replace('!','')
            i=i.replace(')','')
            i=i.replace('(','')
            i=i.replace('"','')
            i=i.replace('\'','')
            per_file_words=per_file_words+ i.strip().strip('"').split()
        per_file_words = list(set(per_file_words))
        per_file_words =list(set(per_file_words)-set(stopwords))
        per_file_words=stem_terms(per_file_words)
        filename= txtfile.split('\\')[-1]
        texts[filename] = per_file_words
        words = words + per_file_words
    return texts, list(set(words))


def termsearch(terms):
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))


# print('\nWords')
# pp(sorted(words))

# print('\nInverted Index')
# pp({k:sorted(v) for k,v in invindex.items()})


def search_inv_idx(phrase):
    # phrase = '"चुपचाप कुएँ में मिट्टी डालते रहे"'
    global texts, words, invindex, intmd_res
    it_str = ''
    result = []
    start = time.clock()
    texts, words = parsetexts()
    invindex = {word: set(txt for txt, wrds in texts.items() if word in wrds) for word in words}
    query_terms = phrase.strip().strip('"').split()
    query_terms = list(set(query_terms) - set(stopwords))
    query_terms = stem_terms(query_terms)
    intmd_res = list(termsearch(query_terms))
    for i in intmd_res:
        it_str = it_str + i + '\n'

    print('\nTerm Search on full inverted index for: ' + repr(query_terms))
    pp(sorted(termsearch(query_terms)))
    result.append("===========================================================")
    result.append("\n\n\n-------सामान्य खोज के परिणाम---------------\n\n")
    result.append("परिणाम प्राप्त करने के लिए " + "  " + str(round(time.clock() - start, 4)) + "s " + "का समय लिया गया")
    result.append(it_str)
    return result
def main():
print("\t\t\t चलो खोज करें\t\t\t\t")
query=input("आप क्या खोजना चाहते हैं")
query=f'"{query}"'
print(query)
search_inv_idx(query)
main()
search_inv_idx()