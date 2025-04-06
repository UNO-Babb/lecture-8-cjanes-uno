def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split(" ")
    print(info[0], info[1], "had a rating of", info[10])
  
  myFile.close()

if __name__ == '__main__':
  main()
