#friday the 5
# 20 MIN MA 4 LINE CODE WHOAAAAAAAAAAAAAAAAAAAH BHOJ DAIIIIIIIIIIIII 32 ma 9 
import random


listo=["A","E","I","O","U"]
PASS=[]


for _ in range(4):
    PASS.append(listo.pop())

print(PASS)

run=True
while run:
    x=input(f"enter a four character guess from{listo}")
    
    if len(x)!=4:
        print("a FOUR characters  ..* _ *..  plzzzzzzzzz")
    else :
        for i in x:
            if i.isdigit():
                print("characters......>.<")
                break
        
        else:
            run=False

k=0
count=0
for j in x:
    if PASS[k]==j:
        count+=1
    k+=1
    
print(f"the digits that were right were{count}")
