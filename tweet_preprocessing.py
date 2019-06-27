import codecs
import preprocessor as p
import argparse

p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.MENTION) # only convert urls and emoji to unique tags

def process(corpus, output):
	fout = codecs.open(output, 'w', 'utf-8')

	with codecs.open(corpus, 'r', 'utf-8') as f:
		for line in f:
			line = line.strip()
			line = p.tokenize(line)

			lineArr = line.split()
			outArr = []
			for word in lineArr:
				if word.startwith("#") and word.endswith("#"):
					word = word[1:-1]
					outArr.append(word)

			lineOut = " " + join(outArr) 								
			fout.write(lineOut + "\n")

	fout.close()
	f.close()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Preprocess Tweets')
	parser.add_argument('--input', type=str, help='text input file')
	parser.add_argument('--output', type=str, help='output file')

	params = parser.parse_args()

	corpus = params.input
	output = params.output

	process(corpus, output)


		
