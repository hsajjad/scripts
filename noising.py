import sys
import codecs
import argparse

def build_vocab(corpus):
	dict_vocab={}
	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			word_arr = line.strip().lower().split()
			for i in range(len(word_arr)):
				if word_arr[i] in dict_vocab:
					dict_vocab[word_arr[i]] = dict_vocab[word_arr[i]] + 1
				else:
					dict_vocab[word_arr[i]] = 1
	f.close()
	return dict_vocab


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


def load_vocab(corpus_vocab):
	dict_vocab = {}
	with codecs.open(corpus_vocab, 'r', 'utf-8') as f:
		for line in f:
			word, count = line.strip().split('\t')
			dict_vocab[word] = count
	f.close()
	return dict_vocab


def save_vocab(dict_vocab, corpus):
	with codecs.open(corpus+".vocab", 'w', 'utf-8') as f:
		for key, value in dict_vocab.items():
			f.write(key + "\t" + str(value) + "\n")
	f.close()


def norm_dict_to_corpus(corpus, dict_norm):
	# save the line numbers that have the dictionary word
	dict_norm_corpus = {}
	line_num = 0
	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			line_num += 1
			word_arr = line.strip().lower().split()
			for word in word_arr:
				if word in dict_norm:
					if word in dict_norm_corpus:
						dict_norm_corpus[word].append(line_num)
					else:
						dict_norm_corpus[word] = [line_num] # this line contains the lexicon word
	f.close()
	return dict_norm_corpus


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Add spelling errors in the corpus')

	parser.add_argument('--corpus', type=str, help='corpus file')
	parser.add_argument('--corpus_vocab', type=str, help='corpus vocab file. optional parameter')
	parser.add_argument('--norm_dictionary', type=str, help='normalized dictionary')

	params = parser.parse_args()

	corpus = params.corpus
	norm_dictionary = params.norm_dictionary

	dict_norm = read_normalized_dict(norm_dictionary)

	dict_vocab = {}
	if params.corpus_vocab == None:
		dict_vocab = build_vocab(params.corpus)
		save_vocab(dict_vocab, corpus)
		print ("Save vocabulary file as " + corpus + ".vocab")
	else:
		dict_vocab = load_vocab(params.corpus_vocab)

	dict_norm_corpus = norm_dict_to_corpus(params.corpus, dict_norm)
	print (dict_norm_corpus)

