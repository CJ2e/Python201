filename = input("Enter the filename: ")
content = input("Enter the content: ")

with open(filename, 'w') as file:
    file.write(content)
    file.write('\n')  # Add a new line at the end of the filename

open_file = input("Would you like to open the file? (y/n): ")
if open_file in ['y', 'n']:
    if open_file == 'y':
        with open(filename, 'r') as file:
            print(file.read())
    else:
        print("Okay, goodbye!")
