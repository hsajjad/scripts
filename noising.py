import sys
import codecs

def file_process(corpus):
	dict_vocab={}
	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			word_arr = line.strip().split()
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

if __name__ == "__main__":
	#corpus = sys.argv[0]
	#norm_dict = sys.argv[1]

	
	dict_norm = read_normalized_dict('/Users/hsajjad/Desktop/normalization/emnlp_dict.txt')
	print (dict_norm)