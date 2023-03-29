x = float(input('number one:'))
y = float(input('number two:'))
operation = input('operation:')
result = None

if operation == 'x':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print("eror")
if result is not None:
    print("result:", result)

