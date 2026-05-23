from abc import ABC, abstractmethod

class parent(ABC):
    @abstractmethod
    def money_management(self):
        pass

class child(parent):
    def task(self):
        print('we are inside test_class task')

test_obj = child()
test_obj.task()