# Build a command-line tool that lets users interact with a store and browse different departments.
#
# The first "page" should look like this:
#
# Welcome to My Fancy Store!
# Departments:
# 1. Shoes
# 2. Pets
# 3. Kitchenware
# 4. Tractors
#
# Choose a department to browse or enter q to exit.
# user chooses 3
# You chose department 3. Kitchenware
# Print a store welcome message w/ the departments
# Take in user input
# Do stuff with the user input
# Repeat until user quits
# Potential Classes
# Department
# User / Customer
# Products
# Registers -- some way of payment?
from typing import List


class Department:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Store:
    def __init__(self, name, departments):
        self.name = name
        # List[Department] is a type hint for readability -- similar to how you define types in typescript
        # but in this case it doesn't have any functionality outside of making code more readable
        self.departments: List[Department] = departments

    def __str__(self):
        return f"{self.name}: {[department.name for department in self.departments]}"

    def print_welcome(self):
        print(f"Welcome to {self.name}!")
        print("Browse our departments:")
        for i, department in enumerate(self.departments):
            print(f"{i+1}. {department.name}")


store = Store("Lambda Store", [
    Department("Python"),
    Department("CS"),
    Department("Data Science"),
    Department("React")
])
# print(store)
while True:
    store.print_welcome()
    user_input = input("Choose a department or enter q to quit:\n")
    # Is there a better way to get the department corresponding to the user input
    # that is more encapsulated?
    print(f"You chose department {store.departments[int(user_input)-1]}")
