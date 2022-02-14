import os
import pandas as pd
import re
from string import punctuation
from killing_orthography import kill_orthography

voc = pd.read_csv('voc.csv', sep = '\t')
def lemmatize(line):
    linewords = []
    for word in line.split():

        wl = voc[voc['sort'] == kill_orthography(word.strip(punctuation))]
        #print(wl)
        if len(set(wl['lex']))>=1:
            linewords.append(list(wl['lex'])[0])
        else:
            linewords.append(word)
    text_lem = (' '.join(linewords))
    return text_lem
#print(kill_orthography("де́лех"))
#print(lemmatize("Го́споди Бо́же наш, Вели́кий в сове́те и ди́вный в де́лех, всея́ тва́ри Соде́телю"))