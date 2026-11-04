



import random

def w():
    weatherrr=["sunny","rainy","snowy"]
    weather=random.choice(weatherrr)
    
    return weather

def T(weather):
    if weather=="snowy":
        temperature=random.randint(-10,2)
    else:
        temperature=random.randint(3,42) 

    return temperature

def suggest(temperature):
    if -10<=temperature<3:
        suggestionnn=("wear very warm clothes")

    if 3<=temperature<10:
        suggestionnn=("wear warm clothes")
            
    if 10<=temperature<20:
        suggestionnn=("wear a light jacket")    
          
    if 20<=temperature<27:
        suggestionnn=("wear light clothes")    
            
            
    if 27<=temperature<=42:
        suggestionnn=("wear light and breathable clothes")

    return suggestionnn   