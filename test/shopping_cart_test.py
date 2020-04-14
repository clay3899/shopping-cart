from datetime import datetime
from datetime import date
from app.shopping_cart import calculate_total_price, to_usd, find_product, human_friendly_timestamp



def test_to_usd():
    # it should apply USD formatting
    assert to_usd(4.50) == "$4.50"

    # it should display two decimal places
    assert to_usd(4.5) == "$4.50"

    # it should round to two places
    assert to_usd(4.55555) == "$4.56"

    # it should display thousands separators
    assert to_usd(1234567890.5555555) == "$1,234,567,890.56"

def test_find_product():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    # if there is a match, it should find and return a product
    matching_product = find_product("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

   
def test_human_freindly_timestamp():
    date = datetime.now()
    friendly = human_friendly_timestamp(date)

    assert friendly == date.strftime("%m/%d/%Y %I:%M:%S%p")


def test_calculate_total_price():
    subtotal1 = 20.00
    tax1 = .06
    subtotal2 = 30.00
    tax2 = .0875
    # if there is a match, it should calculate total price
    calculate_total_price(subtotal1, tax1)
    final1 = calculate_total_price(subtotal1, tax1)
    final2 = calculate_total_price(subtotal2, tax2)
    assert final1 == "$21.20"
    assert final2 == "$32.62"