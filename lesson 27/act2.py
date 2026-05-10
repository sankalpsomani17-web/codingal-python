class vehicle:

    def __init__(self,model,max_speed, mileage):
        self.model = model
        self.max_speed = max_speed
        self.mileage = mileage

BMW_M5 =  vehicle("BMW M5",275,14)

print("BMW_M5 max speed:",BMW_M5.max_speed)
print("bmw m5 mileage:",BMW_M5.mileage)
