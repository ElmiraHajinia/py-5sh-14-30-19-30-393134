riazii=[]
def riazi(num):
    riazii.append(num)

def aveeR():
    num=0
    for i in riazii:
        num=i+num
    aveR=num/len(riazii)
    print(aveR)