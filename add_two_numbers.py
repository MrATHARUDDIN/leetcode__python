def addTwoNumbers(l1, l2):
    num1 = int("".join(str(digit) for digit in reversed(l1)))  

    num2 = int("".join(str(digit) for digit in reversed(l2)))
    
    sum = num1+num2
    print(sum)

l1 = [3, 4, 2]
l2 = [1, 2, 3]
addTwoNumbers(l1, l2)
