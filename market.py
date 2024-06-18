import pandas as pd 
import smtplib
def available_product(df):
    print("Available product names:")
    for product_name in df['product name']:
        print(product_name)
def product(df):
    total_price=0
    gst=0.8
    bills_items=[]
    while True:
        Enter_product=input("Enter the  name of  the product your buy the product (or 'quit' to exit):")
        if Enter_product.lower()=='quit':
            print("\nbill is printing")
            break
        if Enter_product in df['product name'].values:
            product_details=df[df['product name']==Enter_product]
            while True:
                try:
                    how_many_product=int(input(f"How many Product{Enter_product} your buy the product?"))
                    if how_many_product<=0:
                        print("Please enter a valid quantity greater than zero.")
                    elif how_many_product> product_details['available product'].values[0]:
                        print(f"Sry!..Only available{product_details['available product'].values[0]} products.")
                    else:
                        quality=product_details.index[0]
                        df.at[quality,'available product']-=how_many_product
                        cost_per_unit=product_details['product price'].values[0]
                        total_product_cost=how_many_product*cost_per_unit
                        gst_amount=total_product_cost*gst
                        total_product_cost_with_gst=total_product_cost + gst_amount
                        total_price+=total_product_cost_with_gst
                        bills_items.append({"product": Enter_product,
                                            "Quantity": how_many_product,
                                             "Price per unit": cost_per_unit,
                                             "GST Amount": gst_amount,
                                             "Total cost":total_product_cost_with_gst})
                        print(f"You can buy {how_many_product} {Enter_product}at ${cost_per_unit:.2f} each.")
                        print(f"Total cost for {how_many_product} {Enter_product}(incl.GST): ${total_product_cost_with_gst:.2f}")
                        break
                except:
                    print("Invalid input.Please enter a valid number.")
        else:
            print(f"Product '{Enter_product}'not found, Please enter a valid product name.")
    if bills_items:
        print("\n------ Bill Summary ------")
        for item in bills_items:
            print(f"{item['product']} {item['Quantity']} at ${item['Price per unit']:.2f} each. Total(incl.GST): ${item['Total cost']:.2f}")
        print(f"\nTotal Bill Amount(incl.GST): ${total_price:.2f}")
        df.to_csv('ragava.csv', index=False)
        print("ragava file updated.")
        Enter_mail = input("Enter email id to get bill (or 'quit' to exit): ")
        if Enter_mail.lower() == 'quit':
            return  
        send_mail(Enter_mail,bills_items,total_price)
    else:
        print("No items purchased. Exiting...")
    print("Thank you for shopping with us!")
def send_mail(Enter_mail,bills_items,total_pice):
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('ragavanragavan95204@gmail.com', 'actu rkhf jkwr xrzn')
        subject = 'Your Purchase Bill'
        body = "\nBill Summary\n"
        for item in bills_items:
            body += f"{item['product']} {item['Quantity']} at ${item['Price per unit']:.2f} each. Total(incl.GST): ${item['Total cost']:.2f}\n"
        body += f"\nTotal Bill Amount(incl.GST): ${total_pice:.2f}"
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail('ragavanragavan95204@gamil.com', Enter_mail, message)
        smtp_server.quit()
        print(f"Bill sent successfully to {Enter_mail}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")
def main():
    df = pd.read_csv('ragava.csv')
    available_product(df)
    while True:
        product(df)
        next_customer = input("Do you want to continue with another customer? (yes/no): ")
        if next_customer.lower() != 'yes':
            break
    print("Thank you for using our shopping system!")
if __name__ == "__main__":
    main()
                