# import the existing word and sentence tokenizing 
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize 

text = "Natural language processing (NLP) is a field. don't worry" 

print(sent_tokenize(text)) 
print(word_tokenize(text)) 
