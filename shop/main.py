



from shop import*

while True:

    menu=input("1.add 2.show 3.search 4.edit 5.delete 6.exit===")
    match menu:
        case "1": 
            while True:
                product_id=input("1.enter product's id or 2.exit===")
                match product_id:
                    case "1":
                        product_id=int(input("enter product's id==="))
                        name=input("name===")
                        price=int(input("price==="))
                        add(product_id,name,price)
                    case "2":
                        break
        case "2":
            print(products)    
            
        case "3":
            while True:
                search=input("1.enter product_id or 2.exit===")
                match search:
                    case "1":
                        product_id=int(input("enter product's id==="))
                        searchhh(product_id)
                    case "2":
                        break
        case "4":
            while True:
                edit=input("1.enter product_id or 2.exit===")
                match edit:
                    case "1":
                        product_id=int(input("enter product's id==="))
                        if product_id in products:
                            name=input("name===")
                            price=int(input("price==="))
                            update(product_id,name,price)
                        else:
                            print("wrong product_id")
                            continue
                    case "2":
                        break        
        case "5":
            while True:
                delete=input("1.enter product_id or 2.exit===")
                match delete:
                    case "1":
                        product_id=int(input("enter product's id==="))
                        if product_id in products:
                            deleteee(product_id)

                        else:
                            print("wrong product_id")
                            continue
                    case "2":
                        break 
        case "6":
            break

print(products)       

                