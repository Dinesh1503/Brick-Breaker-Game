# Spell Checker Program

import os.path
from os import path

#Time inputs 
import time
from datetime import date
today = date.today()

# Global variables for Summary Statistics 
count_correct = 0
count_ignored = 0
count_incorrect = 0
count_added = 0
count_changed = 0
count_total = 0

# Copying contents of file 'Englishwords.txt' into a list 'wordslist'
file = open("Englishwords.txt")
wordslist = []
x = 0
for j in range(84093):
    wordslist.append(file.readline())
    wordslist[x] = wordslist[x].strip()
    x = x + 1
# Calculating number of words in file 'Englishwords.txt'
wlsize = len(wordslist)
file.close()

# Storing statistics in a dictionary 'satisticslist' and returning the dictionary
def statistics(d1,etime):
    statisticslist = {  "Number of correct words" : str(count_correct),
                        "Number of incorrect words added" : str(count_added),
                        "Number of words incorrect" : str(count_incorrect),
                        "Number of words Ignored" : str(count_ignored),
                        "Last Checked" : str(d1),
                        "Elapsed Time" : etime }
    return statisticslist

# Function for writing Summary Statistics in a file choosen by the user 
def store(words,d1,time):
    statlist = statistics(d1,time)
    filename = input("Enter Filename for the words to be stored: ")
    file = open(filename, "w")
    file.write(str(statlist))
    file.write(str("\n"))
    for i in range(len(words)):
        file.write(str(words[i] + "\n \n"))
    return

# Function for encountering incorrect words 
def options(word):
    d1 = today.strftime("%d/%m/%Y")
    print("\n Options Available: ")
    print("\n 1 - Ignore word", "\n 2 - Mark word", "\n 3 - Add to dictionary", "\n 4 - suggestion")
    ch = int(input("Enter your choice: "))
    # To ignore the word
    if (ch == 1):
        print(str(word) + " Ignored")
        global count_ignored
        count_ignored += 1
        global count_incorrect
        count_incorrect += 1
    # To Mark the word 
    elif (ch == 2):
        word = "?" + str(word) + "?"
        print(str(word) + " marked")
        count_incorrect += 1
    # To add the word to the dictionary
    elif (ch == 3):
        f = "Englishwords.txt"
        with open(f,'a') as f_obj:
            f_obj.write(str('\n') + str(word))
        print(str(word) + " added to dictionary")
        f_obj.close()
        global count_added
        count_added += 1
    # To show suggestions for incorrect word
    elif (ch == 4):
        f = open("Englishwords.txt")
        for k in wordslist:
            if (k[0] == word[0]):
                print("Suggested word: " + k)
        suggest = input("\n Enter one word from above that you would like as a suggestion: ")
        print("\n If you would not like any of the suggestions (press Enter)")
        if (suggest == ""):
            print("\n You have not accepted a suggested word")
            count_incorrect += 1
        else:
            print("\n Suggestion accepted")
            word = suggest
            print(word)
            global count_correct
            count_correct = count_correct + 1
    else:
        print("Invalid Option")
        options(word)
    return word


#Function to check the words in File entered by the user
def checkFile():
    start = time.time()
    d1 = today.strftime("%d/%m/%Y")
    filename = input("\n Enter File name(please make sure that the file exists in the same path as the Program): ")
    file_exist = str(path.exists(str(filename)))
    global count_total
    global count_correct
    count_total = 0
    count_correct = 0
    # Checking if given file exists
    if (file_exist == "True"):
        f = open(filename, "r")
        newfile_words = []
        # Copying words of given file in a list 'newfile_words' and checking if it is only alpha characters
        n = 0
        with open(filename) as f_obj:
        	file_words = f_obj.readlines()
        	for a in file_words:
        		file_words[n] = file_words[n].rstrip()
        		n = n + 1
        temp = [x.lower() for x in file_words]
        newfile_words = [x.strip("1234567890,.''") for x in temp]
        # Calculating number of words in given file and assigning to a variable 'wsize'
        wsize = len(newfile_words)
        count_total = wsize
        print("\n words in the given file:- " + str(newfile_words))
        # Checking the spelling of each word from the file 'Englishwords.txt'
        i,k,flag = 0,0,0
        for i in range(wsize):
            for k in range(wlsize):
                if (newfile_words[i] == wordslist[k]):
                    flag = 1
                    break
                else:
                    flag = 0
            if (flag == 1):
                print("\n The word " + newfile_words[i] + " is correct")
                count_correct = count_correct + 1
            else:
            	# calling function options to show the otions available if an incorrect word is encountered
                print("\n The word " + newfile_words[i] + " is incorrect")
                newfile_words[i] = options(newfile_words[i])
        f.close()
    else:
        print("\n File does not exits")
        print("\n do you want to renter filename or return to menu ?","\n 1 - Re-enter file name","\n 2 - return to Menu")
        ans = input("\n Enter Your Choice: ")
        if (ans == 1):
            checkFile()
        else:
            return Menu()
    end = time.time()
    etime = end - start
    statistics(d1,etime)
    store(newfile_words)
    print(statistics(d1,etime))
    print("\n File has been checked")
    ch = input("\n Do you want to return to the main menu (y/n): ")
    if (ch == "y"):
        Menu()
    else:
        exit()

    return

# Function to check the words of a Sentence entered by the user 
def checksentence():
    start = time.time()
    d1 = today.strftime("%d/%m/%Y")
    print("\n Check Sentence Function")
    sent = input("\n Enter Your Sentence: ")
    size = len(sent)
    file = open("Englishwords.txt")
    flag = 0
    i,k = 0,0
    global count_total
    global count_correct
    count_total = 0
    count_correct = 0
    new_sent = ""
    # Checking if the words contain any other characters than alphabets and removing if it has
    for i in sent:
    	if(i.isupper()) == True:
    		new_sent += i.lower()
    	elif(i.isspace()) == True:
    		new_sent += i
    	elif(i.isalpha()) == True:
    		new_sent += i
    print(new_sent)
    words = new_sent.split()
    print("Words in the Sentence: " + str(words))
    wsize = len(words)
    count_total = wsize
    # checking the spelling of words fron the file 'Englishwords.txt'
    for i in range(wsize):
        for k in range(wlsize):
            if(words[i] == wordslist[k]):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 1):
            print("\n The word " + words[i] + " is correct")
            count_correct = count_correct + 1
        else:
            print("\n The word " + words[i] + " is incorrect")
            words[i] = options(words[i])
    end = time.time()
    etime = end - start
    statistics(d1,etime)
    store(words,d1,etime)
    print(statistics(d1,etime))
    print("\n Sentence has been checked")
    ch = input("\n Do you want to return to the main menu (y/n): ")
    if (ch == "y"):
        Menu()
    else:
        exit()
    return


# Function to display the Main Menu 
def Menu():
    print("\n Welcome to Spell Checker Program")
    # Displaying the Menu with borders of '#'
    for i in range(2):
    	print(" ########################")
    	if (i == 0):
    		print(" #			#")
    		print(" # Menu			#")
    		print(" #			#")
    		print(" # 1 - Check Sentence   #")
    		print(" # 2 - Check File   	#")
    		print(" # 0 - Exit	  	#")
    		print(" #			#")
    	elif (i == 1):
    		break
    # To check the option entered by the user
    try:
    	x = int(input("\n Enter Your Choice: "))	
    	if x == 1:
        	print(x)
        	checksentence()
    	elif x == 2:
        	print(x)
        	checkFile()
    	elif x == 0:
        	print(x)
        	exit()
    except ValueError:
    	print("Invalid Option \n")
    	Menu()
    return


Menu()
