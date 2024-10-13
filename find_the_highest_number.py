#Use def to identify the user's highest number
def highest_number(var1, var2, var3, var4, var5):
    #Compare all the variables
    if var1 > var2 and var1 > var3 and var1 > var4 and var1 > var5:
        return var1
    elif var2 > var1 and var2 > var3 and var2 > var4 and var2 > var5:
        return var2
    elif var3 > var1 and var3 > var2 and var3 > var4 and var3 > var5:
        return var3
    elif var4 > var1 and var4 > var2 and var4 > var3 and var4 > var5:
        return var4
    elif var5 > var1 and var5 > var2 and var5 > var3 and var5 > var4:
        return var5
    else:
        return "Error"
#Create a variable to store the user's 5 numbers
var1 = int(input("Please input your first number: "))
var2 = int(input("Please input your second number: "))
var3 = int(input("Please input your third number: "))
var4 = int(input("Please input your fourth number: "))
var5 = int(input("Please input your fifth number: "))
#Create a variable for the result
result = highest_number(var1, var2, var3, var4, var5)
#Print the result of finding the highest number
print(f"The highest number is: {result}")