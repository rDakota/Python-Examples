s = "hello"

my_list = [3, 7, 5, 10]
# print( my_list[0])
# print( my_list[-1] )
# print(len(my_list))

# s[0] = "H" # cannot do this bc are immutable
# strings are immutable 
# lists ARE muttable !!!!!!!

# my_list[0] = 6 # overrode the previous variable it is gone
# print(my_list[0])

# iterating over lists
# for item in my_list:
#     print(item)

# index = 0
# while index < len(my_list): # cannot do <= or one iteration too far
#     my_list[index] += 3 # my_list[index] = my_list[index] + 3
#     index += 1
# print(my_list)

# List functions ->

# print(my_list)

# my_list.append(11)# can only append one thing using this method
# print(my_list)
# my_list.append([12, 13, 14]) # would create nested list and appear as given
# print(my_list)

# my_list.extend([4, 3, 1]) # one argument as list with 3 pieces of data in it
# order matters will add in order you give

# print(my_list)

# my_list.insert(4, 30) # at index 4 replace with 30
# print(my_list)

# my_list.remove(1) # removes value 1
# print(my_list)

# val = my_list.pop() # returns the value that was at the top
# print(my_list)
# print(val)

my_list = ["d", "A", "B", "z", "5", "?"] # sorts by ascii values

# sorting must involve all of the ame data type
my_list.sort() # sort by smallest to greatest numerical value
print(my_list)

my_list.reverse() # reverse order
print(my_list)

# lists ARE muttable !!!!!!!!!!!!!
