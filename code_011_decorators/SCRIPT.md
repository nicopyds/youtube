----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre los decoradores en Python.

Creo que después de haber cubierto mucha temática alrededor de funciones en Python,
tenemos todas las piezas para abarcar los decoradores.

Os recomiendo a que le echen un vistazo a los vídeos anteriores porque sin lugar a dudas
os ayudará a entender los decoradores mucho mejor. 

En especial, los *args y los **kwargs serán de gran ayuda porque hoy los vamos a 
usar un montón.

Los decoradores se suelen considerar un concepto avanzado en Python, pero ya veréis que
no tienen mucho misterio.

Empecemos.

----

Los primero que vamos a hacer es plantear un ejemplo práctico.

Supongamos que estamos trabajando en un sistema y últimamente hemos notado una 
ralentización general.

Después de indagar un poco, creemos que hemos dado con el culpable y tenemos una
función que es el principal sospechoso. 

```python
def suspicious_function(param1:str, /, param2:int) -> bool:
    """
    A function in our system that we think is very slow.
    
    Returns:
    -------
    bool
    """
    
    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(5)
    print(f"Everything executed correctly {param1=} with {param2=}")
    
    return True
```

Pues bien, nos piden medir el rendimiento de esta parte de nuestro código.

Y nosotros nos ponemos manos a la obra.

Una implementación sencilla es hacer algo parecido a esto:

```python
def suspicious_function(param1: str, /, param2: int) -> bool:
    """
    A function in our system that we think is very slow.

    Returns:
    -------
    bool
    """

    start = time.time()

    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(1)
    print(f"Executed correctly in function1 with {param1=} and {param2=}")

    end = time.time()
    total_time = end - start
    
    print(f"Total time to execute suspicious_function took {total_time}")


    return True
```

Ejecutamos el código y obtenemos el siguiente resultado:

```text
Executed correctly in function1 with param1='fast' and param2=10
Total time to execute suspicious_function took 1.0053367614746094
```

Y aquí nos damos cuenta que la función se comporta como debe y que debemos seguir 
indagando.

Tras un rato mirando nuestro código, damos con otro posible sospechoso.

```python
def suspicious_function2(param1: str, param2: int, param3: str) -> bool:
    """
    A function in our system that we think is very slow.

    Returns:
    -------
    bool
    """

    # en realidad la función puede llamar una API, procesar un dataset
    # escribir en una BBDD etc
    # en nuestro ejemplo haremos que duerma durante 5 segundos
    time.sleep(5)
    print(f"Executed correctly in function2 with {param1=}, {param2=} and {param3=}")

    return True
```

Y claro, podríamos ir a implementar exactamente lo mismo que antes, pero podemos 
hacerlo mucho mejor.

----

Supongo que todos nosotros estaremos de acuerdo con que, si tuvieramos una función que
acepte otra función como parámetro, la pueda ejecutar y también medir su rendimiento
como en nuestro caso, sería una solución mucho mejor.

Surgen no obstante un par de preguntas importantes:

La primera pregunta: ¿podemos pasar una función comp parámetro a otra función?

Y la respuesta es sí. En Python las funciones son ciudadanos de primer orden y esto
que implica que podemos pasar una función como parámetro a otra función.

La segunda pregunta que surge es. Si la función que quiero medir acepta paramétros 
(en nuestro caso param1, param2, param3 etc): ¿hay alguna forma de hacerlas llegar?

La respuesta es también afirmativa. En Python tenemos los *args y los **kwargs que nos
permite suministrar un número indeterminados de parámetros posicionales o keyword arguments
a una función, recogerlos en una tupla y diccionario respectivamente y reenviarlos a 
nuestra función destino.

Por tanto, Python tiene todos los mecanismos necesarios resolver este problema.

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

