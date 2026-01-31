#calculator of 2 operators 
#operations = add,substract,divide,multiplication

a = float(input("enter 1st number : "))
b = float(input("enter 2nd number : "))
print("for addition enter 1 \nfor substraction enter 2\nfor multiplication enter 3\nfor division enter 4")
c = int(input("enter here : "))
if (c==1):
    print(a+b)
elif (c==2):
    print(a-b)
elif (c==3):
    print(a*b)
elif (c==4):
    if (b==0):
        print("error: cannot divide with zero")
    else:
        print(a/b)
else:
    print("invalid input")  

print("Thank You")       
