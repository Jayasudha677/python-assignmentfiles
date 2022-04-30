data=data2= ""
with open("abcd.txt") as fp:
     data=fp.read()
with open("updated.txt") as fp:
     data2=fp.read()
data += "\n"
data += data2
with open("def.txt","w") as fp:
     fp.write(data)