import math
#def BiggestOfThree():
##    b = int(input("2nd number: "))
#    c = int(input("3rd number: "))

#    return int

#    if a > b and a >c:
#        print(a)
#    elif b > a and b >c:
#        print(b)
#    elif c > b and c >a:
#        print(c)
    


#BiggestOfThree()
#If you want me to make it so an input doesnt have to stop it let me know. I just found this easier to remember
print("Enter 10 Numbers and -1 to move on: ")
num = 0
list1 = []
list2 = []
while num != -1:
    num = int(input())
    if num != -1:
        list1.append(num)
        print(list1)
    num2 = num *2
    list2.append(num2)

    print(list2)

