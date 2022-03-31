def generate_ngrams(text,WordsToCombine):
 words=text.split()
 output=[]
 for i in range(len(words)-WordsToCombine+1):
     output.append(words[i:i + WordsToCombine])

 return output
 
x=generate_ngrams(text="this is a good book to study",WordsToCombine=3)
print(x)