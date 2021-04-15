import math
import random

initial_list=[]
for i in range (0,101):
    initial_list.append(i)

guesses=0

        
while True:
    guesses+=1
    n=random.choice(initial_list)
    q=input("Is your number {}? If not, is it greater(g) or lower(l)".format(n))
    if q=="y":
        print ("I've won in {} guesses".format(guesses))
        break
    elif q=="g":
        for z in reversed(initial_list):
            if z<n:
                initial_list.remove(z)
                continue
    elif q=="l":
        for l in reversed(initial_list):
            if l>n:
                initial_list.remove(l)
    elif q=="q":
        break
    
    
