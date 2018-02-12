# program to take a file with nearest neighbours and extract them
import sys

def process(fname, num):
	f = open(fname, 'r', encoding="utf-8")
	for line in f:
		line = line.strip()
		nearest_words = word_candidates(line, num)
		print (nearest_words)

def word_candidates(line, num):
	word_score = line.split('\t')
	options = word_score[0]

	if num > len(word_score): num = len(word_score)
	for w_s in range(1,num):
		curr_word, curr_score = word_score[w_s].split(' ')
		options = options + "\t" + curr_word
	return options

if __name__ == "__main__":
	text_file = sys.argv[1]
	num = 6 # how many candidates to keep minus 1
	process(text_file, num)