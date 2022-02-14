import os
import pandas as pd
import re
os.chdir(input("Введите адрес папки:"))

with open(input("Введите название файла:"), 'r', encoding = 'utf8') as file:
    file = file.readlines()
voc = pd.read_csv('new_full_vocabulary.csv', sep = '\t')
text_spl = ''
for line in file:
    linewords = []
    for word in line.split():
        wl = voc[voc['sort'] == word]
        if len(set(wl['lex']))>=1:
            linewords.append(list(wl['lex'])[0])
        else:
            linewords.append(word)
    text_spl += (' '.join(linewords))+'\n'

with open(input("Введите название лемматизированного файла:"), 'w', encoding = 'utf8') as sl:
    sl.write(text_spl)