## Document similarity vector for similar document retrieval against a term

Train document similarity vector and use it to find similar documents or similar terms against a key word. To preprocess the data in the required format, see the end of this readme or check in the utils directory.

### usage: train a model
```
python document_similarity.py --train out --save_model trainedModel
```
### usage: load an already saved model
```
python document_similarity.py --load_model trainedModel
```

### Testing the model on train
```
predictions = []
for doc_id in range(len(train)):
    inferred_vector = model.infer_vector(train[doc_id].words)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    pred = [docid for docid, sim in sims].index(train[doc_id].tags[0])
    predictions.append(pred)

import collections
collections.Counter(predictions) # this mentions how many times the right document appear at index 0
```

You can modify the script for various options:
```
model.most_similar('solar', topn=20) # find most similar words given a term

word_vec = model['immigration'] # find most similar documents based on a term
model.docvecs.most_similar([word_vec])

#infer a vector based on several terms and find the closest word or document
inferred_vector = model.infer_vector(['solar', 'energy', 'panels', 'renewable'])
model.most_similar([inferred_vector])

multi_word = model['solar'] + model['energy'] # generate a vector for multiterms
related_words = model.most_similar([multi_word], topn=15)
```


### Preprocessing the data in the required format
If you have all the documents in a directory, following script in utils can be used to put the documents in the required format

### usage: input a directory, output will be a file containing all the documents one line per document

```
python utils/preprocess.py inputDir outputFile
```






