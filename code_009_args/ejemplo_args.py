
# ejemplo unpacking
print("Ejempo unpacking")
elements = [1, 2, 3, 4]
first, *rest = elements
print(first, rest)

# ejemplo desempaquetar una secuencia al llamar una función
print()
print("Ejempo desempaquetar una secuencia al llamar una función")
print(*elements)
print(elements)

# ejemplo *args
print()
print("Ejempo *args en una función de Python")

def func(*args):
    for arg in args:
        print(arg)

print("Ejemplo 1, 2, 3")
func(1, 2, 3)

print("Ejemplo 1, 2, 3, a, b, c")
func(1, 2, 3, "a", "b", "c")

