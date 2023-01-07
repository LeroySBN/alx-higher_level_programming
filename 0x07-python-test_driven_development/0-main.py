#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(1.0, 2.6))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

print(add_integer(1.0, 2.3))
print(add_integer(1.0, -2.0))
print(add_integer(-1, 2))
print(add_integer(-1.0, 2.0))
print(add_integer(-1.0, -2.0))
