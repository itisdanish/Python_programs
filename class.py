# A class is like a blueprint for creating object.

#  Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def birthday(self):
        self.age+=1

# Init User object
danish = User('Danish Iqbal', 'yesiamdanish@gmail.com', 25)
test = User('Test bro', 'test@test.com',26)
test.birthday()
print(danish.greeting())
print(test.greeting())