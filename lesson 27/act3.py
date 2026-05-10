class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        juli = parrot("juli",10)
        kalia = parrot("kalia",15)

        print("juli is a{}".format(juli.species))
        print("kalia is also a{}".format(kalia.species))

        print("{} is {} years old".format( juli.name, juli.age))
        print("{} is {} years old".format( kalia.name, kalia.age))