class library:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
            self.is_borrowed=True
            print(f"you have sucessfully borrowed{self.title}")

    def return_book(self):
         self.is_borrowed = False
         print("you have sucessfully retuned the book{self.title} ")

book1 = library("The ghost , Xybn")
book2 = library("'a , h")
book3 = library("b,fd") 

book1.borrow()

    
        


