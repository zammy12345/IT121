x = 300
def closest(a, b, c):
    
    if abs(x - a) < abs(x - b) and abs(x - a) < abs(x - c):
        print("A or", a,"is the Closest Number to", x)
    elif abs(x - b) < abs(x - a) and abs(x - b) < abs(x - c):
        print("B or", b,"is the Closest Number to", x)
    else:
        print("C or", c,"is the Closest Number to",x)
   
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: ")) 
    
closest(a, b, c)