def greet(name):
    print(f"Hello, {name}")


greet("Alice")

def greet_all(names):
    for name in names:
        greet(name)

list_of_names = input("Write a list of names")
greet_all(["Alice","Bob","Charlie"])