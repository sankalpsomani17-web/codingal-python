class BMW:
    def fuel_type(self):
        print("BMW uses Diesel.")

    def max_speed(self):
        print("BMW max speed is 240 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol.")

    def max_speed(self):
        print("Ferrari max speed is 350 km/h.")

car_bmw = BMW()
car_ferrari = Ferrari()


for car in (car_bmw, car_ferrari):
    car.fuel_type()
    car.max_speed()
    print("-" * 20)
