# shopping_cart.py
from datetime import datetime

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

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

print(products)

#define function that gives name and price of product with id in list [items]

def matchproduct(selectedid): 
    v = list(filter(lambda d: d['id'] == selectedid, products))
    return v



#quit with "done"

items = []

newitem = ''
while newitem != 'done':
    newitem = input("Enter Product Identifier (from 1 to 20), or enter 'done' to print receipt: ")
    if newitem != 'done':
        #make newitem a float or int before appending!
        items.append(int(newitem))

print(items)

#remove any item greater than 20
#check items in "items" list against id in "products" and create new list

newlist = []
for i in items:
    if i < 20:
        v = matchproduct(i)
        newlist.append(v)
print("newlist:", newlist)


#remove addl brackets from the list, doesn't work:
#newlist = (newlist)[1:-1] 


#get the name of the items from our newlist
#next((i for i, item in enumerate(newlist) if item["id"] == 2), None)

x = newlist[0]
x = x[0]
print(x)
print(type(x))
print("selected:" , x["name"] , "" , x["price"])


#seq = [x['id'] for x in newlist]
#print(seq)








#def nameprice(x):
#new_dict = [a for a, b in my_dict.items() if 6 in b]
#use the below code to loop through items list

#if id value from projects in items:
    

#res = next((sub for sub in products if sub['id'] = ???), None) 

#print(str(res))

#create new list with product name and price


#BEGIN RECEIPT
now = datetime.now()
checkout_time = now.strftime("%D %I:%M %p")

print("---------------------------------")
print("Kim's Convenience Store")
print("www.kimsconvenience.ca")
print("---------------------------------")
print("Checkout at :", checkout_time)
print("---------------------------------")
print("SELECTED PRODUCTS:")

#TAX Calculation: https://realpython.com/list-comprehension-python/
#costs = [list of item prices]
#taxrate = .0875
#def taxprice(tx):
#    return tx *(1+taxrate)
#finaltotal = [taxprice(i) for i in costs]
#subtotal = add up total for costs and convert to USD using to_usd function
# print("SUBTOTAL: ",subtotal)
#taxcost = subtract subtotal from finaltotal
#print("TAX: ",taxcost)
#totalcost = sum values in finaltotal
#print("TOTAL: ",totalcost)
#print("---------------------------------")
#print("THANKS, SEE YOU SOON!")
#print("---------------------------------")


#use link instructions to email the receipts:
#https://github.com/prof-rossetti/notification-service-py