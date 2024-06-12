import random
import tabulate

items = {}

# CREATING DEALERS FILE
dealers = {1: ["Anne", "0716482642", "Colombo"], 2: ["Roy", "0789214625", "Kadawatha"],
           3: ["Tom", "0775468291", "Gampaha"], 4: ["Jerry", "0339554561", "Kadawatha"],
           5: ["John", "0116646175", "Veyangoda"], 6: ["Lisa", "0334635975", "Moratuwa"]}
with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers.txt", "w") as dealers_details:
    dealers_details.write(str(dealers))

# CRATING DEALERS ITEMS FILE
dealers_items = {"Anne": [["16' curved monitor", "Samsung", 160000.00, 10], ["32' TV", "LG", 220000.00, 3],
                          ["Speaker system", "JBL", 16000.00, 5]],
                 "Roy": [["WiFi", "Huawei", 8000.00, 10], ["WiFi extender", "tp-link", 5000.00, 5],
                         ["Extension Chord", "Orange", 9000.00, 5]],
                 "Tom": [["Printer", "HP", 13000.00, 5], ["Camera", "Hikvision", 20000.00, 7],
                         ["Hard disk", "Seagate", 10000.00, 10]],
                 "Jerry": [["Folders", "Atlas", 500.00, 20], ["Network cable", "Orange", 300.00, 20],
                           ["AC", "Abans", 28000.00, 5]],
                 "John": [["Chair", "Damro", 5000.00, 30], ["Computer table", "Damro", 15000.00, 20],
                          ["Keyboard", "Logitech", 8000.00, 20]],
                 "Lisa": [["Headphone", "ASUS", 10000.00, 20], ["Mouse", "Logitech", 8000.00, 20],
                          ["Light", "DIMO", 10000.00, 15]]}
with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers_items.txt", "w") as dealers_items_file:
    dealers_items_file.write(str(dealers_items))


def instructions():
    print("\n________________________________'ONE NET CAFE' Inventory Manage System________________________________\n")
    print("Instructions:\n")
    print("Type AID for Adding item details.")
    print("Type DID for Deleting item details.")
    print("Type UID for Updating item details.")
    print("Type VID for Viewing the items table.")
    print("Type SID for Saving the item details to the text file at any time.")
    print("Type SDD for Selecting four dealers randomly from a file.")
    print("Type VRL for Displaying all the details of the randomly selected dealers.")
    print("Type LDI for Display the items of the given dealer.")
    print("Type ESC to Exit the program.")
    print("\n----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------------------------------------")


instructions()


def menu():
    print("\n----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------------------------------------"
          "\n")
    print("AID - Adding item details")
    print("DID - Deleting item details")
    print("UID - Updating item details")
    print("VID - Viewing the items table")
    print("SID - Saving the item details")
    print("SDD - Selecting four dealers randomly")
    print("VRL - Displaying all the details of the randomly selected dealers")
    print("LDI - Display the items of the given dealer")
    print("ESC - Exit the program")


def user_input():
    answer = str(input("\nEnter the keyword: "))
    print("\n----------------------------------------------------------------------------------------------------------"
          "-----------------------------------------------------------------------------------------------------------")
    if answer == "AID":
        adding_item_details()
    elif answer == "DID":
        deleting_item_details()
    elif answer == "UID":
        updating_item_details()
    elif answer == "VID":
        view_items_table()
    elif answer == "SID":
        print("\n**************************************** SAVED SUCCESSFULLY ****************************************")
        saving_item_details()
    elif answer == "SDD":
        select_dealers_randomly()
    elif answer == "VRL":
        displaying_randomly_selected_dealers()
    elif answer == "LDI":
        display_items_of_the_dealer()
    elif answer == "ESC":
        exit_the_program()
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WRONG KEYWORD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        menu()
        user_input()


def adding_item_details():
    item_code = int(input("\nEnter item code: "))
    item_name = input("Enter item name: ")
    item_brand = input("Enter item brand: ")
    item_price = float(input("Enter item price(Rs.): "))
    item_quantity = int(input("Enter item quantity: "))
    item_category = input("Enter item category: ")
    item_purchased_date = input("Enter item purchased date (YYYY/MM/DD): ")

    # Creating a list for the entries
    items[item_code] = [item_name, item_brand, item_price, item_quantity, item_category, item_purchased_date]
    print("\n**************************************** ITEM ADDED ****************************************")
    saving_item_details()

    menu()
    user_input()


