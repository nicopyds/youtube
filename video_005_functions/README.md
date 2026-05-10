----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

El vídeo de hoy me da miedo que vaya a ser un vídeo polémico y es que vamos a hablar 
sobre funciones en Python.

En concreto, quiero explorar con vosotros que significa definir una buena función en Python.

Esto que a priori puede parecer algo muy sencillo y básico, en realidad no es tan trivial 
y quiero que juntamos hagamos una reflexión.

Empecemos.

----

Lo primero, vamos a definir una función muy sencilla en Python.

Supongamos que tenemos una lista de valores númericos (pueden ser enteros o no) y 
nuestro objetivo, al menos la comienzo, es calcular el índice del valor máximo o mínimo
dentro de esta lista.

Para ellos vamos a definir la siguiente función:

```python

def find_index(values, func):

    index = values.index(func(values))

    return index

```

Nosotros ahora mismo podemos ejecutar esta función sin problemas tal y como lo haremos
a continuación.

Vamos a crear una lista con los valores [1, 2, 3] y usaremos la función de min para
ver si el resultado es correcto o no.

Ejecutamos ahora la función y vemos que todo sale según lo esperado.

Yo me encuentro con que muchas veces, nos quedamos aquí. Y lo entiendo perfectamente, ya
que muchas veces las prisas y los deadlines no nos da tiempo para más.

Pero aquí tenemos por lo menos varias mejoras que podemos aplicar a nuestra función.
1. Añadir documentación.
2. Añadir tipado.
3. Añadir los tipos esperados que esta función debe devolver. 
4. Validar los parámetros de entrada.

Vayamos ahora paso a paso aplicando cada una de estas cosas y vemos el resultado final.

----

La documentación quizás es la parte más obvia y que todo el mundo sabe, al menos en teoría,
que se debe añadir a nuestro código.

Conozco muchos compañeros del sector, que vienen de otros lenguajes de programación donde
o bien no existe esta costumbre de la documentación o bien tiran del viejo mantra: mi
código se entiende/explica sólo. Y aunque entiendo los dos puntos de vista, me voy a 
remitir a PEP8.

Los PEP dentro del mundo Python son: Python Enhancement Proposals. 

Básicamente es como un foro donde se pueden solicitar mejoras al lenguaje y su ecosistema.

Aquí muchas veces se proponen y se deban diferentes mejoras desde: abandonar el GIL a como
se debe organizar la comunidad etc

Pues bien, uno del os PEP más relevantes desde siempre es el PEP8, publicado en 2001 por
parte de Guido van Rossum y tiene el nombre de `PEP 8 – Style Guide for Python Code`

https://peps.python.org/pep-0008/#documentation-strings

Dento de este PEP se discute el "estilo" que debemos intentar seguir a la hora de escribir
código Python: desde si seguir el camelcase o snakecase hasta la identación o variables globales.

Una cosa relevante de este PEP es la opinión de Guido respecto a la documentación donde dice:

```text
Write docstrings for all public modules, functions, classes, and methods.
```

Escribe documentación para todas las funciones, clases, métodos y módulos públicos.

Punto pelota.

Escribir documentación en Python no es algo "extra" es la esencia misma de escribir buen código
o código "pythonic".

Si quieren leer más en profunidad sobre las convenciones respecto a la documentación en
Python, os dejo el PEP257

https://peps.python.org/pep-0257/

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

