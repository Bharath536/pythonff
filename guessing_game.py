import random
secret_number=random.randint(1,9)
attempts=0
while true:
    guss=int(input("enter your guss"))
    attempts+=1
if(secret_number==guss):
    print("correct")
    print("attempts:",attempts)
    print("score:",score)
    break
else:
    print("wrong")