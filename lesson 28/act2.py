class Employee:
    def __init__(self):
        print('Employee created')
    def __init__(self):
        print("destructor called")
        
def create_obj():
    print('making object...')
    obj = Employee()
    print('function end...')
    return obj
print('calling create_obj() function...')
obj = create_obj()
print('program end...')