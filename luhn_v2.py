card_num = int(input("Enter your credit card number: "))

mult_by_2 = False

orig_num = card_num
total = 0
twice = 0


while card_num != 0:
    digit = card_num % 10
    card_num = card_num // 10
    #print(digit, card_num)
    
    if mult_by_2 == True:
        twice = 2 * digit
        if twice > 9:
            twice = twice -9
        total += twice
    
    else:
        total += twice 
    
    mult_by_2 = not(mult_by_2)
    
print("Luhn Checksum:", total)

print("The number", orig_num, "is", end=" ")
if total % 10 != 0:
    print("not", end=" ")
print("valid") 