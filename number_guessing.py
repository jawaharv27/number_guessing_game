import random 
#random number is taken btw 1 and 100
random_num=random.randint(1,100)
#guessing number is taken from user
print("*** \"NUMBER GUESSING CHALLENGE\" ***")
print()
while True:
        guessing_num=int(input("ENTER ANY NUMBER TO GUESS:"))
        diff=abs(random_num-guessing_num)
        if(random_num>guessing_num and (diff>=20 or diff>10)):
                print("VERY LOW")
        elif(random_num>guessing_num ):
                print("LOW")
        elif(random_num<guessing_num and (diff>=20 or diff>10)):
                print("VERY HIGH")
        elif(random_num<guessing_num ):
                print("HIGH")
        elif(random_num==guessing_num):
                print()
                print("CONGRADULATIONS!! YOU GUESSED CORRECTLY :" , random_num)
                break




