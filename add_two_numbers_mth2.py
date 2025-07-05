def addtwo(l1, l2):
    i = 0 
    carry = 0
    result = []

    while i < len(l1) or i < len(l2) or carry != 0:
        if i < len(l1):
            d1 = l1[i]
        else:
            d1 = 0     
        if i < len(l2):
            d2 = l2[i]
        else:
            d2 = 0

        total = d1 + d2 + carry
        carry = total // 10
        digit = total % 10
        result.append(digit)
        i = i + 1

    print(result)
    return result

l1 = [3, 4, 2]  
l2 = [1, 2, 3] 

x = list(reversed(l1))
y = list(reversed(l2))

addtwo(x, y)
