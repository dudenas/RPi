import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = (f"Hi, {who_to_greet}!")
    return greeting


print(greet('is'))
print(greet('it'))
print(greet('new?'))
