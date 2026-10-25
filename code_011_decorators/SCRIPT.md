----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre los decoradores en Python.

Creo que después de haber cubierto mucha temática alrededor de funciones en Python,
tenemos todas las piezas necesarias para abarcar los decoradores.

Os recomiendo antes a que le echen un vistazo a los vídeos anteriores porque sin lugar a dudas
os ayudará a entender los decoradores mucho mejor. 

Sobre todo, los *args y los **kwargs serán de gran ayuda porque hoy los vamos a 
usar un montón.

Los decoradores se suelen considerar un concepto avanzado en Python, pero ya veréis que
no tienen mucho misterio.

Empecemos.

----

Los primero que vamos a hacer es plantear un ejemplo práctico.

Supongamos que estamos trabajando en un sistema y últimamente hemos notado una 
ralentización.

Después de indagar un poco, creemos que hemos dado con el culpable y tenemos a esta
función como el principal sospechoso. 

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

Y nosotros nos ponemos a trabajar en ello.

Una implementación sencilla es hacer algo parecido a esto.

Empezamos medir el momento exacto cuando arranca nuestra función, con el time.time()

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
    print(f"Executed correctly function1 with {param1=} and {param2=}")

    end = time.time()
    total_time = end - start
    
    print(f"Total time to execute suspicious_function took {total_time}")


    return True
```

Y luego medimos el momento exacto cuando acaba nuestra ejecución. 

Testeamos nuestro código y obtenemos el siguiente resultado:

```text
Executed correctly function1 with param1='fast' and param2=10
Total time to execute suspicious_function took 1.0053367614746094
```

Y aquí nos damos cuenta que la función se comporta como debe y que no es el culpable.

Debemos seguir indagando.

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
    print(f"Executed correctly function2 with {param1=}, {param2=} and {param3=}")

    return True
```

Y claro, podríamos ir a implementar exactamente lo mismo que antes, pero podemos 
hacerlo mucho mejor.

----

Supongo que todos nosotros estaremos de acuerdo con que, si tuvieramos una función que
acepte otra función como parámetro, la pueda ejecutar y también medir su rendimiento
como en nuestro caso, sería una solución mucho mejor.

Surgen no obstante un par de preguntas importantes:

La primera pregunta: ¿podemos pasar una función como parámetro a otra función?

Y la respuesta es que sí. En Python las funciones son ciudadanos de primer orden y esto
que implica que podemos pasar una función como parámetro a otra función.

La segunda pregunta que surge es. Si la función que quiero medir acepta paramétros 
(en nuestro caso param1, param2, param3 etc): ¿hay alguna forma de hacerlas llegar?

La respuesta es también afirmativa. En Python tenemos los *args y los **kwargs que nos
permite suministrar un número indeterminados de parámetros posicionales o keyword arguments
a una función.

Posteriormente podemos recogerlos en una tupla y diccionario respectivamente y reenviarlos a 
nuestra función destino.

Por tanto, Python tiene todos los mecanismos necesarios resolver problema que se nos
plantea.

----

Antes hemos comentado que queremos una función que acepte otra como parámetro, la ejecute
pero también que haga algo más (en nuestro caso, medir el tiempo). 

Este es el principal próposito de los decorades.

Los decoradores permiten añadir funcionalidad extra a una función o método sin cambiar 
su código fuente. 

Parece magia pero no lo es.

Normalmente la estructura de un decorador es la siguiente:

```python
def decorador(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs):
        return result
    return wrapper
```

Intervienen 3 funciones:
1. Tenemos nuestra función decoradora: llamada aquí decorador.
2. Tenemos la función que queremos decorar, en nuestro caso se llamará func.
3. Y tenemos una función interna llamada wrapper que es la encargada de añadir 
    la funcionalidad extra.

Además, el wrapper acepta *args y **kwargs para que a nuestra func le lleguen todos los
parámetros.

Podemos observar que el wrapper ejecutará la función principal y devolverá su resultado.

Y posteriormente el decorador devolverá el wrapper.

Dado que este ya contiene el resultado que queremos junto con la funcionalidad extra,
tenemos todo lo que queremos.

----

>Posible Short<

Vamos ahora a implementar nuestro decorador. Y ya veréis que es muy sencillo.

Empezamos definiendo una función llamada timer que acepta una función.

Dado que el timer nos servirá para medir cualquier función, el nombre del parámetro 
será func.

Posteriormente, dentro de esta función definimos un wrapper que añadira la funcionalidad
extra a nuestra func.

Queremos que sea lo más flexible posible y que funcione con todo tipo de
funciones y métodos, por este motivo le decimos que acepta *args y **kwargs. 

Dentro ejecutamos nuestra función principal y para ello le pasamos los args y kwargs. 

Recogemos y devolvemos su resultado pero dado que queremos expandir su funcionalidad,
mido cuando empieza y acaba la ejecución de mi función.

Sacamos el tiempo transcurrido y lo reportamos.

Por último devolvemos el wrapper que ahora mismo contiene el resultado de nuestra
ejecución junto con la funcionalidad extra.

```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        r = func(*args, **kwargs)

        end = time.time()
        total_time = end - start
        print(f"Total time to execute {func.__name__} took {total_time}")
        
        return r
    return wrapper
```

Ya tengo mi decorador.

A la hora de usarlo para decorar una función, tengo dos opciones:
   1. Puedo hacerlo creando una nueva función con la sintaxis: 

   ```python
   suspicious_function3 = timer(func=suspicious_function2)
   ```

   2. O bien puedo hacerlo usango el aroba `@`.

   ```python
   @timer
   def suspicious_function2(param1: str, /, param2: int, param3: str) -> bool:
        ...
   ```

Ahora podemos ejecutar nuestro código sin cambios y tendremos la nueva funcionalidad y
además tendremos un timer que puedo usar para decorar cualquier función en nuestro 
proyecto.

----

En resumen, un decorador es una función que permite añadir funcionalidad extra a nuestro
código sin modificar su código fuente.

Es una patrón muy versátil que se utiliza mucho en desarrollo web y también en muchos
paquetes de Python.

Conocerlo y usarlo sin lugar a dudas te ayudará a ser un mejor programador.

Ponme en los comentarios si has usado decoradores o si te queda alguna duda.

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarla
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

