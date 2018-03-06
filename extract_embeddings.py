from gensim import models
import sys
import codecs
import argparse
import numpy as np

# given an embedding file and a word file, extract embedding of those words

def loadEmbeddings(vecFile):
        dic = {}
        fin = codecs.open(vecFile, 'r', 'utf-8')
        for line in fin:
                line = line.strip()
                cols = line.split()
                if len(cols) != 2:

                        dic[cols[0]] = " ".join(cols[1:])
        return dic


def word_file_process(word_file, out_file, word_vectors):
        out = codecs.open(out_file, 'w', 'utf-8')
        with codecs.open(word_file, 'r', 'utf-8') as f:
                for word in f:
                        word = word.rstrip()
                        if word in word_vectors:
                                word_embed = word_vectors[word]
                                out.write(word + " " + word_embed + "\n")
        f.close()
        out.close()
        return


if __name__ == "__main__":

        parser = argparse.ArgumentParser(description='Load word embeddings and find similar words given a file')

        parser.add_argument('--text_file', type=str, help='Text file to get embedding of words')
        parser.add_argument('--embedding', type=str, help='Load embedding file')
	parser.add_argument('--out_file', type=str, help='output file')

        params = parser.parse_args()

        input_file = params.text_file
        embed_file = params.embedding
        embed_format = "Text"


        # load model
        vecs = loadEmbeddings(embed_file)
	out_file = params.out_file
	if out_file == None:
        	out_file = input_file + ".embed"
	
        print ("Output file: " + out_file)
        word_file_process(input_file, out_file, vecs)
