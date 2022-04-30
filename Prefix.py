file1=open("abcd.txt","r")
file2=open("updated.txt","w")

for line in file1.readlines():
     if not (line.startswith("hi")):
          print(line)
          file2.write(line)
file2.close()
file1.close()