class myClass:
    __privateVAr = 27
    def __privMeth(self):
        print("i am inside class my class")

    def hello(self):
        print("private variable value:",myClass.__privateVAr)
foo = myClass()
foo .hello()
foo.__privMeth