#Name: Leon Chen
#Date: May 18
#This program calculates the price of a movie depending on the age and number of guests

#input data
people=int(input("Enter how many people are in your group:"))
age=int(input("Enter the age of your group:"))
movie=str(input("Enter the name of the movie you are watching:"))

#calculating the price based on the inputs
if age>=65:
    price=3.2
elif age>=20:
    price=6.5
elif age>=14:
    price=4.25
elif age>0:
    price=2
else:
    print("Please enter a vaiid age catagory.")

#calculating total price and taxes
subTotal=price*people
tax=subTotal*0.13
total=subTotal+tax

#output data
print("\nThe price per ticket is $%.2f"% price)
print("Subtotal is $%.2f"% subTotal)
print("Taxes are $%.2f"% tax)
print("The total price with taxes is $%.2f"% total)
print("Please have fun watching "+movie,"!")
