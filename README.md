## Random Scripts

Some detail of every script can be found in the beginning of the script


### Normalize Arabic
This script normalizes Arabic and do some Twitter related normalization e.g. hashtags, numbers, etc.
```
python normalize_Arabic.pl input_file output_file
```

#### Prune Vocabulary
Given a text file, calculate frequency of each word in it and replace the least frequent ones (3) with tag <unk>
```
python pruneVocab.py input_file > output
```

