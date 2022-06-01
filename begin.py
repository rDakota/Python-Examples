import random

#random.seed(1)
l = ['wef', 'wer', 'wit']

num = random.choice(l)

print(num)
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

print("Die1", die1, "Die2", die2)



i = 1
user = int(input("Enter a num: "))
while i < user:
    print(i)
    i += 1