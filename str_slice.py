
''' Program which checks to see if one string is part of another
    string.
    Demonstrates the use of string slicing and return statements
    which end a function's execution
'''

def exists_in(word1, word2):
    index = 0
    
    while index < len(word1):
        sub = word1[index: index + len(word2)]
        #print(index, sub)
        index += 1
        
        if sub == word2:
            return True
    
        #print(sub)
    return False
    
#should return True because "Hello" is part of hte larger string "Hello World"
print( exists_in("Hello World", "Hello") )
#should return False
print( exists_in("Hello World", "Bye") )
#should return True
print( exists_in("Hello World", "llo") )