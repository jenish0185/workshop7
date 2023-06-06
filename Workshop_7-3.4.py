with open('expressions.txt', 'r') as f:
    for line in f:
        expression = line.strop()
        result = eval(expression)
        print(f"{expression} = {result}")
        