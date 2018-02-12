## Random Scripts

Some detail of every script can be found in the beginning of the script


#### Normalize Arabic
This script normalizes Arabic and do some Twitter related normalization e.g. hashtags, numbers, etc.
```
python normalize_Arabic.pl input_file output_file
```

#### Prune Vocabulary
Given a text file, calculate frequency of each word in it and replace the least frequent ones (occurring <= 3) with tag <unk>
```
python pruneVocab.py input_file > output
```
You can also specify your own threshold value. Note that check on threshold value is inclusive of the threshold frequency
```
python pruneVocab.py input_file 10  > output
```

#### Candidate pairs from a file of nearest neighbours in word2vec format
```
python candidatePairs.py file_with_nearest_neighbor
```
