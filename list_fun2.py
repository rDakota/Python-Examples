'''
Program where the elements of a list are square and returned
'''

def square_list(my_list):
    new_list = [] # initialize list 
    for num in my_list: # iterate arcross my_list
        square = num * num # squaring
        new_list.append(square) # add the squared value to new_list
    # aggregator pattern => add element each iteration of our loop
    return new_list 
    # return statement MUST BE OUTSIDE of loop 
    # in order for to run properly
    # if looking for a particular value across the loop 
    # then may have it inside of the loop

#list = []
#list1 = [1]
#list1 = [2, 3]
#list1 = [5, 6, 7, 8, 9]
list1 = [3, 4, 5, 6, 7, 8]
list2 = square_list(list1)
print(list1)
print(list2)