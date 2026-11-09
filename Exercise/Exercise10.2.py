with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    modified_line = line.replace("Python", "C")
    print(modified_line.strip())