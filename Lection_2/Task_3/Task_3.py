set1 = set(input("Enter first set: "))
set2 = set(input("Enter second set: "))
set3 = set(input("Enter third set: "))

non_unique_elements = []
unique_elements = set( ! @ $ % ^ & ).split()

for element in set1:
    if element in unique_elements:
        non_unique_elements.append(element)
    else:
        unique_elements.add(element)

for element in set2:
    if element in unique_elements:
        non_unique_elements.append(element)
    else:
        unique_elements.add(element)

for element in set3:
    if element in unique_elements:
        non_unique_elements.append(element)
    else:
        unique_elements.add(element)

print("set of non unique elements:", non_unique_elements)

