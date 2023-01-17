items=[]
while True:
    print("-----------------------------Welcome to the supermarket-----------------------------")
    print(" 1. View Item \n 2. Add Item \n 3. Purchase Item \n 4. Search Item \n 5. Remove Item \n 6. Exit Store")
    choice = int (input("Enter a number of your choice: "))
    if choice==1:
        print("------------View Item------------")
        print("The number of items in the inventory are %d:" %len(item))
        if len(item)!=0:
            print("Here are the list of items available in the supermarket")
            for item in items:
                for key,value in item.items():
                    print(key,value)

    elif choice==2:
        print("------------Add Item------------")
        print("To add an item fill the form")
        item={}
        while True:
            try:
                item["name"]=input("Enter the item: ")
                break
            except ValueError:
                print("Enter the item name in character and not number!!")
            
        
        while True:
            try:
                item["quantity"]=int(input("Enter the quantity: "))
                break
            except ValueError:
                print("Enter the number for quantity and not string!!")
         
        while True:
            try:
                item["price"]=float(input("Enter the price: "))
                break
            except ValueError:
                print("Enter the number for price and not string!!")
            
        print("Item has been successfully added")
        items.append(item)

    elif choice==3:
        print("------------Purchase Item------------") 
        print(items)
        purchase_item=input("Which item do you want to purchase? Enter name: ")
        purchase_item_qty=int(input("Enter the item quantity you want to purchase"))
        for item in items:
            if item["name"].lower()==purchase_item.lower():
                if item["quantity"]!=0:
                    if item["quantity"] >= purchase_item_qty:
                        print("Pay " +str(item["price"]*purchase_item_qty)+" at checkout")
                        item["quantity"]-=purchase_item_qty
                    else:
                        print("Only %d quantity available", item["quantity"])
                    
                else:
                    print("Item not present")
            else:
                print("Incorrect item name")

    elif choice==4:
        print("------------Search Item------------") 
        print(items)
        find_item=input("Which item do you want to search? Enter name: ")
        for item in items:
            if item["name"].lower()==find_item.lower():
                print("Item named " +find_item +" is available in the inventory with details")
                print(item)
            else:
                print("Item not present")
                

    elif choice==5:
        print("------------Remove Item------------") 
        print(items)
        remove_item=input("Which item do you want to Remove? Enter name: ")
        for item in items:
            if item["name"].lower()==remove_item.lower():
                print("Here are the details of:" + remove_item)
                print(item)
                item["name"]=input("Enter the item you want to add in place of removed item: ")
                
                while True:
                    try:
                        item["quantity"]=int(input("Enter the quantity: "))
                        break
                    except ValueError:
                        print("Enter the number for quantity and not string!!")
         
                while True:
                    try:
                        item["price"]=float(input("Enter the price: "))
                        break
                    except ValueError:
                        print("Enter the number for price and not string!!")
                 
            else:
                print("Item not present")
                
    elif choice==6:
        print("------------Exit Store------------") 
        break

    else:
        print("You entered an invalid option")
                