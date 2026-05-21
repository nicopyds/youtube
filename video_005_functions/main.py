from typing import Union

#         0  1  2
values = [2, 0, 3]

# 1. Añadir documentación 
# 2. Añadir tipado
# 3. Validar los params de entrada

def find_index(values:list, func:Union[min, max]) -> int:
    """Returns the index of the maximum or minimum value in a list.
    
    Args:
        values (list): list with integer or float values.
        func (callable): must be the default Python max or min function.
    
    Returns:
        int: index of the value in the list. In case we have more than one solution
             the first index is returned.
    """
    assert isinstance(values, list), f"values must be a list, we have {type(values)}"
    assert func in (min, max), "func must be the built in min or max function"

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
#find_index(values=set(values), func=max)
find_index(values=values, func=abs)
