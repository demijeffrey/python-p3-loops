#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    pass
    squared = [num * num for num in int_list]
    return squared

def fizzbuzz():
    # code goes here!
    pass
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f"{i}")


#### FIZZBUZZ SOLUTION ####
# def fizzbuzz():
#     for i in range(1, 101):
#         if not i % 15:
#             print("FizzBuzz")
#         elif not i % 5:
#             print("Buzz")
#         elif not i % 3:
#             print("Fizz")
#         else:
#             print(i)