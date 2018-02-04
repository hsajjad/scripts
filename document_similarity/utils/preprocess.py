# read files from a directory and make them one line per document
# append document name as first word in the file
# output one single file concatenating all the input files

# usage: python preprocess.py inputDir outputFile

from os import listdir
from os.path import isfile, join
import sys

def combineDocs(d_path, o_file):

	docLabels = []
	#d_path = "/Users/hsajjad/Desktop/ted_data_conspeesh_formatted/data_stage_ted_001/"
	#d_path = "/Users/hsajjad/Work/software/documentEmbed/tmp/"

	docLabels = [f for f in listdir(d_path) if f.endswith('.txt')]

	data = []
	doc_in_line = ""

	fout = open (o_file, 'w', encoding="utf-8")

	for doc in docLabels:
		with open(d_path + doc, 'r', encoding="utf-8") as f:
			doc_in_line = doc + " " + (f.read()).replace("\n", " ") + "\n"
			fout.write(doc_in_line)
	fout.close()


if __name__ == "__main__":
	d_path = sys.argv[1] # path to the directory to read files
	o_file = sys.argv[2] # path and name of the outputfile
	combineDocs(d_path, o_file)

