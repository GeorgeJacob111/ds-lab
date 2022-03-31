import nltk
#nltk.download('averaged_perception_tagger')
sample_text="""Rama killed Ravana to save Sita from Lanka.The legend of the Ramayan is the most 
popular Indian epic. 
A lot of movies and serials have already been shot in several languages here in India 
based Ramayana"""
tokenized=nltk.sent_tokenize(sample_text)
for i in tokenized:
 words=nltk.word_tokenize(i)
 tagged_words=nltk.pos_tag(words)
 chunkGram=r"""VB: {}"""
 chunkParser=nltk.RegexpParser(chunkGram)
 chunked=chunkParser.parse(tagged_words)
 print(chunked)
 chunked.draw()