file1=open("abcd.txt","r")
file2=open("updated.txt","w")
lines=file1.readlines()
type(lines)
for i in range(0,len(lines)):
      if(i % 2 !=0):
            file2.write(lines[i])
file1.close()
file2.close()
file1=open("abcd.txt","r")
file2=open("updated.txt","r")
str1=file1.read()
str2=file2.read()
print("system")
print(str1)
print()
print("updated content")
print(str2)
file1.close()
file2.close()