# 1.
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    number_one = int(in_file.readline())
    number_two = int(in_file.readline())
print(number_one + number_two)

# 4.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)