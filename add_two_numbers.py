# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list (or list) in reverse order.

# Example:-
# l1 = [3, 4, 2]  # Represents 243
# l2 = [1, 2, 3]  # Represents 321

# 243 + 321 = 564

def addTwoNumbers(l1, l2):
    num1 = int("".join(str(digit) for digit in reversed(l1)))  

    num2 = int("".join(str(digit) for digit in reversed(l2)))
    
    sum = num1+num2
    print(sum)

l1 = [3, 4, 2]
l2 = [1, 2, 3]
addTwoNumbers(l1, l2)
