# ERROR HANDLING IN PYTHON
#ZeroDivisionError:
#Occurs when you try to divide a number by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

#ValueError:
#Occurs when a built-in operation or function receives an argument with the right type but an inappropriate value
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#IndexError:
#Occurs when trying to access an element from a list using an invalid index
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Error: Index out of range")

#KeyError:
#Occurs when trying to access a dictionary key that doesn't exist
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError:
    print("Error: Key not found")

#FileNotFoundError:
#Occurs when trying to open or read a file that does not exist.
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

#IOError (Python 2) / OSError (Python 3):
#Occurs when there is an I/O-related issue while reading or writing to a file.    
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
except IOError as e:  # Python 2
    print("I/O Error:", e)
except OSError as e:  # Python 3
    print("OS Error:", e)


#FILE HANDLING IN PYTHON
'''
Opening and Closing Files:
To work with a file in Python, you need to open it first.
The built-in open() function is used to open a file and returns a file object. 
After performing file operations, it is essential to close the file using the close() method of the file object.

'''
# Opening a file in read mode
file = open("example.txt", "r")
# File operations here...
file.close()  # Close the file when done

#FILE MODES:
'''
The open() function takes a second argument specifying the file mode. The most commonly used modes are:
'r': Read mode (default). It allows reading from the file.
'w': Write mode. It truncates the file to zero length or creates a new file for writing.
'a': Append mode. It appends data to the end of the file.
'b': Binary mode. Used for non-text files like images or executables.
't': Text mode (default). Used for text files.
'''
# Open a file in write mode
file = open("example.txt", "w")
# File operations here...
file.close()

'''
Reading from Files:
You can read the contents of a file using various methods, such as read(), readline(), and readlines().
'''
# Reading the entire file
file = open("example.txt", "r")
content = file.read()
file.close()

# Reading one line at a time
file = open("example.txt", "r")
line = file.readline()
file.close()

# Reading all lines into a list
file = open("example.txt", "r")
lines = file.readlines()
file.close()

'''
Writing to Files:
You can write data to a file using the write() method.
'''
# Writing to a file
file = open("example.txt", "w")
file.write("Hello, this is a new line.")
file.close()

'''
Appending to Files:
To append data to an existing file, use the 'a' mode or the write() method
'''
# Appending to a file using 'a' mode
file = open("example.txt", "a")
file.write("This line will be appended.")
file.close()

'''
Context Manager (with statement):
Python provides a context manager to work with files,
 which ensures that files are properly closed after usage without explicitly calling file.close()
'''
with open("example.txt", "r") as file:
    content = file.read()
# File is automatically closed when leaving the 'with' block

'''
File Pointer:
The file object maintains a file pointer, which indicates the current position in the file for reading or writing.
 You can use the seek() method to move the file pointer to a specific location.
'''
file = open("example.txt", "r")
file.seek(10)  # Move the file pointer to the 10th byte
data = file.read()
file.close()

'''
Handling Exceptions while Working with Files:
When dealing with file operations, it is essential to handle exceptions properly, such as FileNotFoundError or IOError.
'''
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")


#SOME JOINED EXAMPLES ON ERRORS AND FILE HANDLING

def file_handling_example():
    # Opening a file in read mode
    with open("example.txt", "r") as file:
        # Reading the entire content of the file
        content = file.read()
        print("File Content:")
        print(content)

    # Writing to a file (overwrites existing content)
    with open("example.txt", "w") as file:
        file.write("Hello, World!")

    # Appending to a file (adds new content without overwriting)
    with open("example.txt", "a") as file:
        file.write("\nThis is a new line.")

    # Reading lines from the file
    with open("example.txt", "r") as file:
        print("\nReading Lines:")
        line1 = file.readline()
        print("Line 1:", line1.strip())  # Using strip to remove the newline character
        lines = file.readlines()
        print("Remaining Lines:")
        for line in lines:
            print(line.strip())  # Using strip to remove the newline character


if __name__ == "__main__":
    print("File Handling Concepts in Python")
    print("--------------------------------")
    file_handling_example()

try:
    # File handling - Reading from a file
    with open('example.txt', 'r') as file:
        data = file.read()
        print("Content of 'example.txt':")
        print(data)

    # File handling - Writing to a file
    with open('output.txt', 'w') as file:
        file.write("Hello, this is a sample text.")
    print("'output.txt' written successfully.")

    # Exception handling - Division by zero
    result = 10 / 0  # This will raise a ZeroDivisionError
except FileNotFoundError:
    print("File not found.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("End of the program.")

