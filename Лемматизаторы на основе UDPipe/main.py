# This file is part of UDPipe <http://github.com/ufal/udpipe/>.
#
# Copyright 2016 Institute of Formal and Applied Linguistics, Faculty of
# Mathematics and Physics, Charles University in Prague, Czech Republic.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import conllu
import ufal.udpipe
import os
import argparse
# ufal.udpipe.Model etc. are SWIG-magic and cannot be detected by pylint
# pylint: disable=no-member

class Model:
    def __init__(self, path):
        """Load given model."""
        self.model = ufal.udpipe.Model.load(path)
        if not self.model:
            raise Exception("Cannot load UDPipe model from file '%s'" % path)

    def tokenize(self, text):
        """Tokenize the text and return list of ufal.udpipe.Sentence-s."""
        tokenizer = self.model.newTokenizer(self.model.DEFAULT)
        if not tokenizer:
            raise Exception("The model does not have a tokenizer")
        return self._read(text, tokenizer)

    def read(self, text, in_format):
        """Load text in the given format (conllu|horizontal|vertical) and return list of ufal.udpipe.Sentence-s."""
        input_format = ufal.udpipe.InputFormat.newInputFormat(in_format)
        if not input_format:
            raise Exception("Cannot create input format '%s'" % in_format)
        return self._read(text, input_format)

    def _read(self, text, input_format):
        input_format.setText(text)
        error = ufal.udpipe.ProcessingError()
        sentences = []

        sentence = ufal.udpipe.Sentence()
        while input_format.nextSentence(sentence, error):
            sentences.append(sentence)
            sentence = ufal.udpipe.Sentence()
        if error.occurred():
            raise Exception(error.message)

        return sentences

    def tag(self, sentence):
        """Tag the given ufal.udpipe.Sentence (inplace)."""
        self.model.tag(sentence, self.model.DEFAULT)

    def parse(self, sentence):
        """Parse the given ufal.udpipe.Sentence (inplace)."""
        self.model.parse(sentence, self.model.DEFAULT)

    def write(self, sentences, out_format):
        """Write given ufal.udpipe.Sentence-s in the required format (conllu|horizontal|vertical)."""

        output_format = ufal.udpipe.OutputFormat.newOutputFormat(out_format)
        output = ''
        for sentence in sentences:
            output += output_format.writeSentence(sentence)
        output += output_format.finishDocument()

        return output

os.chdir("C:\\Users\\Arseny\\Desktop\\Лемматизаторы\\Лемматизаторы на основе UDPipe")
def main(args):

	ocs_model = "old_church_slavonic-proiel-ud-2.5-191206.udpipe"
	oes_model = "old_russian-torot-ud-2.5-191206.udpipe"

	test_text = args.text
	test_conllu = args.conllu
	current_model = args.model

	with open (test_text, 'r', encoding = 'utf8') as file:
	    text = file.read()

	model = Model(current_model)
	sentences = model.tokenize(text)
	for s in sentences:
	    model.tag(s)
	    model.parse(s)
	conllu_txt = model.write(sentences, "conllu")

	with open ('latest_result.conllu', 'w', encoding='utf8') as file:
	    file.write(conllu_txt)

	#________________________________________________________________________________________________________________


	with open('latest_result.conllu', 'r', encoding='utf8') as file:
		result = file.read()

	with open(test_conllu, 'r', encoding='utf8') as file:
		golden_standard = file.read()	

	sentences_result = conllu.parse(result)
	sentences_golden = conllu.parse(golden_standard)

	#print(sentences_result[0][0].values())

	words_result = []
	words_golden = []

	for s in sentences_result:
		for w in s:
			words_result.append(list(w.values())[:6])

	for s in sentences_golden:
		for w in s:
			words_golden.append(list(w.values())[:6])

	added_by_mistake = (len(words_result)-len(words_golden))*100/len(words_result)
	#print("Added by mistake:" + str(added_by_mistake))
	#print(len(words_golden))
	print("Length of corpus (in words):" + str(len(words_result)))

	lem_coincidences = 0
	morph_coincidences = 0

	for i in range(len(words_golden)):
		if words_golden[i][1].lower() != words_result[i][1].lower():
			words_result.remove(words_result[i])
			#print(words_golden[i][1], words_result[i][1], i)
		if words_golden[i][2] == words_result[i][2]:
			lem_coincidences += 1
		if words_golden[i][3] == words_result[i][3] and words_golden[i][4] == words_result[i][4] and words_golden[i][5] == words_result[i][5]:
			morph_coincidences += 1
		

	#print(len(words_result))

	with open('all_results.txt', 'a+', encoding='utf8') as file:
		file.write("FILE: " + test_text +"\n")
		file.write("MODEL: " + current_model +"\n")
		file.write("Length of corpus (in words): " + str(len(words_golden)) +"\n")
		file.write("Number of words accurately lemmatized: " + str(lem_coincidences) +"\n")
		file.write("Number of words accurately analyzed: " + str(morph_coincidences) +"\n")
		file.write("Accuracy of lemmatizator: "+ str (round (100 * lem_coincidences / len(words_result) - added_by_mistake, 2))+" %\n")
		file.write("Accuracy of morphological parser: "+ str (round (100 * morph_coincidences / len(words_golden) - added_by_mistake, 2))+" %\n")
		file.write("--\n")

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    parser.add_argument('--text')
    parser.add_argument('--conllu')
    args = parser.parse_args()
    main(args)