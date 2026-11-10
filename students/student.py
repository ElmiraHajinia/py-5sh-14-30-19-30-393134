


students={}

def IDDD(ID,info):
    students[ID]=info
    return students

def deleteee(deletee):
    students.pop(deletee)
    return students

def edittt(editt,num):
    students[editt].update({"num":num})
    return students


   
