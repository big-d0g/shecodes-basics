# PROJECT: RECEIPTS FOR LOVELY SEATS.  Creating receipts for customers of a furniture store.  Storing descriptions and prices of the store catalog in variables and then processing and printing receipts for customers to the output terminal.

# Lovely Loveseat Details
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

# Stylish Settee Details
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

# Luxurious Lamp Details
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

# Sales Tax
sales_tax = 0.088

# FIRST CUSTOMER!
customer_one_total = 0
customer_one_itemization = ""

# Customer decides to buy Lovely Loveseat

customer_one_itemization += lovely_loveseat_description
customer_one_total += lovely_loveseat_price

# Customer decides to buy Luxurious Lamp 

customer_one_itemization += luxurious_lamp_description
customer_one_total += luxurious_lamp_price

# Total plus Tax

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items: " + customer_one_itemization)
print("Customer One Total: "  + str(customer_one_total)) 