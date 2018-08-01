import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList
 #print(ourList) 
    belowFive=[i for i in ourList if i<5] #sort all integers less than Five for ourList Array

print(belowFive)
