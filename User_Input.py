from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# 1-Tokenize
print('Hello in IR Project...')
text = input('Please Write your text that you want to make Tokenization for it: ')
print('Sentence that i want to make tokenizer for it:' + text)
tokenize_sentence = word_tokenize(text)
print(tokenize_sentence)

# 2-Stemmer
ps = PorterStemmer()
for w in tokenize_sentence:
   print(ps.stem(w))



