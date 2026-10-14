# 4. Read a file, split its content into words, and store them in a list.
#   i. Print the total number of words
#   ii. Print all unique words

file_name = input("Enter the file name: ")
with open(file_name, "r") as f:
    content = f.read()
    words = content.split()
    print("Total number of words in the file:", len(words))
    unique_words = set(words)
    print("Unique words in the file:", unique_words)