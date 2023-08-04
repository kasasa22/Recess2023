#Matching and searching
#regex re.match re.search() re.findall()

#Example 1
#demostrating regular explations
#merge first word, merge group word, merge all numbers

import re
text = "Hello, My name is kasasa Trevor. Iam a programmer with 1 year experience"

#merge first word

match = re.search (r"^\b\w+\b", text)

if match:
    print("Matches:", match.group())

matches = re.findall(r"\d+", text)
print("Matches:", matches)

#Example 2
#validate email format or email adddres

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False
email = 'kasasatrevor25@gmail.com'
email1 = "kasatrecd9274789"

print(validate_email(email))
print(validate_email(email1))

#generators and iterators
#'yield' generator
#iterator __iter__ __next__ iterator

def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * next(factorial(n-1))

# Print the factorial of a number from 1 to 10
for i in range(1, 11):
    print(i, ":", next(factorial(i)))


#Example 2
#Generate function that yields the square of numbers from 1 to 1

#decorators
def my_decoratr(func):
    def inner():
        print ("this is my decorator")
        fuc()
    return inner
@my_decorator
def outer_decoratror():
    print("this is outer function")

outer_decolator()
