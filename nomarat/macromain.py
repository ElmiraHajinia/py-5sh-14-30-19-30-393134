
tarikhh=[]
zistt=[]
riazii=[]
def riazi():
    riazii.append(num)
def tarikh():
    tarikhh.append(num)
def zist():
    zistt.append(num)
def aveeR():
    num=0
    for i in riazii:
        num=i+num
    aveR=num/len(riazii)
    print(aveR)
def aveeT():
    num=0
    for i in tarikhh:
        num=i+num
    aveT=num/len(tarikhh)  
    print(aveT)   
def aveeZ():
    num=0
    for i in zistt:
        num=i+num
    aveZ=num/len(zistt) 
    print(aveZ)
while True:
    command=input("1.riazi  2.tarikh  3.zist  4.avee  5.exit======") 
    if command=="1":
        num1=input("num=")
        num=int(num1)  
        riazi()
    elif command=="2":
        num2=input("num=")
        num=int(num2)  
        tarikh()  
    elif command=="3":
        num3=input("num=")
        num=int(num3)  
        zist()    
    elif command=="4":
        aveeT()
        aveeR()
        aveeZ()
    elif command=="5":
        break
print(riazii) 
print(zistt)
print(tarikhh)  
      