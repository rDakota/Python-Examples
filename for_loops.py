'''There are certain tasks where for loop is easier and certain ones where while is easier.
Try switching if you are having lots of trouble'''

'''for loop structure is used below'''
total_num_ls = 0

s = "hello World"

for letter in s:
    if letter == 'l':
        total_num_ls += 1

print("There were", total_num_ls, "ls found.")

'''while loop structure is used below'''
iterations = len(s) # loop run this many times
index = 0
total_num_ls = 0

while iterations != 0: 
    letter = s[index]
    if letter == 'l':
        total_num_ls += 1
        
    iterations -= 1
    index += 1
print("There were still", total_ls, "ls found.")

'''2nd variation of while loop structure is used below'''
iterations = len(s) # loop run this many times
i = 0
total_num_ls = 0

while i < iterations: #up to but not include index 11
    print("inside while loop") #tester to see if while loop is running
    letter = s[i]
    if letter == 'l':
        total_num_ls += 1
        
    i += 1
print("There were still", total_num_ls, "ls found.")


'''for loop using a sequence'''
total = 0

for num in [8, 2, 10, -16]:
    total += num
print(total)

print(range(20))
print(range(5, 20))