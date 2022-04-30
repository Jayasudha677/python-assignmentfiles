def counter(fname):
     num_words=0
     num_lines=0
     num_charc=0
     num_spaces=0
     with open("abcd.txt",'r') as f:
         for line in f:
          num_lines +=1
          word = 'Y'
         for letter in line:
               if(letter !='' and word =='Y'):
                    num_words +=1
                    words ='N'
               elif (letter==' '):
                    num_spaces +=1
                    words='Y'
               for i in letter:
                    if(i!=" " and i !="\n"):
                          num_charc +=1
         print("number of words in text files:",num_words)
         print("number of characters in text file:",num_charc)
         print("number of spaces in text file:",num_spaces)
         print("number of lines in text file:",num_lines)
if __name__ == '__main__':
     fname='abcd.txt'
     try:
          counter(fname)
     except:
          print("file not found")

               