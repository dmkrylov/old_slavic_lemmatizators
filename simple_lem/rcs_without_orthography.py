from killing_orthography import kill_orthography

with open ("russian_church_slavonic.txt", 'r', encoding = 'utf8') as file:
	text = file.read()
with open ("rnc_without_orthography.txt", 'w', encoding = 'utf8') as file:
	for word in text.split():
		file.write(kill_orthography(word)+' ')

