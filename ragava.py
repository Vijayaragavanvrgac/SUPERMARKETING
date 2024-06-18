import pandas as pd 
import csv
filename='ragava.csv'
file=open('ragava.csv','a',newline='')
writer=csv.writer(file)
if file.tell()==0:
    header=['product name','product price','available product']
    writer.writerow(header)
while True:
    product_name=input("Enter your product name:")
    while True:
        try:
            product_price=float(input("Enter a your product price:"))
            break
        except ValueError:
            print("invalid input.Please Enter your valid number.")
    available_product=int(input("Enter a available product:"))
    writer.writerow([product_name,product_price,available_product])
    add=input("Do you want to add more?(yes/no):").lower()
    if add!='yes'.lower():
        break
print("Data has been written.")

