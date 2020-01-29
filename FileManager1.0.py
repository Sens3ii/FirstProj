import os
import time
import os.path


def MainMenu():
    print("0. Input '0' - back/exit")
    print("1. Input '1' - work with directories")
    print("2. Input '2' - work with files")
    print("3. Input '3' - change current directory")


def FileChoices():
    print("0. Input '0' - back/exit")
    print("1. Input '1' - delete file")
    print("2. Input '2' - rename file")
    print("3. Input '3' - add content to file")
    print("4. Input '4' - rewrite file")
    print("5. Input '5' - return to the parent directory")


def DirChoices():
    print("0. Input '0' - back/exit")
    print("1. Input '1' - rename your directory")
    print("2. Input '2' - check number of files in directory")
    print("3. Input '3' - check number of directories")
    print("4. Input '4' - check content of directory")
    print("5. Input '5' - add new file into directory")
    print("6. Input '6' - add new directory into current directory")


def DeleteFile(fileName):  # Function to delete the file
    os.remove(curDir + "/"+fileName)
    print("File was deleted")


def RenameFile(fileName, newFileName):  # Function to rename the file
    os.rename(fileName, newFileName)
    print("File was renamed")


def AddContFile(fileName):  # Function to add something into your file
    curFile = open(fileName, 'a')
    newCont = input("Input your text: ")
    curFile.write(newCont)
    print("Content was added")
    curFile.close()


def RewriteContFile(fileName):  # function to rewrite whole file
    curFile = open(fileName, 'w')
    newCont = input("Input your text: ")
    curFile.write(newCont)
    print("File was rewrited")
    curFile.close()


def RenameDir(dirName, newDirName):  # Function to rename the directory
    os.rename(dirName, newDirName)
    print("Directory was renamed")


def CountOfFiles():                # function to print number of files
    entries = os.listdir(curDir)
    num = int(0)
    for entry in entries:
        if os.path.isfile(entry):
            num += 1
    print("There are", num, "files")


def CountOfDir():                # function to print number of files
    entries = os.listdir(curDir)
    num = int(0)
    for entry in entries:
        if os.path.isdir(entry):
            num += 1
    print("There are", num, "directories")


def ContentOfDir():
    entries = os.listdir(curDir)
    for entry in entries:
        print(entry)


def AddFile(fileName):
    curFile = open(fileName, 'w')
    print("File was added into this directory")
    curFile.close()


def AddDir(dirName):
    os.mkdir(dirName)


print("FileManager 1.0")
while(True):
    curDir = os.getcwd()
    MainMenu()
    print("Current directory is:"+curDir)
    firstChoice = int(input("Input: "))
    if firstChoice == 1:
        DirChoices()
        secondChoice = int(input("Input: "))
        if secondChoice == 1:
            dirName = input("Input directory's name: ")
            newDirName = input("Input new directory's name: ")
            RenameDir(dirName, newDirName)
        elif secondChoice == 2:
            CountOfFiles()
        elif secondChoice == 3:
            CountOfDir()
        elif secondChoice == 4:
            ContentOfDir()
        elif secondChoice == 5:
            fileName = input("Input name of file: ")
            AddFile(fileName)
        elif secondChoice == 6:
            dirName = input("Input name of directory: ")
            AddDir(dirName)

    elif firstChoice == 2:
        FileChoices()
        secondChoice = int(input("Input: "))
        if secondChoice == 1:
            fileName = input("Input file's name: ")
            DeleteFile(fileName)
        elif secondChoice == 2:
            fileName = input("Input file's name: ")
            newFileName = input("Input new file's name: ")
            RenameFile(fileName, newFileName)
        elif secondChoice == 3:
            fileName = input("Input file's name: ")
            AddContFile(fileName)
        elif secondChoice == 4:
            fileName = input("Input file's name: ")
            RewriteContFile(fileName)
        elif secondChoice == 5:
            parentDir = os.path.dirname(os.getcwd())
            os.chdir(parentDir)
    elif firstChoice == 3:
        newPath = input("Input path: ")
        os.chdir(newPath)
    else:
        print("Thank you")
        time.sleep(1)
        break
