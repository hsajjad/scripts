import re
import json
import argparse


# python create_jsons.py --json sample.json --ordering ordering.txt --order bottom --output_dir output-bot/

#####
layer = "rnn"
NUM=25

def load_orderings(file):

	### read ordering file
	c = 1
	with open(file) as fp:
		for line in fp:
			if c == 3:
				TOP_TO_BOTTOM = list(map(int, line.rstrip().split(" ")))
			elif c == 6:
				BOTTOM_TO_TOP = list(map(int, line.rstrip().split(" ")))
			c += 1

	assert(len(TOP_TO_BOTTOM)==1000)
	assert(len(BOTTOM_TO_TOP)==1000)
	return TOP_TO_BOTTOM, BOTTOM_TO_TOP

#UNSUPERVISED_RANKINGS = [1696,1903,1776,633,1722,1570,1625,1869,1281,1593,602,1827,653,104,91,1653,1782]

def load_json_template(mask_file):
	with open(mask_file) as fp:
	    mask_file_content = "\n".join(fp.readlines())
	    mask_file_content = re.sub(r'//.*\n', '\n', mask_file_content)
	    mask = json.loads(mask_file_content)
	return mask


def write_json(outputDir, order):

	### write json files

	output_file = outputDir + "/" + str(0) + ".json"
	with open(output_file, 'w') as outf:
		json.dump(mask, outf)


	for i in range(0,len(order),NUM):
		print (i)
		current = order[i:i+NUM]
	
		for n in current:
			if n < 500:
				mask[layer]["0"]["output"].append(n)
			else:
				mask[layer]["1"]["output"].append(n-500) # indexing will be from 0

		output_file = outputDir + "/" + str(i+NUM) + ".json"
		with open(output_file, 'w') as outf:
			json.dump(mask, outf)
		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Create Json files for LM ablation')

	parser.add_argument('--json', type=str, help='json format file', required = True)
	parser.add_argument('--ordering', type=str, help='neuron ordering file', required = True)
	parser.add_argument('--order', choices=['top', 'bottom'], help='Neuron order to pick, top to bottom or bottom to top', required = True)
	parser.add_argument('--output_dir', type = str, required = True)

	args = parser.parse_args()

	mask = load_json_template(args.json)
	top_to_bot, bot_to_top = load_orderings(args.ordering)
	if args.order == "top":
		write_json(args.output_dir, top_to_bot)
	elif args.order == "bottom":
		write_json(args.output_dir, bot_to_top)
	else:
		print ("Wrong choice of order")
		exit(0)


