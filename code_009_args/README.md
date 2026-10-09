----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre la sintáxis de *args en Python.

Los *args se suele considerar como un concepto "avanzado" en Python pero creo que esto
se debe sobre todo porque la sintáxis de "*algo" tiene varios usos en Python.

Nosotros hoy nos vamos a centrar en explicar únicamente los casos cuando *args
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

Imagina que eres un Data Analyst en Spotify y necesitas hacer un análisis de diferentes
canciones.

En concreto, tenemos una dataset parecido al siguiente:

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

¿Cuales son los difentes estádisticos de este dataset?

¿Dime los primeras cinco canciones más populares? 

Etc etc etc

Un tema importante para que se entienda bien el caso que planteamos es que nuestro jefe
es exigente pero no del todo constante y cada día nos pregunta diferentes cosas y no
siempre en el mismo orden.

Esto lo digo, porque no podemos predecir que nos va a preguntar ni el número de preguntas
que nos va a hacer.

En este caso, podemos empezar a plantear una solución parecida a la esta:

```python

def versatile_func(df, *, head = True, tail = True, describe = True, sample = True):
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

Planteamos una función "versátil" donde defino diferentes métodos y en función de si
es verdadero (en función de si me jefe me pregunta o no) puedo obtener un resultado o no.


Ahora bien, un problema clave que plantea esta solución es que pasa si ahora mi jefe
me pregunta algo nuevo.

Puedo ir a añadir un nuevo parámetro a mi función pero claramente no es una solución
demasiada práctica.

Acabaremos en una jungla de ifs y un montón de booleanos.

Necesitamos una solución más elegante.

---

Una cosa quiero haceros ver del anterior ejemplo es que mi jefe me puede preguntar un 
número indetermiado de cosas. Un día pueden ser 3 y otras veces pueden ser 10.

Para estos casos, yo necesito plantear una función igual. Una función que acepte
un número indeterminados de parámetros.

En Python, los *args sirven justo para este propósito: definir funciones muy flexibles
que aceptan un número indeterminados de parámetros.

¿Como se traslada esto a nuestro ejemplo de antes? 

Veamos:

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

