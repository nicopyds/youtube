
def find_index(values, func):

    index = values.index(func(values))
    print(values, func, index)

    return index

if __name__ == "__main__":
    values = [1, 2, 3]
    func = max
    find_index(values=values, func=func)

    values = [-1, 2, 3]
    func = min
    find_index(values=values, func=func)
