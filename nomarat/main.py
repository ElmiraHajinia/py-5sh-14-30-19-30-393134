from riazi import *
from tarikh import *
from zist import *
while True:
    command=input("1.riazi  2.tarikh  3.zist  4.avee  5.exit") 
    match command:
        case "1":
    
            num1=input("num=")
            num=int(num1)  
            riazi(num)
        case "2":
            num2=input("num=")
            num=int(num2)  
            tarikh(num)  
        case"3":
            num3=input("num=")
            num=int(num3)  
            zist(num)    
        case "4":
            aveeT()
            aveeR()
            aveeZ()
        case "5":
            break
print(riazii) 
print(zistt)
print(tarikhh)  