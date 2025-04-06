def main():
  myFile = open("MLB_Pitching.csv", 'r')

  for line in myFile:
    info = line.split(",")
    name = info[0]
    
    print(name)
  
  myFile.close()

if __name__ == '__main__':
  main()