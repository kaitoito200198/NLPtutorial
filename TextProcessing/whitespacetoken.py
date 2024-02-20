# import WhitespaceTokenizer() method from nltk 
from nltk.tokenize import WhitespaceTokenizer 
	
# Create a reference variable for Class WhitespaceTokenizer 
tk = WhitespaceTokenizer() 
	
# Create a string input 
gfg = "GeeksforGeeks \nis\t for geeks"
	
# Use tokenize method 
geek = tk.tokenize(gfg) 
	
print(geek) 
