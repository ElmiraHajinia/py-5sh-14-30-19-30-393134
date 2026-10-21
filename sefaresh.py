resid_food=[]
resid_drink=[]

def pizza():
    num1=int(input("tedad=="))
    mablagh1=1000*num1
    resid_food.append(mablagh1)
    return mablagh1
def pasta():
    num2=int(input("tedad=="))
    mablagh2=800*num2
    resid_food.append(mablagh2)
    return mablagh2  
def sandwich():
    num3=int(input("tedad=="))
    mablagh3=600*num3
    resid_food.append(mablagh3)
    return mablagh3 

def aab():
    num4=int(input("tedad=="))
    mablagh4=30*num4
    resid_drink.append(mablagh4)
    return mablagh4

def cola():
    num5=int(input("tedad=="))
    mablagh5=70*num5
    resid_drink.append(mablagh5)
    return mablagh5  

def fanta():
    num6=int(input("tedad=="))
    mablagh6=60*num6
    resid_drink.append(mablagh6)
    return mablagh6 

def resid():
    hazineF=0
    for i in resid_food:
        hazineF=hazineF+i

    hazineD=0
    for j in resid_drink:
        hazineD=hazineD+j

    mablaghK=(hazineD+hazineF)*1.1
    return mablaghK