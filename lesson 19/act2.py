import random 

while True:
    u = input("rock/paper/scissors:")
    c = random.choice(["rock","paper","scissors"])
    print(u,"vs",c)

    print("tie!" if u==c else
          "win!" if (u,c) in [("rock","scissors"),("paper","rock"),
        ("scissors","paper")]
        else "lose!")
    
    if input ("again?y/n: ")!="y":break