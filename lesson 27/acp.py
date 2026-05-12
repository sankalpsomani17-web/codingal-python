class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, breed, name):
        # Instance variables
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 20)

# Create two instances of different breeds
dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("German Shepherd", "Max")

# Display details
print("Dog 1 Details:")
dog1.display_details()

print("Dog 2 Details:")
dog2.display_details()
