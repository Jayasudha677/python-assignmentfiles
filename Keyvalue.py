file=open("abcd.txt","r")
dct=dict()
for temp in file:
  temp=temp.strip()
  temp=temp.lower()
  readline=temp.split()
  for i in readline:
        if i in dct:
              dct[i]=dct[i]+1
        else:
              dct[i]=1
file.close()
print("count of:")
for k in list(dct.keys()):
      print("{}".format(k,dct[k]))