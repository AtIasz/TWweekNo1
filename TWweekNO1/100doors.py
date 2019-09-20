openedDoors=[]
m=False
by=1
for i in range(101):
    openedDoors.append(m)
while by<=100:
    i=1
    while i<=100:
        if i%by==0:
            if openedDoors[i]!=True:
                openedDoors[i]=True
            else:
                openedDoors[i]=False
        i+=1
    by+=1
for i in range(len(openedDoors)):
    if openedDoors[i]==True:
        print(str(i)+", ",end="")
print()
