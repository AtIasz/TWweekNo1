import sys
path="todolist.txt"
List=[]
empty="[ ]"
mark="[x]"
def write():
    with open(path) as p:
            line= p.readline()
            cnt=1
            while line:
                line=p.readline()
                cnt+=1
            text=open(path,"a")
            text.write("{}. {} {}\n".format(cnt,empty,i))
def read():
    with open(path) as p:
            line= p.readline()
            cnt=1
            while line:
                print(line.strip())
                line=p.readline()
                cnt+=1
x=input("Please specify a command [list, add, mark, archive]: ")
if x=="add":
    i=input("Add an item: ")
    write()
    print("Item added.")
elif x=="list":
    print("You saved the following to-do items:")
    read()
elif x=="mark":
    print("You saved the following to-do items:")
    read()
    n=int(input("Which one you want to mark as completed: "))
    canWrite=False
    List=[]
    zawarudo=""
    with open(path) as p:#listába bementeni a külső fájl sorait
        line=p.readline()
        cnt=0
        
        while line:
            if cnt==n-1:
                zawarudo=line
            List.insert(cnt,line)
            line=p.readline()
            cnt+=1
    newList=[]
    riteNou=""
    taskName=""
    nospace=""
    for i in range(len(List)):
        canWrite=False
        taskName=""
        nospace=""
        riteNou=List[i]
        for j in range(len(riteNou)):
            
            if j>2: 
                if riteNou[j]==" " and riteNou[j-1]=="]":
                    canWrite=True
            if canWrite:
                taskName+=riteNou[j]
        for j in range(len(taskName)):
            if j>0:
                nospace+=taskName[j]
        newList.append(nospace)
    with open(path,"w") as p:
        for i in range(len(newList)):
            if i==n-1:
                p.write("{}. {} {}".format((i+1),mark,newList[i]))
            else:
                p.write("{}. {} {}".format((i+1),empty,newList[i]))
    for i in range(len(newList)):
        if i==(n-1):
            print(newList[i][:-1]+" is completed.")
elif x=="archive":
    with open(path) as p:
            line= p.readline()
            cnt=1
            while line:
                line=p.readline()
                cnt+=1
    List=[]
    whereList=[]
    with open(path) as p:#listába bementeni a külső fájl sorait
        line=p.readline()
        cnt=0
        while line:
            List.insert(cnt,line)
            line=p.readline()
            cnt+=1
    for i in range(len(List)):
        for j in range(len(List[i])):
            if j>2:
                if List[i][j]=="x" and List[i][j-1]=="[":
                    whereList.append(i)#jelölt elemek indexe

    newList=[]
    riteNou=""
    taskName=""
    nospace=""
    for i in range(len(List)):
        canWrite=False
        taskName=""
        nospace=""
        riteNou=List[i]
        for j in range(len(riteNou)):
            if riteNou[j]=="]":
                    canWrite=True
            if canWrite:
                taskName+=riteNou[j]
        for j in range(len(taskName)):
            if j>1:
                nospace+=taskName[j]
        newList.append(nospace)#ezzel bezárólag a newList listában benne vannak az elemek számozás és zárójelek nélkül.
    if len(whereList)>0:
        lineNum=0
        with open(path,"w") as p:
            for i in range(len(whereList)):
                for j in range(len(newList)):
                    if j!=whereList[i]:
                        p.write("{}. {} {}".format((lineNum+1),empty,newList[j]))
                        lineNum+=1
        print("All completed tasks got deleted.")
    