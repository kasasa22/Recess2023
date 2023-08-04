#NAME: KASASA LIVINGSTONE TREVOR
#REG_NO.: 22/U/22469
#STUDENT NO. : 2200722469



import time
import threading
import multiprocessing
import sqlite3


# Notes on Context Managers
'''
Context managers are objects that define the methods __enter__() and __exit__() which enable us to manage 
resources such as files or database connections. It is used alongside the 'with' statement which automatically
calls the __enter__() method at the beginning of the block and the __exit__() method at the end of the block.

The __exit__() method handles any cleanup  or resource release tasks.
'''

# This is an example of a context manager that handles file operations.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
 # Perform other file operations as needed







# Context manager to handle database operations.
class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.close()

# Using the database manager.
# the program will create a database file called database_example.db on your computer
class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()

with DatabaseManager("example.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES ('John')")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)










# Notes on mulithreading and multiprocessing:
'''
Multithreading and multiprocessing are both techniques used to achieve concurrent execution of tasks.
They allow programs to execute multiple taks simultaneously.
Multithreading invloves creating multiple threads within a single thread while multiprocessing invloves running
multiple processes simultaneously.

'''

# Function that will be called by each process and thread.
def task(seconds):
    print(f"Running task for {seconds} seconds...")
    # time.sleep(seconds) is used to suspend the execution of the thread or process for the given number of seconds.
    time.sleep(seconds)
    print(f"Task completed after {seconds} seconds")

# Implementation for multithreading.
def run_multithreading():
    thread1 = threading.Thread(target=task, args=(2,))
    thread2 = threading.Thread(target=task, args=(4,))
    thread3 = threading.Thread(target=task, args=(6,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

# this is an implementation of multiprocessing.
# The Join() method is used to block the excecution of the current program until the process completes execution
def run_multiprocessing():
    process1 = multiprocessing.Process(target=task, args=(2,))
    process2 = multiprocessing.Process(target=task, args=(4,))
    process3 = multiprocessing.Process(target=task, args=(6,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

# Each process and thread is going to run the task() function for a specific amount of time specified using 'args' argument of the process function
print("Multithreading example:")
run_multithreading()

print("\nMultiprocessing example:")
if __name__ == '__main__': 
    multiprocessing.freeze_support()
    run_multiprocessing()

