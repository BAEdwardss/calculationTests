A=5
B=2
C=7
D=1


def findGpa():
    return((4*A+3*B+2*C+1*D)/(A+B+C+D))


def findLargest(a, b):
    if a > b:
        print("a is greater than b")
    elif a < b:
        print("a is less than b")
    elif a == b:
        print("a equals b")
    else:
        print("error")

def addNumbers(a, b):
    return(a+b)





findLargest(2, 7)
print(addNumbers(5,6))
print(findGpa())


