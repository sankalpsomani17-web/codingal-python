def hotel_cost(n):return 140*n

def plane_ride_cost(city):
    return{"charlotte":183,"tampa":220,"pittsburgh":222,"los angeles":475}.get(city,0)

def rental_car_cost(d):
    return 40*d - (50 if d>=7 else 20 if d>=3 else 0)

def trip_cost(city,d ,money):
    return hotel_cost(d)+plane_ride_cost(city)+rental_car_cost(d)+money

print(trip_cost("los angeles",7,500))
print(trip_cost("tampa",6,500))