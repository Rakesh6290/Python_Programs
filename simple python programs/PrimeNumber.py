num = int(input("Enter a Number:"))
if num == 1:
    print("It is not a prime")
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("Not a Prime")
            break
    else:
        print("It's a Prime")
            