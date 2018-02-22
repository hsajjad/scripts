import sys
import codecs
import argparse
import random

def read_normalized_dict(norm_dict):
	dict_norm = {}
	with codecs.open(norm_dict, 'r', 'utf-8') as f:
		for line in f:
			wd, word = line.strip().split('\t')
			if word in dict_norm:
				dict_norm[word].append(wd)
			else:
				dict_norm[word] = [wd]
	f.close()
	return dict_norm


def norm_dict_to_corpus(corpus, dict_norm, threshold):
	# save the line numbers that have the dictionary word
	dict_norm_corpus = {}
	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			modified_line = []
			print (line.strip())
			word_arr = line.strip().lower().split()
			for word in word_arr:
				if word in dict_norm:
					print (word)
					if threshold > random.random(): # between 0 and 1
						# choose random option from the normalized dictionary
						random_replacement = random.randint(0,len(dict_norm[word])-1)
						dict_options = dict_norm[word]
						word = dict_options[random_replacement]
					print (word)
				modified_line.append(word)
			print (" ".join(modified_line) + "\n")
	f.close()



if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Add spelling errors in the corpus')

	parser.add_argument('--corpus', type=str, help='corpus file')
	parser.add_argument('--norm_dictionary', type=str, help='normalized dictionary')
	parser.add_argument('--threshold', type=str, help='Percentage of words need to be replaced')
	params = parser.parse_args()

	corpus = params.corpus
	norm_dictionary = params.norm_dictionary
	threshold = float(params.threshold)

	dict_norm = read_normalized_dict(norm_dictionary)

	norm_dict_to_corpus(corpus, dict_norm, threshold)
	

