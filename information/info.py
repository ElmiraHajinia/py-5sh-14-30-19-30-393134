






list_info=[]
list_userPass=[]
def information(name:str,family:str,age:int,email:str,phone:str,user:str,password:str):
    list_info.append(name)
    list_info.append(family)
    if age>18:
        list_info.append(age)
    else:
        print("gheire mojaz")
    sex=input("1.agha 2.khanoom 3.sayer===")
    match sex:
        case "1":
            agha="agha".strip()
            list_info.append(agha)
        case "2":
            khanoom="khanoom".strip() 
            list_info.append(khanoom)   
        case "3":
            sayer="sayer".strip()
            list_info.append(sayer)   
    edu=input("1.lisanse 2.fogh 3.phd 4.sayer===")  
    match edu:
        case "1":
            lisanse="lisanse".strip()
            list_info.append(lisanse) 
        case "2":
            fogh="fogh".strip() 
            list_info.append(fogh)   
        case "3":
            phd="phd".strip()
            list_info.append(phd)
        case "4":
            sayer="sayer".strip()
            list_info.append(sayer)   
    if email.endswith("@gmail.com")==True:
        list_info.append(email)
    else:
        print("email sahih nemibashad")
    
    if len(phone)==11:
        list_info.append(phone)
    else:
        print("shomare sahih nemibashad")    

    if user.isalnum()==True and len(user)>6:
        list_userPass.append(user)   
    if password.isascii()==True and len(password)>8:
        list_userPass.append(password)   
    userPass=tuple(list_userPass)
    list_info.append(userPass)
    return list_info
    return list_userPass