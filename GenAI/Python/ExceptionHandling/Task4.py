filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        lines = file.readlines()

        print("First 3 lines of the file:")
        for line in lines[:3]:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to read the file.")
finally:
    print("File operation attempted.")