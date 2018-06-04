from nltk.corpus import brown
import nltk
print(brown.fileids())
texts = brown.words('ca01')
print(texts)