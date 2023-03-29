string = input("enter your text:")
char = input("character to be counted:")

count = 0
for i in string:
    if i == char:
        count += 1

print(f"character '{char}' on string '{string}' equals: {count}.")
