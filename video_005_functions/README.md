----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

El vídeo de hoy me da un poco de miedo que vaya a ser un polémico y es que vamos a hablar 
sobre funciones en Python.

En concreto, quiero explorar conjuntamente con vosotros que significa definir una 
buena función en Python.

Esto que a priori puede parecer algo muy sencillo y básico, en realidad no es tan trivial 
y quiero que juntos hagamos una reflexión.

Empecemos.

----

Lo primero, vamos a definir una función muy sencilla en Python.

Supongamos que tenemos una lista de valores númericos (pueden ser enteros o no) y 
nuestro objetivo, al menos al comienzo, es calcular el índice del valor máximo o mínimo
dentro de esta lista.

Es decir, si yo le paso a mi función la siguiente lista:
```python
l = [2, 0, 3]
```
y también le suministro la función de `min`, es de esperar que la función de devuelva
el índice de 1 porque el valor más pequeño corresponde al valor 0.

Para ellos vamos a definir la siguiente función:

```python
def find_index(values, func):

    index = values.index(func(values))

    return index
```

Nosotros ahora mismo podemos ejecutar esta función sin problemas tal y como lo haremos
a continuación.

Vamos a crear una lista con los valores [2, 0, 3] y usaremos la función de min para
ver si el resultado es correcto o no.

Ejecutamos ahora la función y vemos que todo sale según lo esperado.

Yo me encuentro con que muchas veces, nos quedamos aquí. Y lo entiendo perfectamente, ya
que muchas veces las prisas y los deadlines no nos da tiempo para más.

¿Pero como deberíamos funcionar en un mundo ideal? ¿Mejoras podemos hacer a esta función?

Os recomiendo a que pausen el vídeo durante unos 2 minutos y apunten las ideas que os vienen
a la cabeza. Posteriormente vamos a poder comprar.

A mi me vienen a la cabeza por lo menos los siguientes 3 puntos de mejora:
1. Añadir documentación.
2. Añadir tipado.
3. Validar los parámetros de entrada.

Vayamos ahora paso a paso aplicando cada una de estas cosas y vemos el resultado final.

----

La documentación quizás es la parte más obvia y que todo el mundo sabe, al menos en teoría,
que se debe añadir a nuestro código.

Conozco muchos compañeros del sector, que vienen de otros lenguajes de programación donde
o bien no existe esta costumbre de la documentación o bien tiran del viejo mantra: mi
código se entiende/explica sólo. 

Y aunque entiendo los dos puntos de vista, y tuve muchos debates de este estilo, 
yo me voy a remitir a PEP8.

Para los que no conocen: los PEP dentro del mundo Python son: Python Enhancement Proposals. 

Básicamente es como un foro donde se pueden solicitar mejoras al lenguaje y su ecosistema.

Aquí muchas veces se proponen y se debaten diferentes mejoras desde: abandonar el GIL a como
se debe organizar la comunidad etc

Pues bien, uno del os PEP más relevantes en la historia de Python es el PEP8, publicado en 2001 por
parte de Guido van Rossum y tiene el nombre de `PEP 8 – Style Guide for Python Code`

https://peps.python.org/pep-0008/#documentation-strings

Dento de este PEP se discute el "estilo" que debemos intentar seguir a la hora de escribir
código Python: desde si seguir el camelcase o snakecase hasta la identación o variables globales.

Una cosa relevante de este PEP es la opinión de Guido respecto a la documentación donde dice:

```text
Write docstrings for all public modules, functions, classes, and methods.
```

ESCRIBE DOCUMENTACIÓN PARA TODAS LAS FUNCIONES, CLASES, MÉTODOS Y MÓDULOS PÚBLICOS.

Punto pelota.

Escribir documentación en Python no es algo "extra" es la esencia misma de escribir buen código
o código "pythonic". Y el BDFL de Python así lo dice.

Si quieren leer más en profunidad sobre las convenciones respecto a la documentación en
Python, os dejo también el PEP257

https://peps.python.org/pep-0257/

Antes de escribir nuestra docu, también os tengo que decir que hay muchos estilos a la hora
de documentar nuestro código.

Yo que vengo del mundo del Machine Learning y Data Science, estoy muy influenciado por el
estilo que marca [scikit-learn](https://gist.github.com/jakevdp/3808292) que podéis ver 
a continuación y por el otro lado tenemos el estilo de [Google](https://chromium.googlesource.com/external/github.com/google/styleguide/+/f9347e1e9d79aee9cde0802fe178d72c8f87926c/pyguide.md)
o bien lo podemos ver aquí [Google](https://google.github.io/styleguide/pyguide.html).

Que se puede resumir en:

```text
Python uses docstrings to document code. A docstring is a string that is the first 
statement in a package, module, class or function. These strings can be extracted 
automatically through the __doc__ member of the object and are used by pydoc. 
(Try running pydoc on your module to see how it looks.) 
Always use the three-double-quote """ format for docstrings (per PEP 257). 
A docstring should be organized as a summary line 
(one physical line not exceeding 80 characters) terminated by a period, question mark, 
or exclamation point. When writing more (encouraged), this must be followed by a blank 
line, followed by the rest of the docstring starting at the same cursor position as the 
first quote of the first line. There are more formatting guidelines for docstrings 
below.
```

```python
def find_index(values, func):
    """Returns the index of the maximum or minimum value in a list.
    
    Args:
        values (list): list with integer or float values.
        func (callable): can be the default Python max or min function.
    
    Returns:
        int: index of the value in the list. In case we have more than one solution
             the first index is returned.
    """
    index = values.index(func(values))

    return index
```

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

