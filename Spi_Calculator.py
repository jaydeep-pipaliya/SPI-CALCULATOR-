

G_Object={
    'AP':10,'A':9,'BP':8,'B':7,'CP':6,'C':7
}

def SPI(sublist,GradeList):
    f=[]
    d=[]
    for i in sublist:
        f.append(int(i[-1]))
    sum1,sum2=0,0
    for i in range(len(f)):
        sum1=sum1+f[i]*G_Object[GradeList[i]];
        sum2=sum2+f[i]
    return round((sum1/sum2) , 2)