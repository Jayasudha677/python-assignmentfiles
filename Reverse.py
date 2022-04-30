f1=open("abcd.txt","w")
with open("def.txt","r") as myfile:
     data=myfile.read()
data_1=data[ : : -1]
f1.write(data_1)
f1.close()

