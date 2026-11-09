with open("learning_python.txt") as file:
    contents = file.read()

print(contents)

with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())