class vehicle:
    def __init__(self,name, maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("eicher starline",100 , 5)
print("vehicle name:",school_bus.name,"speed:",school_bus.maxspeed,)