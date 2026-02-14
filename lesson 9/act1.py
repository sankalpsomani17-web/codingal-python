medical_cause = input("did you have a medical cause ? (y/n)").strip().upper()

if medical_cause == 'Y' :
    print("you are allowed")
else:
    atten=int(input("enter your attendance"))
    if atten >=75 :
        print("you are allowed")
    else:
        print("you are not allowed")
