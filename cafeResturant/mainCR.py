from sefaresh import*
while True:

    menu=input("1.resturant 2.cafe 3.exit")
    match menu:
        case "1":
            while True:
                menu_food=input("1.pizza 1000 2.pasta 800 3.sandwich 600 4.exit =====").strip()
                match menu_food:
                    case "1":
                        pizza()
                    case "2":
                        pasta()
                    case "3":
                        sandwich()
                    case "4":       
                        break
        case "2":            
            while True:        
                menu_drink=input("1.aab 30  2.cola 70  3.fanta 60 4.exit ======").strip()
                match menu_drink:   
                    case "1":
                        aab()
                    case "2":
                        cola()
                    case "3":
                        fanta()
                    case "4":       
                        break 
        case "3":
            break   
print("mablagheFood=",resid_food)        
print("mablagheDrink=",resid_drink) 
print("mablagheKole=",resid())                   
