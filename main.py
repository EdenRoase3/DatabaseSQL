import database


MENU_PROMPT = """

Hello! Welcome to the Farmer's Market. Please proceed to self-checkout


Please choose from theese options:

1) Add new product
2) See all products
3) Get product info by Name
4) Get price for product
5) Display products greater than selected value
6) Display prouducts lower than selected value
7) Display products with prices in between 0-100
8) Display products with prices in between 100-500
9) Update product by id 
10) Update product by name
11) Delete product by Name
12) Delete product by id
13) Sort by price (high to low)
14) Sort by price (low to high)

15) EXIT

Your selection: """

try:
    def menu():
        connection = database.connect()
        database.create_tables(connection)
    
        while(user_input := input(MENU_PROMPT)) != '15':
            if user_input == '1':
                name = input("Enter product name: ")
                shop = input("Product shop: ")
                weight = float(input("Enter weight(lbs): "))
                price =  float(input("Enter product price: "))
                shelf = input("Enter shelf life in weeks: ")
    
                database.add_product(connection, name, shop, weight, price, shelf)
    
                   
            elif user_input == '2':
                products = database.get_all_products(connection)
    
                for product in products:
                    print(f"\n product {product[0]}  {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")
    
            elif user_input == '3':
                name = input("Enter product name to find: ")
                products = database.get_products_by_name(connection,name)
    
                for product in products: 
                    print(f"\n product {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")
                    
                
            elif user_input == '4':
                name = input("Enter product name to find: ")
                price = database.get_price_for_product(connection,name)
    
                print(f"The price per pound of {name} is ${price[4]} ")


            elif user_input == "5":
                price = input("Display by products with a price grater than:")
                products = database.get_by_greatthan(connection,price)
                
                for product in products:
                    print(f"\n product {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")      

            elif user_input == "6":
                price = input("Display by products with a price lower than: ")
                products = database.get_by_lowerthan(connection,price)
                
                for product in products:
                    print(f"\n product {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")


            elif user_input == "7":
                products = database.get_by_range100(connection)
                
                for product in products:
                    print(f"\n product {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")
                
            elif user_input == "8":
                products = database.get_by_range100_500(connection)
                
                for product in products:
                    print(f"\n product {product[1]} from ({product[2]}) -- {product[3]} lbs  and costs ${product[4]} /lbs -- Lasts refrigerated {product[5]} weeks!")
                
            elif user_input == '9':
                print("***RECOMENDED TO VISIT OPTION #2 TO REVISE INFO BEFORE UPDATING")
                name = input("Enter product name: ")
                newid  = input("Enter new id(Product #): ")
                products = database.update_product_id(connection, name, newid)
                print(f"Changed {name} id to {newid}")
         
    
            elif user_input == '10':
                print("***RECOMENDED TO VISIT OPTION #2 TO REVISE INFO BEFORE UPDATING")
                name = input("Enter product name to update: ")
                newname = input("Enter new name: ")
                products = database.update_product_name(connection,name, newname)
                print(f"Changed {name} name to {newname}")
            
            elif user_input == '11':
                print("***RECOMENDED TO VISIT OPTION #2 TO REVISE INFO BEFORE DELETING")
                name = input("Enter product name to delete: ")
                question = input(f"Would you like to delete product #{name}? (Y or N)")
                print(question)
                if (question == "Y"):
                    products = database.delete_product(connection,name)      
                    print(f"Product {name} deleted")

            elif user_input == "12":
                print("***RECOMENDED TO VISIT OPTION #2 TO REVISE INFO BEFORE DELETING")
                id = input("Please enter product Id(Product #) to delete: ")
                question = input(f"Would you like to delete product #{id}? (Y or N)")
                print(question)
                if (question == "Y"):
                    products = database.delete_by_ID(connection, id)
                    print(f"Product {id} deleted")
                    print("*NOTE* Product ID has changed due to UNIQUE PROUDCT, unless asssigned to a specific product, product ID will not be assigned to current products")
    
            elif user_input == "13":
                products = database.order_by_price_hightolow(connection)
                for product in products: 
                    print(f"Product {product[1]} - Price {product[5]}$")

                    
            elif user_input == "14":
                products = database.order_by_price_lowtohigh(connection)
                for product in products: 
                    print("\n" + f" Product {product[1]} - Price {product[5]}$")


            elif user_input == "17":
                price = input("Search for a price greater than: ")
                price1 = input("Please enter another price lower than: ")
                products = database.get_by_range(connection, price, price1)
                for product in products: 
                    print("\n" + f" Product {product[1]} - Price {product[5]}$")
                
                
            else:
                print("Please enter a correct input. Please try again!")
   
except TypeError:
    print("Entered wrong data, please try again")

menu()

