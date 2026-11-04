


from micro import*
import random
week_weather=[]
for i in range(7):
    weather=w()
    temperature=T(weather)
    suggestion=suggest(temperature)
    
    week_weather.append(weather)
    week_weather.append(temperature)
    week_weather.append(suggestion)

    print(weather)
    print(temperature)
    print(weather)
   
print(week_weather)                   
