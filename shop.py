cp = float(input("Enter the cost price :"))
sp = float(input("Enter the selling price :"))
if(cp<sp):
    print("The Price is profitable")
    x = sp - cp
    print("profit at this product is :", x ,"Rs")
else:
    print("no profit")
    y = cp - sp
    print("Loss at this product is :", y , "Rs")

   