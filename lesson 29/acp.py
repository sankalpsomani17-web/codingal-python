class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        
        amount = super().fare()
        total_fare = amount + (0.1 * amount)
        return total_fare

School_Bus = Bus("School Volvo", 12, 50)
print(f"Total Bus fare is: {School_Bus.fare()}")
