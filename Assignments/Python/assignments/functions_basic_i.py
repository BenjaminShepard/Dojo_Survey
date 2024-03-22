# 1
def number_of_food_groups():
    return 5


print(number_of_food_groups())

# Prediction - 5


# 2
def number_of_military_branches():
    return 5


print(
    number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()
)
# Prediction - 5
# Correct answer - code errored out because number_of_days_in_a_week_silicon_or_triangle_sides is not defined


# # 3
def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())
# Prediction - 5, 10
# Correct answer - only returned 5, im assuming becuase after it reached the first return the code does not run again to try and return the 10


# # 4
def number_of_fingers():
    return 5
    print(10)


print(number_of_fingers())
# # Prediction - 5
# # Just like the previous one this only returns the 5 because the print(10) statement is after the return and does not get executed becuase the return 5 ends the code


# # 5
def number_of_great_lakes():
    print(5)


x = number_of_great_lakes()
print(x)
# # Prediction - 5, none
# # This function will print the 5 but since there is no a return statement in the function it automatically returns none


# # 6
def add(b, c):
    print(b + c)


print(add(1, 2) + add(2, 3))
# # Prediction - 3, 5
# # First  part of the prediction was correct, after it printed 3, 5 on seperate lines an error occured indicatin the + sign in pring(add(1, 2) + add(2, 3)). Unsure why


# # 7
def concatenate(b, c):
    return str(b) + str(c)


print(concatenate(2, 5))
# # Prediction - 25
# this function takes b and c and turns them into strings then will concatenates/comabines them as strings. Does not add the m together as if they were numbers


# # 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(number_of_oceans_or_fingers_or_continents())
# # Prediction - 100, 10
# # this function will print 100 becuase thats what is called immediatley then goes on to runt he if statement and since b is greater than 10 the else parts is true which will return 10


# # 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(
    number_of_days_in_a_week_silicon_or_triangle_sides(2, 3)
    + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3)
)
# # Prediction - 7, 14, 21
# # in the first call 2 < 3 so returns 7. In the second call 5 > 3 so returns 14. in the third call 2 < 3 so returns 7 the 5 > 3 so returns 14. Then adds the numbers 7 and 14 due to the + sign to get 21.


# # 10
def addition(b, c):
    return b + c
    return 10


print(addition(3, 5))
# # Prediction -  8
# # Just outputs the first return statement because the function is immediatley exited afterwards.


# # 11
b = 500
print(b)


def foobar():
    b = 300
    print(b)


print(b)
foobar()
print(b)
# # Prediction - 500, 300, 500
# # Correct outcome - 500, 500, 300, 500. So my understanding is the first part will print b which is 500 then will do nothing with the function until it is called on to print the local variable 300 so the outcome is 500, 500, 300, 500


# # 12
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)
# # Prediction - 500, 500, 300, 500


# # 13
b = 500
print(b)  # --> prints 500 immediatley


def foobar():
    b = 300
    print(b)  # --> this doesnt do anything yet because it hasnt been invoked/called on
    return b


print(b)  # --> prints 500 again
b = foobar()  # --> sets b equal to the local value of foobar which is 300 and prints is
print(b)  # --> prints b again but with the new value from foobar
# # Prediction - 500, 500, 300, 300


# # 14
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


foo()
# # Prediction -1, 3, 2


# 15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)
# Prediction - 1, 3, 5, 10
