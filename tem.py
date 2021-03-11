# ===================================
# This file is used to crate Api of niram per sem semester wise data
# ===================================

f1=open("./static/Nirma_Data.txt","r")
data=f1.read()
list1=data.split("End")
persem_list=list(map(lambda x: x.split("\n"),list1))
# print(persem_list)
Data_inDic={}
tem=1
last=-1
for i in persem_list:
    i.remove("")
    if "" in i:
        i.remove("")
    if(i[0][0:8]!="Semester"):
        # print(i)
        if tem !=1:
            Data_inDic[last]=tem
        last=i[0]
        i.remove(i[0])
        tem={}
    tem[i[0]]=i[1:]
Data_inDic[last]=tem
for i in Data_inDic:
    # print(i):
    for sem in Data_inDic[i]:
        # print(f'{sem} {i}')
        list=Data_inDic[i][sem]
        for i1 in range(len(list)):
            list[i1]=list[i1].split("-")
import json
f1.close()
f1=open("Niram_data.py","w")
f1.write("DATA=")
f1.write(json.dumps(Data_inDic))
f1.close()