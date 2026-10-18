----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

El vídeo de hoy va a ser cortito y relacionado con el último vídeo que subí al canal.

En concreto, vamos a seguir hablando funciones en Python.

Empecemos.

----

Como pueden recordar, este es el código que hemos trabajado. 

Es una función muy sencilla que le pasas una lista de valores númericos y te devuelve
el índice del valor más pequeño o el valor más grande, dependiendo de si le pasas la 
función min o max.

```python
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
```

Vamos a aprovechar esta función para explicar 2 cosas adicionlaes que podéis encontrar
muy  a menudo en diferentes métodos y funciones en Python: me refiero a estos dos
símbolos `/` y `*`.

Estos dos símbolos, controlan como puedes enviar los parámetros a tu función.

Si no sabían, en Python existen dos formas de suministrar parámetros: posicional o por
keyword.

Posicional implica que los valores que tu le suministras a una función o método de una clase,
Python los asigna en el mismo orden que los parámetros que vienen dentro del paréntesis
es decir, respetan el orden que tu le pusiste cuando definias la función.

Keyword arguments, implica que cuando le pasamos los parámetros escribimos el nombre
del parametro y luego le damos el valor.

Pues, en Python se puede llegar a "forzar" a que determinados parámetros sea únicamente
posicionales y otros parámetros sea únicamente keyword arguments.

Veamos estos con unos ejemplos.

Lo primero que voy a hacer es añadir aquí es limpiar un poco nuestro código y añadir
un nuevo parámetro que controlara el print de nuestra función.

Le vamos a llamar verbose y le diremos que debe ser un booleano.

Ahora que tenemos 3 parametros, podemos llegar a invocar nuestra función de diferentes
maneras. Os pondré aquí algunos ejemplos.

```python
find_index(values, func = max, verbose = True)
find_index(values=values, func=max, verbose = True)
find_index(values, max, True)
```

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

