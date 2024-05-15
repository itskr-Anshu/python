a = int(input("enter the first no."))
b = int(input("enter the second no."))
c = input("Enter the operator :")

match c:
    case "+":
        print("Addition is :", a+b)
    case "-":
        print("subtraction is :", a-b)
    case "*":
        print("Multiplication is :", a*b)
    case "/":
        print("Division is :", a/b)


