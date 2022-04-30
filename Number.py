file=open("abcd.txt","r")
counter=0
content=file.read()
coList=content.split("\n")
for i in  coList:
     if i:
         counter += 1
         print("this is the number of lines in the file")
         print(counter)
    