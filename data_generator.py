# EDA project

# Step 1: Import Libraries
import pandas as pd
import numpy as np
import random as rd
from faker import Faker

#Initialize Faker for genrating fake data
fake = Faker()

# Step 2: Define base list

categories = {
    "Furniture": ["Office Chair","Study Table","Sofa","Bookshell","Dining Table"],
    "Office Supplies": ["Pen","Notebook","Stapler","File Folder","Calculator"],
    "Electronics": ["Laptop","Keyboard","Mouse","Headphones","Monitor"],
    "Grocery": ["Rice Bag","Cooking oil","Sugar","Snacks","Juice Pack"] 
}

regions = ["North","South","East","West"]
payment_modes = ["Cash","Credit card","UPI","Net Banking"]
delivery_status = ["Delivered","Pending","Returned","Cancelled"]
customer_segments = ["Consumer","Corporate","Home Office"]

# Step 3: Generate dataset

superstore_data = [] #Empty list to store all rows

for i in range(1000): #1000 fake records
    order_id = f"ORD{1000 + i}"
    order_date = fake.date_between(start_date='-2y', end_date='today')
    ship_date = order_date + pd.Timedelta(days = rd.randint(1,7))

    customer_name = fake.name()
    customer_id = f"CUST{rd.randint(100,999)}"
    customer_segment = rd.choice(customer_segments)

    category = rd.choice(list(categories.keys()))
    product_name = rd.choice(categories[category])
    product_id = f"PROD{rd.randint(1000,9999)}"

    region = rd.choice(regions)
    state = fake.state()
    city = fake.city()

    quantity = rd.randint(1,10)
    unit_price = rd.randint(100,5000)
    discount = rd.choice([0,5,10,15,20])

    sales_amount = quantity * unit_price * (1 - discount / 100)
    cost_price = sales_amount + rd.uniform(0.6,0.9)
    profit = sales_amount - cost_price

    stock_left = rd.randint(0,50)

    if stock_left < 10:
        auto_reorder = "Yes"
        reorder_quantity = rd.randint(20,50)

    else:
        auto_reorder = "No"
        reorder_quantity = 0

    supplier_name = fake.company()
    supplier_email = fake.company_email()
    payment_mode = rd.choice(payment_modes)
    delivery = rd.choice(delivery_status)

    # Append row as a dictionary
    superstore_data.append({
        "Order ID": order_id,
        "Order Date": order_date,
        "Ship Date": ship_date,
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Customer Segment": customer_segment,
        "Product ID": product_id,
        "Product Name": product_name,
        "Category": category,
        "Region": region,
        "State": state,
        "City": city,
        "Quantity": quantity,
        "Unit Price": unit_price,
        "Discount (%)": discount,
        "Sales Amount": round(sales_amount,2),
        "Cost Price": round(cost_price,2),
        "Profit": round(profit,2),
        "Payment Mode": payment_mode,
        "Delivery Status": delivery,
        "Supplier Name": supplier_name,
        "Supplier Email": supplier_email,
        "Stock left": stock_left,
        "Auto Reorder": auto_reorder,
        "Reorder Quantity": reorder_quantity
    })

# Step 4: Create Dataframe and save to CSV

df = pd.DataFrame(superstore_data)
try:
    df.to_csv("Superstore_Managment_System.csv", index=False)
    print("✅ Dataset generated Successfully! File saved as 'Superstore_Management_System.csv'")

except PermissionError:
    print("⚠ Please close the file 'Superstore_Management_System.csv' if it's open in Excel or Power BI")

