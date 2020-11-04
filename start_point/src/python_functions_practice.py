import calendar

# Function that returns an int of value 10. 
def return_10():
    return 10 

# Function that returns the sum of two int args.
def add(num_1, num_2):
    return num_1 + num_2

# Function that returns the sub of two int args.
""" Note, order of args is important to returned value, good old subtraction :) """ 
def subtract(num_1, num_2):
    return num_1 - num_2

# Function that returns the product of two int args. 
def multiply(num_1, num_2):
    return num_1 * num_2

# Function that returns the division of two int args.
def divide(num_1, num_2):
    return num_1 / num_2 

# Function that returns the lenght of an string arg. 
def length_of_string(input_string):
    return len(input_string)

# Function that concatenates two string args.
def join_string(string_1, string_2):
    return string_1 + string_2

# Function that take two strings of number value args and returns the sum as an int.
def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

# Function that returns the name of a month given an int arg of 
# it's place in a year (i.e 1-12)
def number_to_full_month_name(int_month):
    return calendar.month_name[int_month]





