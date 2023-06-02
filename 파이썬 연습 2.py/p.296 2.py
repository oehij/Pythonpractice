import random
count=[0,0,0,0,0,0]

for i in range(1000):
    r=random.randint(0,5) 
    
    count[r]=count[r]+1

print("주사위가 1인 경우는 ",count[0]) 
print("주사위가 2인 경우는 ",count[1]) 
print("주사위가 3인 경우는 ",count[2]) 
print("주사위가 4인 경우는 ",count[3]) 
print("주사위가 5인 경우는 ",count[4]) 
print("주사위가 6인 경우는 ",count[5])