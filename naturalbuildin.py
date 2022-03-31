import nltk
from nltk.util import ngrams

samplText="this is very good book to study"
Ngrams=ngrams(sequence=nltk.wordpunct_tokenize(samplText),n=2)
for grams in Ngrams:
 print(grams)