#Riley Haluzak
#3/3/2018
#Blood Drive

#the main function
def main():
  endProgram = 'no'
  while endProgram == 'no':
    option = 0
    print
    print ('Enter new to enter in new data and store to file')
    print ('Enter read to display data from the file')
    option = input('Enter now: ')
    print ('\n')
    
    # declare variables
    pints = [0] * 7
    totalPints = 0
    averagePints = 0

    if option == 'new':
      # function calls
      pints = getPints(pints)
      totalPints = getTotal(pints, totalPints)
      averagePints = getAverage(totalPints, averagePints)
      writeToFile(averagePints, pints)
        
    elif option == 'read':
        readFromFile(averagePints, pints)

    else:
      while not (option == 'read' or option == 'new'):
        print ('Please select new or read.')
        option = input('Enter now: ')
           
    endProgram = input('Do you want to end program? (Enter no or yes): ')
    while not (endProgram == 'yes' or endProgram == 'no'):
      print ('Please enter a yes or no')
      endProgram = input('Do you want to end program? (Enter no or yes): ')

#the getPints function
def getPints(pints):
  counter = 0
  while counter < 7:
      pints[counter] = input('Enter pints collected: ')
      counter = counter + 1
  return pints  
  
#the getTotal function
def getTotal(pints, totalPints):
  counter = 0
  while counter < 7:
    totalPints = int(totalPints) + int(pints[counter])
    counter = counter + 1
  return totalPints

#the getAverage function
def getAverage(totalPints, averagePints):
  averagePints = float(totalPints) / 7
  return averagePints

#the writeToFile function
def writeToFile(averagePints, pints):
    fileName = input("Select a name for the file: ")
    fileName = fileName + ".txt"
    outFile = open(fileName, 'a')
    outFile.write('Pints Each Hour' + '\n')
    counter=0
    while counter < 7:
        outFile.write(pints[counter] + '\n')
        counter = counter + 1
    outFile.write("Average Pints" + '\n')
    outFile.write(str(averagePints))
    outFile.close()

#the readFromFile function
def readFromFile(averagePints, pints):
    findingFile = 1
    while (findingFile == 1):
        fileName = input("Select a file to read.")
        try:
            inFile = open(fileName, "a")
            findingFile = 0
        except:
            print ('File not found, please select a valid file.')
    str1 = inFile.read()
    print(str1)
    pints = inFile.read()
    print (pints)
    print #adds a blank line
    str2 = inFile.read()
    print (str2)
    averagePints = inFile.read()
    print (averagePints)
    print #adds a blank line
    inFile.close()

# calls main
main()
