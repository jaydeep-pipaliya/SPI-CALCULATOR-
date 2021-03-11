d={1:["LA","Physic","EEEE","EWP","DT"],2:["CDE","Chemistry","CP","CT","EC"],
3:["DE","DSA","DM","DC","JAVA"],4:["C++","C","DM2","DC3","PYTHON"]}

d2={1:[3,2,1,3,2],2:[1,2,3,2,1],3:[4,3,2,1,3],4:[2,3,2,1,2]}


def getList(n):
    if(n==1 or n==8):
        return d[1]
    elif(n==2 or n==7):
        return d[2]
    elif(n==3 or n==6):
        return d[3]
    elif(n==4 or n==5):
        return d[4]


def getNumber(s):
    if(s=="SEM1" or s=="SEM8"):
        return 1
    elif(s=="SEM2" or s=="SEM7"):
        return 2
    elif(s=="SEM3" or s=="SEM6"):
        return 3
    elif(s=="SEM4" or s=="SEM5"):
        return 4

def SPI(sem,ans):
    f=d2[sem]
    d=[]
    for i in range(len(ans)):
        d.append(getMarks(ans[i],f[i]))
    sum1,sum2=0,0
    for i,j in zip(d,f):
        sum1=sum1+i
        sum2=sum2+j
    return round((sum1/sum2)*10 , 2)
def getMarks(a,l):
    if a=="AP":
        return l-0
    elif a=="A":
        return l-0.5
    elif a=="BP":
        return l-1
    elif a=="B":
        return l-1.5
    elif a=="CP":
        return l-2
    elif a=="FP":
        if(l<2):
            return 0
        return l-2.5
    else:
        return 0