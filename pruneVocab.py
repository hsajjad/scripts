import sys
import codecs


# Takes a text file as input
# create it's vocab
# replace infrequenct words (count 3)  with <unk>


def file_process(text_file):
	dict_vocab={}
	with codecs.open(text_file, 'r', 'utf-8') as f:
		for line in f:
			word_arr = line.split()
			for i in range(len(word_arr)):
				if word_arr[i] in dict_vocab:
					dict_vocab[word_arr[i]] = dict_vocab[word_arr[i]] + 1
				else:
					dict_vocab[word_arr[i]] = 1
	f.close()
	return dict_vocab

def replace_with_unk(text_file, dict_vocab, freq_threshold):
	with codecs.open(text_file, 'r', 'utf-8') as f:
		for line in f:
			output = []
			word_arr = line.split()
			for i in range(len(word_arr)):
				if dict_vocab[word_arr[i]] <= freq_threshold:
					output.append("<unk>")
				else:
					output.append(word_arr[i])
			print (" ".join(output))
	f.close()
	return 


if __name__ == "__main__":
	text_file = sys.argv[1] # vocab file is frequency space word
	if len(sys.argv) == 3:
		freq = int(sys.argv[2])
	else:
		freq = 3
	print ("UNK replacement frequency is: %d" % freq)
	dict_vocab = file_process(text_file)
	replace_with_unk(text_file, dict_vocab, freq)
