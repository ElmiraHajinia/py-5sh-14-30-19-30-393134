



products={}

def add(product_idd,namee,pricee):
    global products
    products[product_idd]={"name":namee,"price":pricee}
    print("added")
    return products

def searchhh(product_idd):
    global products    
    search_result=products.get(product_idd)
    print(search_result)
    return products

def update(product_idd,namee,pricee):
    global products 
    products[product_idd].update({"name":namee,"price":pricee})
    print("edited")
    return products

def deleteee(product_idd):
    global products 
    products.pop(product_idd)   
    print("deleted")
    return products

