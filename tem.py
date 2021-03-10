import json

f1=open("hh.txt","w")
data={ "1":True}
x = '{ "name":"John", "age":30, "city":"New York"}'
f1.write(json.dump(data))
# print(str(data))
# True