# 1. Write a program to read a file and count how many vowels are present in its content.

name = input("Enter file name: ")
with open(name, "r") as f:
  data = f.read()
  vowels = "aeiouAEIOU"
  count = 0
  for char in vowels:
    count += data.count(char)
  print("Vowels present in the file: ", count)


# 2. Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line


# 3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.

# 4. Read a file, split its content into words, and store them in a list.
#   i. Print the total number of words
#   ii. Print all unique words