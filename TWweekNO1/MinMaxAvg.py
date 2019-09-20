RandomList=[-5,23,0,-9,12,99,105,-43]
numMin=RandomList[0]
numMax=RandomList[0]
numAVG=0
for i in range(len(RandomList)):
    if numMin>RandomList[i]
    :
        numMin=RandomList[i]
    if numMax<RandomList[i]:
        numMax=RandomList[i]
    numAVG+=RandomList[i]
numAVG=numAVG/len(RandomList)
print("Maximum: "+str(numMax))
print("Minimum: "+str(numMin))
print("Average: "+str(numAVG))