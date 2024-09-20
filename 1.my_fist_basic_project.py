try:
    n1 = int(input("Enter the first number: "))
    n = str(input("Operation to be performed(+ - * /): "))
    n2 = int(input("Enter the second number: "))
    if n=='+':
        print(n1+n2)
    elif n=='-':
        print(n1-n2)
    elif n=='*':
        print(n1*n2)
    elif n=='/':
        if n2==0:
            print("Division by zero is not allowed")
        else:
            print(n1/n2)
    else:
        print("Please forgive us for our calculator only perform only these operation (+ - * /)")
except ValueError:
    print("Please input valid numbers")
