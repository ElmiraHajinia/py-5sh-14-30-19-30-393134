tarikhh=[]
def tarikh(num):
    tarikhh.append(num)

def aveeT():
    num=0
    for i in tarikhh:
        num=i+num
    aveT=num/len(tarikhh)  
    print(aveT)       