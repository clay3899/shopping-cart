# shopping_cart.py

#from pprint import pprint
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
tax= os.environ.get("TAX")




products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output
userChoice = "0"
shopping_cart = []
total_price = 0.00
total_tax = 0.00
subtotal = 0.00
iterator = 0
matching_product = 0
matching_products =[]
all_ids = []

for product in products:
    id_val =  str(product["id"])
    all_ids.append(id_val)

while userChoice != "DONE":
    
    userChoice = input("Please input the product identifier: ")
    
    if userChoice == "DONE" or userChoice == "done":
        break
    elif userChoice in all_ids:
        shopping_cart.append(userChoice)
    else:
        print("That item is not in the list")
        pass
    

    

    pass




divider ="----------------------------------"
print(divider)
print("WHOLE FOODS MARKET")
print("www.wholefoodsmarket.com")
print(divider)


today = date.today()
now = datetime.now()
print("CHECKOUT AT: ", now.strftime("%Y/%m/%d %H:%M:%S"))

print(divider)

print("SELECTED PRODUCTS: ")
for userChoice in shopping_cart:
    matching_products = [product for product in products if str(product["id"]) == str(userChoice)]
    matching_product = matching_products[0]
    print(" + " + matching_product["name"] + " ($" + str("{0:.2f}".format(matching_product["price"])) + ")")
    subtotal = subtotal + float(matching_product["price"])
    total_tax = total_tax + (float(matching_product["price"]) * float(tax))
    total_price = total_price + (float(matching_product["price"]) * (1 + float(tax)))
    pass




print(divider)
print("SUBTOTAL: " + " $" + str("{0:.2f}".format(subtotal)))
print("TAX: " + " $" + str("{0:.2f}".format(total_tax)))
print("TOTAL: " + " $" + str("{0:.2f}".format(total_price)))
print(divider)
print("THANKS, SEE YOU AGAIN SOON!")
print(divider)

   



    

#print(shopping_cart)