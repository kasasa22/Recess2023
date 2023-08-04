# Name: Kasasa Livingstone Trevor
#stdNo: 2200722469
#RegNo: 22/U/22469

#INDIVIDUAL ASSIGNMENT
#EXERCISE 1
                        #QUESTION 1

names = ["John", "Emily", "Michael", "Jessica", "David"]
second_item = names[1]
print(second_item)

#output Emily

                   #QUESTION 2
names = ["John", "Emily", "Michael", "Jessica", "David"]
new_value = "Sarah"

names[0] = new_value
print(names)

#output ['Sarah', 'Emily', 'Michael', 'Jessica', 'David']

                #QUESTION 3
names = ["John", "Emily", "Michael", "Jessica", "David"]
new_item = "Sophia"

names.append(new_item)
print(names)

#output ['John', 'Emily', 'Michael', 'Jessica', 'David', 'Sophia']

            #QUESTION 4
names = ["John", "Emily", "Michael", "Jessica", "David"]
new_item = "Bathel"

names.insert(2, new_item)
print(names)

#output ['John', 'Emily', 'Bathel', 'Michael', 'Jessica', 'David']
 
            #QUESTION 5
names = ["John", "Emily", "Michael", "Jessica", "David"]

del names[3]
print(names)

#output ['John', 'Emily', 'Michael', 'David']

            #QUESTION 6
names = ["John", "Emily", "Michael", "Jessica", "David"]

last_item = names[-1]
print(last_item)

#output David

            #QUESTION 7
items = ["Apple", "Banana", "Orange", "Grape", "Mango", "Pineapple", "Cherry"]

item = items[2:5]
print(item)

#output ['Orange', 'Grape', 'Mango']


            #   QUESTION 8
countries = ["USA", "Canada", "UK", "Germany", "France", "Japan"]
countries_copy = countries.copy()

print(countries)
print(countries_copy)

#output ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan']
#output ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan']

            #QUESTION 9
countries = ["USA", "Canada", "UK", "Germany", "France", "Japan"]

for country in countries:
    print(country)

#output
'''
USA
Canada
UK
Germany
France
Japan

'''
         #QUESTION 10
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey", "Zebra"]

# Sort in descending order
descending_order = sorted(animals, reverse=True)

# Sort in ascending order
ascending_order = sorted(animals)

print("Descending order:", descending_order)
print("Ascending order:", ascending_order)

'''
Descending order: ['Zebra', 'Tiger', 'Monkey', 'Lion', 'Giraffe', 'Elephant']
Ascending order: ['Elephant', 'Giraffe', 'Lion', 'Monkey', 'Tiger', 'Zebra']

'''
            #QUESTION 11
animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey", "Zebra"]

animals_with_a = [animal for animal in animals if "a" in animal.lower()]

for animal in animals_with_a:
    if "a" in animal.lower():
        print(animal)
#output 
'''
Elephant
Giraffe
Zebra
'''
            #QUESTION 12
# Create two lists of first names and last names
first_names = ["John", "Emily", "Michael"]
last_names = ["Doe", "Smith", "Johnson"]

# Join the two lists
full_names = first_names + last_names

# Print the joined list
print("Joined list of names:", full_names)
# Output: Joined list of names: ['John', 'Emily', 'Michael', 'Doe', 'Smith', 'Johnson']


                # EXERCISE 2
# 1. Output favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print("Favorite phone brand:", favorite_brand)  # Output: Favorite phone brand: iphone

# 2. Print the 2nd last item using negative indexing
second_last_item = x[-2]
print("Second last item:", second_last_item)  # Output: Second last item: tecno

# 3. Update "iphone" to "itel"
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print("Updated tuple:", x)  # Output: Updated tuple: ('samsung', 'itel', 'tecno', 'redmi')

# 4. Add "Huawei" to the tuple
x = x + ("Huawei",)
print("Updated tuple with Huawei:", x)  # Output: Updated tuple with Huawei: ('samsung', 'itel', 'tecno', 'redmi', 'Huawei')

# 5. Loop through the tuple
print("Looping through the tuple:")
for phone in x:
    print(phone)
# Output:
# Looping through the tuple:
# samsung
# itel
# tecno
# redmi
# Huawei

# 6. Remove the first item in the tuple
x = x[1:]
print("Tuple after removing the first item:", x)  # Output: Tuple after removing the first item: ('itel', 'tecno', 'redmi', 'Huawei')

# 7. Create a tuple of cities in Uganda using the tuple() constructor
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print("Uganda cities tuple:", uganda_cities)  # Output: Uganda cities tuple: ('Kampala', 'Entebbe', 'Jinja', 'Mbarara')

# 8. Unpack the tuple
city1, city2, city3, city4 = uganda_cities
print("Unpacked cities:", city1, city2, city3, city4)  # Output: Unpacked cities: Kampala Entebbe Jinja Mbarara

# 9. Print the 2nd, 3rd, and 4th cities using a range of indexes
cities_subset = uganda_cities[1:4]
print("Subset of cities:", cities_subset)  # Output: Subset of cities: ('Entebbe', 'Jinja', 'Mbarara')

# 10. Join two tuples of first and second names
first_names = ("John", "Emily", "Michael")
second_names = ("Doe", "Smith", "Johnson")
full_names = first_names + second_names
print("Joined tuples of names:", full_names)  # Output: Joined tuples of names: ('John', 'Emily', 'Michael', 'Doe', 'Smith', 'Johnson')

