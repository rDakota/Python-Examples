# show examples of using range function

# range is a built in function
# It's used to create a range of integer numbers

# Basic range loop

# This loop steps through the sequence of numbers 
# created by range(5)
# and prints each one
for i in range(5):
    print(i)


# # Example -- add up the numbers from 0 to n
# print()
# # Sum up values from 0 to 100

total = 0 
for i in range(101):
    total += i

print(total)

# print()
# # Loop through numbers from 0 to 100
# # Printt each number, except print Beep for numbers divisible by 7
# # See FizzBuzz on the homework

for n in range(1, 51):
    if n % 7 == 0: # if divisible by 7
        print("BEEP")
    else:
        print(n)

# print()
# Three argument range, start stop increment

# for i in range(6, 0, -2):
#     print(i)
    
for row in range(4):
    for col in range(4):
        print('*', end='')
    print()