#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  file_name = input("Enter the name of the file: ")
  with  open(file_name,'r') as textFile:
  #textFile = open("gettysberg.txt", 'r')
      lineCount = 0
      wordCount = 0
      letterCount = 0
      charCount = 0
      for line in textFile:
        lineCount = lineCount + 1
        charCount += len(line)
        words = line.split()
        for w in words:
          wordCount = wordCount + 1

  print("Lines: " , lineCount)
  print("words:", wordCount)
  print("Characters :", charCount)
  
if __name__ == '__main__':
  main()
