file=open('abcd.txt','r')
while 1:
     char=file.read(1)
     if not char:
          break
     print(char)
file.close()

with open("abcd.txt") as f:
     while True:
          c=f.read(5)
          if not c:
               break
          print(c)
