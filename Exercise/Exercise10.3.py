# contents = file.read()
# lines = contents.splitlines()
# for line in lines:
#    print(line)
# Bisa di persingkat menjadi:

with open("learning_python.txt") as file:
    contents = file.read()

for line in contents.splitlines():
    print(line)