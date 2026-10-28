

from sefaresh import *
while True:
    food=input("1.pizza 1000 2.pasta 800 3.sandwich 600 4.khorooj===")
    match food:
        case "1":
            num=int(input("tedad==="))
            hazine=1000
            ghaza(num,hazine)
        case "2":
            num=int(input("tedad==="))
            hazine=800
            ghaza(num,hazine)
        case "3":
            num=int(input("tedad==="))
            hazine=600
            ghaza(num,hazine)
        case "4":
            break

while True:
    drink=input("1.aab 30 2.cola 70 3.fanta 70 4.khorooj===")
    match drink:
        case "1":
            num=int(input("tedad==="))
            hazine=30
            nooshidani(num,hazine)
        case "2":
            num=int(input("tedad==="))
            hazine=70
            nooshidani(num,hazine)
        case "3":
            num=int(input("tedad==="))
            hazine=70
            nooshidani(num,hazine)
        case "4":
            break
gheymat=0
for i in factor:
    gheymat=gheymat+i
pardakhti=gheymat*1.1 
print(pardakhti)
print(factor)