# 11. Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied colors tuple:", multiplied_colors) 
 # Output: Multiplied colors tuple: ('red', 'blue', 'green', 'red', 'blue', 'green', 'red', 'blue', 'green')

# 12. Return the number of times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Count of 8:", count_8)  # Output: Count of 8: 2

            #EXERCISE 3
# 1. Create a set of favorite beverages using the set() constructor
beverages = set(["Coffee", "Tea", "Juice"])
print("Set of favorite beverages:", beverages)  # Output: Set of favorite beverages: {'Juice', 'Coffee', 'Tea'}

# 2. Add 2 more items to the beverages set using the correct method
beverages.add("Water")
beverages.update(["Soda", "Smoothie"])
print("Updated set of beverages:", beverages)  # Output: Updated set of beverages: {'Coffee', 'Smoothie', 'Water', 'Tea', 'Juice', 'Soda'}

# 3. Check if "microwave" is present in the given set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
microwave_present = "microwave" in mySet
print("Is microwave present?", microwave_present)  # Output: Is microwave present? True

# 4. Remove "kettle" from the set
mySet.remove("kettle")
print("Set after removing kettle:", mySet)  # Output: Set after removing kettle: {'oven', 'microwave', 'refrigerator'}

# 5. Loop through the set
print("Looping through the set:")
for item in mySet:
    print(item)
# Output:
# Looping through the set:
# oven
# microwave
# refrigerator

# 6. Add elements in the list to elements in the set
mySet = {"apple", "banana", "orange", "kiwi"}
myList = ["pear", "grape"]
mySet.update(myList)
print("Updated set:", mySet)  # Output: Updated set: {'kiwi', 'grape', 'apple', 'banana', 'orange', 'pear'}

# 7. Join two sets of ages and first names
ages = {25, 30, 35}
first_names = {"John", "Emily", "Michael"}
joined_set = ages.union(first_names)
print("Joined sets:", joined_set)  # Output: Joined sets: {'John', 35, 25, 'Michael', 30, 'Emily'}
                
                #EXERCISE 4

# 1. Concatenate an integer and a string using the correct method
num = 10
text = "Apples"
concatenated = str(num) + text
print("Concatenated string:", concatenated)  # Output: Concatenated string: 10Apples

# 2. Remove spaces at the beginning, in the middle, and at the end of the string
txt = "      Hello,       Uganda!       "
trimmed = txt.strip()
print("Trimmed string:", trimmed)  # Output: Trimmed string: Hello,       Uganda!

# 3. Convert the value of 'txt' to uppercase
uppercase = txt.upper()
print("Uppercase string:", uppercase)  # Output: Uppercase string:       HELLO,       UGANDA!       

# 4. Replace 'U' with 'V' in the string
replaced = txt.replace("U", "V")
print("String with replaced character:", replaced)  # Output: String with replaced character:       Hello,       Vganda!       

# 5. Return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print("Range of characters:", range_of_characters)  # Output: Range of characters:  am

# 6. Correct the code to avoid an error
x = 'All "Data Scientists" are cool!'
print("Corrected string:", x)  # Output: Corrected string: All "Data Scientists" are cool!


                #EXERCISE 5
# 1. Print the value of the shoe size from the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print("Shoe size:", shoe_size)  # Output: Shoe size: 40

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])  # Output: Updated brand: Adidas

# 3. Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)  # Output: Updated dictionary: {'brand': 'Adidas', 'color': 'black', 'size': 40, 'type': 'sneakers'}

# 4. Return a list of all the keys in the dictionary
keys_list = list(Shoes.keys())
print("List of keys:", keys_list)  # Output: List of keys: ['brand', 'color', 'size', 'type']

# 5. Return a list of all the values in the dictionary
values_list = list(Shoes.values())
print("List of values:", values_list)  # Output: List of values: ['Adidas', 'black', 40, 'sneakers']

# 6. Check if the key "size" exists in the dictionary
size_exists = "size" in Shoes
print("Does 'size' exist?", size_exists)  # Output: Does 'size' exist? True

# 7. Loop through the dictionary
print("Looping through the dictionary:")
for key, value in Shoes.items():
    print(key + ":", value)
# Output:
# Looping through the dictionary:
# brand: Adidas
# color: black
# size: 40
# type: sneakers

# 8. Remove "color" from the dictionary
Shoes.pop("color")
print("Dictionary after removing 'color':", Shoes)  # Output: Dictionary after removing 'color': {'brand': 'Adidas', 'size': 40, 'type': 'sneakers'}

# 9. Empty the dictionary
Shoes.clear()
print("Empty dictionary:", Shoes)  # Output: Empty dictionary: {}

# 10. Create a dictionary and make a copy of it
original_dict = {"a": 1, "b": 2, "c": 3}
copied_dict = original_dict.copy()
print("Copied dictionary:", copied_dict)  # Output: Copied dictionary: {'a': 1, 'b': 2, 'c': 3}

# 11. Show nested dictionaries
nested_dict = {"person1": {"name": "John", "age": 30}, "person2": {"name": "Emily", "age": 25}}
print("Nested dictionaries:")
for person, details in nested_dict.items():
    print(person + ":", details)
# Output:
# Nested dictionaries:
# person1: {'name': 'John', 'age': 30}
# person2: {'name': 'Emily', 'age': 25}

