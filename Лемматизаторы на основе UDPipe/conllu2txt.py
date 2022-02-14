import conllu
import os

os.chdir("C:\\Users\\Arseny\\Desktop\\Лемматизаторы\\Лемматизаторы на основе UDPipe")

test_conllu = 'russian_church_slavonic.conllu'


with open(test_conllu, 'r', encoding='utf8') as file:
	conllu_text = file.read()

sentences_conllu = conllu.parse(conllu_text)

words = []

for s in sentences_conllu:
	print(s)
	for w in s:
		words.append(list(w.values())[1])



with open ('russian_church_slavonic.txt', 'w', encoding='utf8') as file:
	file.write(" ".join(words))