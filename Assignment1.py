# Assignment1
# ETG-Skill-India Python for AI/ML Internship
# Name: Aditi Hegde
# Email: aditimsh@gmail.com
# Batch-2
# Program for inventory management


# Program is written and comipled on PyCharm


import json
import os
import time
clear = lambda: os.system('cls')

# Code to read and load json file
fd = open("productlist.json",'r')
r = fd.read()
fd.close()

record = json.loads(r)
print(record)

# Defining the function addItemToInventory which will add items to the inventory
def addItemToInventory():
    clear()
    print("ADD ITEMS TO THE INVENTORY")
    print("----------------------")
    print()
    # Asking user to add number of items they want to add to inventory
    ui_num = int(input("enter number of items you want to add to the inventory"))
    # Asking user for product name, product Id, Price and quantity of the item
    for i in range(ui_num):
      prod_id = str(input("Enter product id:"))
      name = str(input("Enter name:"))
      pr = int(input("Enter price:"))
      qn = int(input("Enter quantity:"))
      print("The details of item added is:")
      record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}
      print(record[prod_id])
      t = time.ctime()
      print("The inventory loading transaction time is:")
      print(t)

    js = json.dumps(record)

    cs = open("productlist.json", 'w')
    cs.write(js)
    cs.close()

    js = json.dumps(record)
    # Updating record after Transaction
    with open("productlist.json", 'w') as fd:
      fd.write(js)
      fd.close()
    print("The updated record after adding the items:")
    print(record)


# Defining the function Purchase items which will purchase items from the inventory
def purchaseitems():
    clear()
    print("PURCHASE ITEMS FROM THE INVENTORY")
    print("----------------------")
    print()
    i = 0
    sum = 0
    # Asking user to add number of items they want to add to inventory
    ui_num = int(input("enter number of items you want to purchase"))
    # Asking user for product name, product Id, Price and quantity of the items
    for i in range(ui_num):
        ui_prod = str(input("Enter the product_Id: "))
        ui_quant = int(input("Enter the quantity: "))

        print("Product: ", record[ui_prod]['name'])
        print("Price: ", record[ui_prod]['pr'])
        sum = sum+record[ui_prod]['pr'] * ui_quant;
        print("Billing Amount of item: ", record[ui_prod]['pr'] * ui_quant)
        record[ui_prod]['qn'] = record[ui_prod]['qn'] - ui_quant
        total_bill=sum
        print("the total bill is:")
        print(total_bill)
        t = time.ctime()
        print("The inventory purchasing transaction time is:")
        print(t)


    js = json.dumps(record)

    cs = open("productlist.json", 'w')
    cs.write(js)
    cs.close()

    js = json.dumps(record)
    # Updating record after Transaction
    with open("productlist.json", 'w') as fd:
      fd.write(js)
      fd.close()
    print("The updated record after purchasing the items:")
    print(record)



print("INVENTORY MANAGEMENT SYSTEM")
print("--------------------")
print()
print("Available Options:")
print()
print(" Choose 1 - To Add Items To Inventory")
print(" Choose 2 - To Purchase From Inventory")
print()

# Asking users to chose their transaction type
# That is do they want to add items to inventory
# Or purchase items from inventory
while True:
        userChoice = input("Choose An Option: ")
        if userChoice == '1':
            print("add items")
            addItemToInventory()
            break
        elif userChoice == '2':
            print("purchase items")
            purchaseitems()
            break
        else:
            print("please enter valid input")
            break

