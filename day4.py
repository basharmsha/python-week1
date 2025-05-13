# try:
#     with open("missingfile4.txt", "x") as f:
#         data = f.write("")
#         print("File created")
# except FileNotFoundError:
#     print("NOT FOUND")
# except Exception as e:
#     print("Some else")

# with open("missingfile4.txt", "r") as file:
#     data4 = file.read()
#     print(data4)
# with open("missingfile4.txt", "w") as file:
#     file.write("/nThis is the 2nd line")
# with open("missingfile4.txt", "r") as file:
#     data4 = file.read()
#     print(data4)
# Exercise 1: Journal Logger (Write)
# Prompt:
# Create a script that:
#
# Asks the user to enter a journal entry
#
# Appends the entry to a file named journal.txt

#entry = input("Enter a journal entry: ")

# with open("myjournal", "w") as file:
#     file.write(entry)
# with open("myjournal", "a") as file:
#     file.write("\n" + entry)
# print("saved")
# with open("myjournal", "r") as file:
#     journal = file.read()
#     print(journal)
# #
# Exercise 2: File Reader
# Prompt:
# Write a script that:
#
# Opens journal.txt
#
# Prints all contents to the console
#
# Catches FileNotFoundError if the file doesn't exist
# try:
#     with open("journal.txt", "r") as f:
#         content = f.read()
#         print("Journal Contents:\n", content)
# except FileNotFoundError:
#     print("File not found")
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num = num1 / num2
    print(num)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except Exception as e:
    print("Unexpected error:", e)













