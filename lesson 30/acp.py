class point:
    def __init__(self,word):
        self.word=word
    def __str__(self):
        return self.word[::-1]

p1 = point("sankalp")
print(p1)