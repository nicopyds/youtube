#         0  1  2
values = [2, 0, 3]

# 1. Añadir documentación 
# 2. Añadir tipado
# 3. Validar los params de entrada

def find_index(values, func):
    index = values.index(func(values))
    message = f"""
        For this values {values}
        and this function {func.__name__}
        we have this output {index}
    """
    print(message)
    return index

find_index(values=values, func=min)
find_index(values=values, func=max)

