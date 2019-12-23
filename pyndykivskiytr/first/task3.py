"""
Вивести суми парних і непарних чисел списку.
"""

numbers=[1, 2, 3, 4]
parni=neparni=0
for i in numbers:
    if(i%2==0):
        parni+=i
    elif(i%2==1):
        neparni+=i
        
print("sum of parni = "+str(parni))
print("sum of neparni = "+str(neparni))
