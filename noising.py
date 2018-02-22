import sys

def file_process(corpus):
	dict_vocab={}
	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			word_arr = line.split()
			for i in range(len(word_arr)):
				if word_arr[i] in dict_vocab:
					dict_vocab[word_arr[i]] = dict_vocab[word_arr[i]] + 1
				else:
					dict_vocab[word_arr[i]] = 1
	f.close()
	return dict_vocab


def read_normalized_dict(norm_dict):
	dict_lex = {}
	with codecs.open(lexicon, 'r', 'utf-8') as f:
		for line in f:



if "__name__" == __main__:
	corpus = sys.argv[0]
	norm_dict = sys.argv[1]

	print ("corpus")
	print ("lexicon")