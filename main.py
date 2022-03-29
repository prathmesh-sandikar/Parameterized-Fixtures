def divby5(a):
    if a%5==0:
        return True
    else:
        return False

def divby7(a):
    if a%5==0:
        return True
    else:
        return False

def divby9(a):
    if a%5==0:
        return True
    else:
        return False

def divby11(a):
    if a%5==0:
        return True
    else:
        return False

if __name__ =="__main__":
    num1=int(input("Enter number"))
    result1=divby5(num1)
    result2 = divby7(num1)
    result3 = divby9(num1)
    result4 = divby11(num1)
