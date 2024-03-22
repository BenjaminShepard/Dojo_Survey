# here's the syntax for creating a class that we want to call User:
# we will be using the term method to refer to functions that specifically belong to a class, in other works, functions that are defined inside the scope of a class definition.
class User:
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

# Now that you have a class set pu with a constructor
# You can assing new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) #prints Ada

user_2 = User()
print(user_2.first_name) #also prints Ada



#and heres how we create a new instance of our class:

michael = User()
anna = User()


#This is a code preview of a class called Shoe

class Shoe:
    def __init__(self):
        self.brand = "Adidas"
        self.type = "tennis shoe"
        self.price = 45.99
        self.in_stock = True

        def rebrand(self, new_brand):
            self.brand = new_brand

        def sold_out(self):
            self.in_stock = False

        def on_sale(self, percent):
            self.price = self.price * (1 - percent)


print(Shoe)