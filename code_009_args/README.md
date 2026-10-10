----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre los *args en Python.

Los *args se suele considerar como un concepto "avanzado" en Python pero creo que esto
se debe sobre todo porque la sintáxis de "*algo" tiene muchos usos y a veces, en función
del contexto donde aparece, en realidad realiza operaciones opuestas.

Pero no lo vamos a complicar más.

Nosotros hoy nos centraremos en explicar únicamente los casos cuando *args
aparece dentro de la definición de una función en Python.

En concreto, si alguna vez has visto una función parecida a la siguiente:

```python

def func(*args, **kwargs):

```

Y te has planteado que hacen los *args y los **kwargs, están de enhorabuena porque 
hoy vamos a explicar los *args y en el siguiente los **kwargs.

Empecemos.

----

Lo primero que vamos a hacer, es plantear un caso práctico.

Y de hecho, uno de los motivos de porque hago este vídeo hoy es porque muchos de los
ejemplos que te encuentras cuando se explican los *args tiene que ver con un ejemplo
de `suma` y te muestran un ejemplo parecido a este:

```python
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
```

Y puedes llegar a utilizar la función de la siguiente manera:

```python
print(suma(1, 2, 3))
print(suma(4, 5, -7))
```

Ahora bien, yo siempre me preguntaba, porque no utilizar la función nativa de `sum`.

----

Pues bien, voy a intentar plantear un ejemplo "un poco más real".

Imagina que eres un Data Analyst en Spotify y tu tarea es hacer análisis de diferentes 
canciones.

En concreto, de manera regular trabajas con un dataset parecido a este: 

```text
                 track_id                                         track_name      track_artist  valence    tempo duration_ms
0  6f807x0ima9a1j3VPbc7VN  I Don't Care (with Justin Bieber) - Loud Luxur...        Ed Sheeran    0.518  122.036      194754
1  0r7CVbZTWZgbTCYdfa2P31                    Memories - Dillon Francis Remix          Maroon 5    0.693   99.972      162600
2  1z1Hg7Vb0AhHDiEmnDE79l                    All the Time - Don Diablo Remix      Zara Larsson    0.613  124.008      176616
3  75FpbthrwQmzHlBJLuGdC7                  Call You Mine - Keanu Silva Remix  The Chainsmokers    0.277  121.956      169093
4  1e8PAfcKUYoKkxPhrHqw4x            Someone You Loved - Future Humans Remix     Lewis Capaldi    0.725  123.976      189052
```

Pues bien, de manera recurente tu jefe te hace diferentes preguntas sobre este dataset.

¿Cuantas canciones tenemos?

¿Cuales son los diferentes estádisticos de este dataset?

¿Dime los primeras cinco canciones más populares? 

¿Dime las últimas cinco canciones que se han añadido?

Etc etc etc

Un tema importante para que se entienda bien el caso que planteamos es que nuestro jefe
es exigente y cada día nos pregunta diferentes cosas y en diferente orden. 

Esto lo digo, porque no podemos predecir que nos va a preguntar ni el número de preguntas
que nos va a hacer.

En este caso, podemos empezar a plantear una solución parecida a la esta:

```python

def versatile_func(df, *, head = True, tail = True, describe = True):
    if head:
        print("El head del df es:")
        print(df.head())
    if tail:
        print("El tail del df es:")
        print(df.tail())
    if describe:
        print("El describe del df es:")
        print(df.describe())

versatile_func(df, head = True, tail = False, describe = False)
versatile_func(df, head = False, tail = False, describe = True)

```

Planteamos una función "versátil" donde defino diferentes métodos y en función de si
el flag es verdadero (en función de si me jefe me pregunta o no) puedo obtener un 
resultado o no.

Esta función la puedo utilizar de la siguiente manera y puedo salir de paso.

Ahora bien, un problema clave que plantea esta solución es ¿que pasa si ahora mi jefe
me pregunta algo nuevo?

Puedo ir a añadir un nuevo parámetro a mi función pero claramente no es una solución
demasiada práctica.

```python

def versatile_func(df, head = True, tail = True, describe = True, sample=True):
    if head:
        print("El head del df es:")
        print(df.head())
    if tail:
        print("El tail del df es:")
        print(df.tail())
    if describe:
        print("El describe del df es:")
        print(df.describe())
    if sample:
        print("El sample del df es:")
        print(df.sample())

versatile_func(df, head = True, tail = False, describe = False, sample=True)
versatile_func(df, head = False, tail = False, describe = True, sample=True)

```

Acabaremos en una jungla de ifs y un montón de booleanos.

Necesitamos una solución más elegante.

---

Una cosa quiero haceros ver del anterior ejemplo es que mi jefe me puede preguntar un 
número indetermiado de cosas. Un día pueden ser 3 y otras veces pueden ser 10.

Para estos casos, yo necesito plantear una función parecida. Una función que acepte
un número indeterminados de parámetros.

En Python, los *args sirven justo para este propósito: definir funciones muy flexibles
que aceptan un número indeterminados de parámetros.

¿Como se traslada esto a nuestro ejemplo de antes? 

Veamos:

El cambio que voy a hacer a mi función es eliminar todos los flags.

El primer parámetro de mi función sigue siendo el `pandas.DataFrame` pero posteriormente
lo que voy a hacer es añadir esta sintáxis de *args.

Args es sólo un nombre y en realidad puedo llamarlo *métodos o lo que *cosas, pero 
el consenso es llamarlo *args.

Este args en Python, lo que hará es recoger, todos los parámetros posicionales después
del df en una tupla llamada args.

Si nunca has escuchado sobre parámetros posicionales en Python, tengo varios vídeos que
hablan sobre estos conceptos, así que quizás te puede interesar verlos más tarde.

Al recoger todos los valores en la tupla args, puedo iterar sobre ella 

```python

def versatile_func(df, *args):
    for arg in args:
        func = getattr(df, arg)
        print(f"El {arg} del df es:")
        print(func())

versatile_func(df, "head", "tail", "describe")

```

---

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

