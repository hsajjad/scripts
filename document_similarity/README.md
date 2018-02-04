## Document Similarity Vector for Similar Document Retrieval Against a term

Train document similarity vector and use it to find similar documents or similar terms against a key word

### usage: train a model
```
python document_similarity.py --train out --save_model trainedModel
```
### usage: load an already saved model
```
python document_similarity.py --load_model trainedModel
```

### Preprocessing the data in the required format
If you have all the documents in a directory, following script in utils can be used to put the documents in the required format

```
### usage: input a directory, output will be a file containing all the documents one line per document
```
python utils/preprocess.py inputDir outputFile
```