def deleting_item_details():
    item_code = int(input("\nEnter the item code to DELETE: "))

    # Search for item code in the list
    if item_code in items:
        del items[item_code]
        print("\n**************************************** ITEM DELETED ****************************************")
        saving_item_details()
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ITEM NOT FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    menu()
    user_input()


def updating_item_details():
    item_code = int(input("\nEnter the item code to UPDATE: "))
    # Changing the values in the list
    if item_code in items:
        item_name = input("\nUpdate item name: ")
        items[item_code][0] = item_name
        item_brand = input("Update item brand: ")
        items[item_code][1] = item_brand
        item_price = float(input("Update item price(Rs.): "))
        items[item_code][2] = item_price
        item_quantity = int(input("Update item quantity: "))
        items[item_code][3] = item_quantity
        item_category = input("Update item category: ")
        items[item_code][4] = item_category
        item_purchased_date = input("Update item purchased date (YYYY/MM/DD): ")
        items[item_code][5] = item_purchased_date

        # CUpdating the list for the entries
        items[item_code] = [item_name, item_brand, item_price, item_quantity, item_category, item_purchased_date]
        print("\n**************************************** ITEM UPDATED ****************************************")
        saving_item_details()
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ITEM NOT FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    menu()
    user_input()


def view_items_table():
    print("\n")
    headers = ["ITEM CODE", "ITEM NAME", "ITEM BRAND", "ITEM PRICE(Rs.)", "ITEM QUANTITY", "ITEM CATEGORY",
               "ITEM PURCHASED DATE", "ITEM TOTAL PRICE(Rs.)"]
    # Add current_total to the list
    for item_code in items:
        item_price = items[item_code][2]
        item_quantity = items[item_code][3]
        current_total = item_price * item_quantity
        items[item_code].append(current_total)

    # Creating the table
    table = []
    for key, value in items.items():
        table.append([key] + value)
    # Sorting the table
    table = sorted(table, key=lambda x: x[0], reverse=True)
    print(tabulate.tabulate(table, headers=headers))

    menu()
    user_input()


def saving_item_details():
    # Creating a text file for items
    with open("items.txt", "w") as item_details:
        item_details.write(str(items))

    menu()
    user_input()


def select_dealers_randomly():
    # Reading the dealers text file
    with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers.txt", "r") as dealers_file:
        x = dealers_file.read()

    # Creating a new list for the list in the text file
    new_dic = eval(x)

    # Selecting 4 random dealers out of 6
    keys = random.sample(list(new_dic.keys()), 4)
    dic = {key: new_dic[key] for key in keys}

    # Saving the 4 random dealers in the text file
    with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers.txt", "w") as random_dealers:
        random_dealers.write(str(dic))
        print("\n**************************************** 4 DEALERS ARE SELECTED RANDOMLY *****************************"
              "***********")

    menu()
    user_input()


def displaying_randomly_selected_dealers():
    # Reading the dealers text file
    with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers.txt", "r") as dealers_file:
        x = dealers_file.read()

    # Creating a new list for the list in the text file
    dic = eval(x)

    # Creating the table
    headers = ["\nNAME", "\nCONTACT NO.", "\nLOCATION"]
    rows = []
    for key, values in dic.items():
        rows.append(values)

    # Sorting the table according to Location without using sorted function
    num = len(rows)
    for i in range(num):
        for j in range(0, num-i-1):
            if rows[j][2] > rows[j+1][2]:
                rows[j], rows[j+1] = rows[j+1], rows[j]

    print(tabulate.tabulate(rows, headers=headers))

    menu()
    user_input()


def display_items_of_the_dealer():
    # Reading dealers_items text file
    with open("../../../Downloads/20221544_2313474_S.A. Chulan Shammika 2/dealers_items.txt", "r") as file:
        x = file.read()

    # Creating a new list for the list in the text file
    dic = eval(x)

    dealer_name = str(input("\nEnter any name from selected dealers: "))

    # View the items table of the dealer
    headers = ["\nITEM NAME", "\nITEM BRAND", "\nITEM PRICE(Rs.)", "\nITEM QUANTITY"]
    if dealer_name in dic:
        table = []
        for values in dic[dealer_name]:
            table.append(values)
        print("\n", dealer_name, "'s Items: ")
        print(tabulate.tabulate(table, headers=headers))
    else:
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WRONG NAME !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    menu()
    user_input()


def exit_the_program():
    user = input("\nAre you sure you want to EXIT (YES or NO): ")
    if user == "YES":
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PROGRAM ENDED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        exit()
    elif user == "NO":
        menu()
        user_input()


user_input()
