#-------------------------------------------------#
# Title: Working with Dictionaries#
# Dev:   RRoot#
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   DAuve, 03/07/2019, Added code to complete assignment 5
#   #https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/table

# Step 5
# Remove a new item from the list/table

# Step 6
# Save task to the Todo.txt file

# Step 7
# Exit program
#-------------------------------------------------

objFileName = "C:\\Users\\Derek\\PycharmProjects\\Assignments\\Todo.txt"
strData = []
dicRow = {}
myTable = []
strMenu = ("\nMenu of Options \n"
            "1)  Show current data.\n"
            "2)  Add a new item.\n"
            "3)  Remove an existing item.\n"
            "4)  Save Data to File.\n"
            "5)  Exit Program.\n")

# Step 1 - Load data from a file
f = open(objFileName, "r")
for line in f:
      strData = line.split(",")
      (key, val) = strData[0], strData[1]
      dicRow[key] = val.strip("\n")

myTable.append(dicRow)

#Display contents of list to user
print(myTable)

# Step 2 - Display a menu of choices to the user
print(strMenu)

#Menu choices loop
while(True):
      strChoice = str(input("Which option would you like to perform? [1 to 4] - "))

# Step 3 -Show the current items in the tableif (strChoice.strip() == '1'):
      if strChoice.strip() == "1":
            print(myTable)
            continue

# Step 4 - Add a new item to the list/Tableelif(strChoice.strip() == '2'):
      elif strChoice == "2":
            new_item = input("List new item. ").title()
            new_priority = input("List new item's priority. ")
            newdict = {new_item: new_priority}
            dicRow.update(newdict)
            # print(myTable)
            continue

# Step 5 - Remove a new item to the list/Tableelif(strChoice == '3'):
      elif  strChoice == "3":
            remove_item = input("Please type 1 item to remove from the list {}.".format(dicRow.keys()))
            del dicRow[remove_item.title()]
            #print(myTable)
            continue

# Step 6 - Save tasks to the ToDo.txt fileelif(strChoice == '4'):
      elif  strChoice == "4":
            with open(objFileName, "a") as d:
                  d.write(str(myTable))
            continue

      elif strChoice == "5": #start here need to get this back into format of original with new items
            #final_list = list(dicRow.items())
            #print(myTable)
            with open(objFileName, "a") as d:
                d.write("\r\n" + "Final List:\n")
                d.write(str(myTable))
            break #and Exit the program