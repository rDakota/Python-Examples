'''
This program concatenates multiple lists into one 
'''

def concat(list_1, list_2):
    concat_list = [] # start with empty
    
    #for word in l1, l2: # content of lists to use for loop
        #print(word)
    
    stop = len(list_1) # in order for loop to run 4 times
    index = 0
    #for index in range(stop):
    while index < stop: # index = > index + len(list) index += 1
        #print(index, list_1[index], list_2[index])
        word = list_1[index] + list_2[index] 
        #print(word)
        concat_list.append(word)
        index += 1
        
    
    return concat_list # eventually return that list
    
    
# lists are the same length 
l1 = ['M', 'na', 'i', 'Val']
l2 = ['y', 'me', 's', 'erie']

new_list = concat(l1, l2)
print(l1)
print(l2)
print(new_list)