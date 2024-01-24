def process_integer(integer, operation):
    if operation == 'double':
        return integer * 2
    elif operation == 'halve':
        return integer / 2
    elif operation == 'subtract':
        return integer - 1
    elif operation == 'add':
        return integer + 3
    else:
        return "Invalid operation"