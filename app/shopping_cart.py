# shopping_cart.py

#from pprint import pprint
from datetime import datetime
from datetime import date


userChoice = "0"
shopping_cart = []

total_tax = 0.00
tax = .0875
iterator = 0
matching_product = 0
matching_products =[]
all_ids = []

def to_usd(my_price):
    """ returns the parameter in a 
    standard USD $ format to simplify the  
    formatting."""
 
    return f"${my_price:,.2f}"

def human_friendly_timestamp(now):
    """Creates a human friendly timestamp of the 
    current time. no parameter required."""
    
    
    return now.strftime("%m/%d/%Y %I:%M:%S%p")

def find_product(product_id, all_products):
    """ looks up a product given its unique identifier
    ... from a provided list of products"""
    
    matching_products = [p for p in all_products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    return matching_product
    
def calculate_total_price(subtotal_price, tax_rate):
   """ Loops through the selected items list
   to find the price of each item and find subtotal/tax/total
   the function is designed to simplify cost calculation in the code."""
   total_price = subtotal_price + (subtotal_price * tax_rate)
   return to_usd(total_price) 

if __name__ == "__main__":

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
    now = datetime.now()

    print(divider)
    print("WHOLE FOODS MARKET")
    print("www.wholefoodsmarket.com")
    print(divider)
    print("CHECKOUT AT: ", human_friendly_timestamp(now))
    print(divider)
    print("SELECTED PRODUCTS: ")
    
    subtotal = 0.00

    for userChoice in shopping_cart:
        matching_product = find_product(userChoice, products)
        print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")
        subtotal = subtotal + matching_product["price"]
    
    print(divider)
    
    print(f"SUBTOTAL: {to_usd(subtotal)} ")
    print(f"TAX: {to_usd(subtotal * tax)}")
    print(f"TOTAL: {calculate_total_price(subtotal, tax)} ")
    print(divider)

    print("THANKS, SEE YOU AGAIN SOON!")
    print(divider)

    





#print(shopping_cart)