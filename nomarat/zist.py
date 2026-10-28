zistt=[]
def zist(num):
    zistt.append(num)


def aveeZ():
    num=0
    for i in zistt:
        num=i+num
    aveZ=num/len(zistt) 
    print(aveZ)    