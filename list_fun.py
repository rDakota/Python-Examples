'''
This program swaps the ends of a list
'''
# NOTE -> Much like the homework 

def swap_ends(my_list):
    first = my_list[0]
    last = my_list[-1]
    
    # Above is eexclusive to python
    #last_idx = len(my_list) -1 
    #last = my_list[last_idx]
    
    # Below cannot be done with strings but can be with lists
    my_list[0] = last
    my_list[-1] = first
    return my_list
    
    
#list = []
#list1 = [1]
#list1 = [2, 3]
#list1 = [5, 6, 7, 8, 9]
list1 = [3, 4, 5, 6, 7, 8]
swap_ends(list1)
print(list1)

