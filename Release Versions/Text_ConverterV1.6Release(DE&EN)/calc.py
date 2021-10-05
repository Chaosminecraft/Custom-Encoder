def main():
    print(f"\nthe first module for the Text converter.")
    print("a Calculator. There is '+' '-' 'x' '/' there.")
    print(f"write help for help.\n")
    while True:
        op=input("What oparation? ")
        print()
        if op.lower()=="+":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1+=num2
            print(num1)
        if op.lower()=="-":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1-=num2
            print(num1)
        if op.lower()=="*" or op.lower()=="x":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            num1*=num2
            print(num1)
        if op.lower()=="/" or op.lower()=="÷":
            num1=int(input("Number 1: "))
            num2=int(input("Number 2: "))
            calc=num1/num2
            print(num1)
        if op.lower()=="exit":
            return
main()
