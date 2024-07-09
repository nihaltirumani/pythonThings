# base-10 to base-2 converter
userinput = ""
number : int = None
binarynumber = ""
decimalnumber = 0

def b102(number): # changes the variable binarynumber only not returns
    global binarynumber
    while not number == 0:
        binarynumber = binarynumber + str(number % 2)
        number = number // 2


def b210(number): # changes the variable decimalnumber only not returns
    global decimalnumber
    for i in range(0,len(binarynumber)): 
        decimalnumber = decimalnumber + (int(binarynumber[i]) * pow(2,i))

userinput = str(input("Convert: \n1.decimal to binary \n2.binary to decimal\n"))
if userinput.lower() == "1": 
    number = int(input("Decimal Number: "))
    b102(number)
    print(binarynumber[::-1])
elif userinput.lower == "2":
    number = int(input("Binary Number: "))

print(decimalnumber)