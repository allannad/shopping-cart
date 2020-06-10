# shopping_cart.py
from datetime import datetime
import os
from dotenv import load_dotenv

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

#print(products)

#define function that gives name and price of product with id in list [items]

def matchproduct(selectedid): 
    v = list(filter(lambda d: d['id'] == selectedid, products))
    return v

#TAX Calculation: https://realpython.com/list-comprehension-python/

#Tax Rate is variable and based on user input
#taxrate = float(input("Enter tax rate as 0.XXX: "))
#print(type(taxrate))
load_dotenv()

taxrate = float(os.getenv("tax_rate"))
def taxprice(tx):
    return tx *(1+taxrate)



items = []

newitem = ''
while newitem != 'done':
    newitem = input("Enter Product Identifier (from 1 to 20), or enter 'done' to print receipt: ")
    #quit with "done"
    if newitem != 'done':
        #make newitem a float or int before appending!
        items.append(int(newitem))
        if int(newitem) > 20:
            print("Invalid item, re-enter.")
#remove any item greater than 20
#check items in "items" list against id in "products" and create new list

newlist = []
for i in items:
    if i < 20:
        v = matchproduct(i)
        newlist.append(v)
#print("newlist",newlist)

#get the name of the items from our newlist

itemslist = []
for x in newlist:
    for i in x:
        itemslist.append(i)
#print("itemslist:",itemslist)


#pared down list
names = [x['name'] for x in itemslist]
#print("names:", names)
prices = [x['price'] for x in itemslist]
#print("prices",prices)
formattedprices = ["($%.2f)" % x for x in prices]
#print("formattedprices",formattedprices)


#multiple items in dictionaries cause the key value pairing not to work with duplicate items
#arr={}
#for key in names: 
#    for value in formattedprices: 
#        arr[key] = value 
#        #formattedprices.remove(value) 
#        break 
#print("arr:",arr)


#use a list rather than dictionary to then use this for selected items
arr = list(zip(names, formattedprices)) 


#when was the checkout?
now = datetime.now()
checkout_time = now.strftime("%D %I:%M %p")

#do the money calculation
subtotal = [i for i in prices]
subtotal = sum(subtotal)
formattedsubtotal = to_usd(subtotal)
finaltotal = [taxprice(i) for i in prices]
finaltotal = sum(finaltotal)
formattedfinaltotal = to_usd(finaltotal)
tax = finaltotal - subtotal
formattedtax = to_usd(tax)

#-----------------------------------------
#BEGIN RECEIPT

print("---------------------------------")
print("Kim's Convenience Store")
print("www.kimsconvenience.ca")
print("---------------------------------")
print("Checkout at:", checkout_time)
print("---------------------------------")
print("SELECTED PRODUCTS:")
for i in arr:
    print("...",*i)
print("---------------------------------")
print("SUBTOTAL:", formattedsubtotal)
print("TAX:", formattedtax)
print("TOTAL:", formattedfinaltotal)
print("---------------------------------")
print("THANK YOU, SEE YOU SOON!")
print("---------------------------------")

#create list of items bought into .csv file
import os
import csv

csv_file_path = os.path.join(os.path.dirname(__file__), "receipts", "inventory.csv")


pareddownitemslist = itemslist

toCSV = pareddownitemslist
keys = toCSV[0].keys()
with open(csv_file_path, 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)



#use link instructions to email the receipts:
#https://github.com/prof-rossetti/notification-service-py

