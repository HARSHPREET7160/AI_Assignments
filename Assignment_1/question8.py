# A) Make a class called Restaurant. The __init__() method for Restaurant should store two 
# attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
# that prints these two pieces of information, and a method called open_restaurant() that prints a 
# message indicating that the restaurant is open. Make an instance called restaurant from your 
# class. Print the two attributes individually, and then call both methods. 
# B) Make a class called User. Create two attributes called first_name and last_name, and then 
# create several other attributes that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information. Make another method called 
# greet_user() that prints a personalized greeting to the user. Create several instances representing 
# different users, and call both method for each user.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name and type of cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Gourmet Haven", "French")

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()



class User:
    def __init__(self, first_name, last_name, **additional_info):
        """Initialize the user's first name, last name, and other attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.additional_info = additional_info

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.additional_info.items():
            print(f"  {key.capitalize()}: {value}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

user1 = User("Alice", "Johnson", age=25, location="New York", profession="Software Engineer")
user2 = User("Bob", "Smith", age=30, location="California", hobby="Photography")
user3 = User("Charlie", "Brown", age=22, location="Texas", hobby="Gaming", status="Student")


user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
