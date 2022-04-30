f=open("abcd.txt",'w')
f.write("hi hello python world")

f.close()

f1=open("def.txt","w")
f1.write("python program")
f1.close()
with open("abcd.txt", 'r') as file:
      for line in file:
           for word in line.split():
                print(word)
