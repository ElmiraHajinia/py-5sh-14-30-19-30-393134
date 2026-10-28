

from  info1 import*
while True:
    entekhab=input("1.vorood 2.sabtenaam 3.exit===")
    match entekhab:
        case "1":
            user=input("username===")
            password=input("password===")
            if user and password in list_userPass:
                print("vorood mojaz")
            else:
                print("sabtenaam konid")    
        case "2":
            while True:
                dastoor=input("1.info 2.exit===")
                match dastoor:
                    case "1":
                        name=input("name===").strip().capitalize()
                        family=input("family===").strip().capitalize()
                        age=int(input("age==="))
                        email=input("email===")
                        phone=input("phone===")
                        user=input("username===")
                        password=input('password===')
                        information(name,family,age,email,phone,user,password)
                        print(list_info) 
                    case "2":
                            break        
                   

        case "3":
            break          















