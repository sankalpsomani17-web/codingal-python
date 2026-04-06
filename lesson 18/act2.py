try:
    num1,num2=eval(input("enter two number,separated by comma:"))
    result=num1/num2
    print("RESULT IS",result)

except ZeroDivisionError:
    print("divison by zero is error !!")

except SyntaxError:
    print("comma is missisng. enter numbers separated by comma like this 1,2")\
    
except:
    print("wrong input ")

else:print("no exceptions")

finally:
    print("this will excute no matter what")