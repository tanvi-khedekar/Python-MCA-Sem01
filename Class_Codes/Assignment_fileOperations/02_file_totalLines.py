# 2. Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line

#name = "random.txt"            #if using "name" as 1st parameter in open()
# or: name = input("Enter file name: ")         # ""

with open("random.txt", "r") as f:
    lines = f.readlines()
    print("Total number of lines in the file:", len(lines))
    if len(lines) >= 4:
        print("The 2nd line is:", lines[1].strip())
        print("The 4th line is:", lines[3].strip())
    else:
        print("The file does not have enough lines to display the 2nd and 4th lines.")