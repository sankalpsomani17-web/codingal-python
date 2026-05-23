class India():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("hindi is most widely spoken language of india")
    
class USA():
    def capital(self):
        print("Washington is the capital of USA")
    def language(self):
        print("English is most widely spoken language of USA")


obj_ind = India()
obj_usa = USA()

for country in (obj_ind,obj_usa):
    country.capital()
    country.language()