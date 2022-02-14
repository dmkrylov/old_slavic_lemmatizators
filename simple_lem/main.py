import argparse
from lemmatizator import lemmatize

def main(args):
	with open (args.file, 'r', encoding = 'utf8') as file:
		lines = file.readlines()
	with open (args.file[:-4]+'_lemmatized.txt', 'w', encoding = 'utf8') as file:
		for line in lines:
			file.write(lemmatize(line))


if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()
    main(args)