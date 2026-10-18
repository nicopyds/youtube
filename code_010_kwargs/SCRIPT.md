----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre los *kwargs en Python.

Este vídeo complementará muy bien el vídeo anterior donde hemos visto los *args.

Vais a ver que los *args y los **kwargs en esencia se parecen mucho: dado que tanto uno como
el otro permiten pasar un número indeterminado de paramétros a una función o método
en Python.

La diferencia entre los dos radica sobre todo en que los *args trabajan con paramétros posicionales
mientras que los **kwargs sirven para los keyword arguments.

No obstante, la mayoría de las veces, cuando queremos definir una función que sea flexible
la definimos de tal manera que accepte tanto args como los kwargs.

Si tenéis cualquier duda sobre paramétros posicionales, keyword arguments o bien los
*args os recomiendo a que miren los otros vídeos que tengo en el canal porque en el
pasado ya hemos cubierto estos temas.

Ahora, sin más demora, empecemos la explicación sobre los kwargs.

---

Lo primero que vamos a hacer es refrescar brevemente lo que vimos en el último vídeo.

Somos un Data Analyst en Spotify y a diario trabajamos con un pandas DataFrame que
contiene información sobre diferentes canciones que se van subiendo a la plataforma.

El DataFrame que tenemos tiene este aspecto.

Pues bien, tenemos un jefe que es bastante exigente y que a menudo nos hace preguntas
sobre nuestro DataFrame.

El punto clave eso sí, es que hace diferentes preguntas cada día y no siempre son las
mismas.

Es imposible predecir lo que preguntará mañana así que para poder responderle en el 
menor tiempo posible, necesito una solución que sea lo más flexible posible.

Aquí es donde nosotros planteamos una función que use los *args de Python.

La solución es muy sencilla, acepta un DataFrame y posteriormente todos los paramétros
posicionales que queramos.

Posicional quiere decir de que no invoco el paramétro por su nombre.

Mirad aquí a la hora de invocar esta función, "head" y "tail" corresponden al paramétro
2 y 3 de esta función porque es la posición que tienen cuando ejecuto el código.

```python

def versatile_func(df, *args):
    print(args, type(args), len(args))
    for arg in args:
        if hasattr(df, arg):
            print(f"El {arg} del df es:")
            func = getattr(df, arg)
            print(func())


versatile_func(df, "head", "tail")
versatile_func(df, "tail", "describe")

```

Los args si se acuerdan fue la solución que planteamos a la jungla de ifs y que era
nuestra primera solución.

La diferencia entre una función y la otra es abismal porque la solución con *args permite
hacer todas las preguntas que queramos sobre el DataFrame sin necesidad de implementar
flags y código.

De hecho, si mi jefe me pide ahora una muestra del df, la solución con los *args
funcionaría sin el menor cambio y la solución con los ifs necesitaría algo más de trabajo.

```python
versatile_func(df, "tail", "describe", "sample")
```

Así que recuerden: los *args permiten suministrar cualquier número de paramétros
posicionales a una función y posteriormente Python lo volcará todo esto en una tupla.

En nuestro caso, los *args son strings y corresponden con el nombre los diferentes 
métodos de un pandas DataFrame.

Al estar en una tupla, yo puedo iterar sobre ella y ejecutarlos dinámicamente.
 
---

Pues bien, nuestra solución actual con los *args tiene un gran defecto y es que no
permite suministrarle ningún paramétro adicional.

De alguna manera sólo puedo ejecutar los métodos con los parametros que vienen por default.

Dicho de otra manera, si mi jefe me pide ahora mismo los 10 primeros registros, 
es decír un head(n=10), ninguna de las dos soluciones funcionaría.

Y para solucionar este problema, vamos a usar los **kwargs de Python.

Los **kwargs como ya hemos dicho, cuando aparecen dentro de la definición de una función
en Python habilitan a que le podamos pasar todos los keyword arguments que queramos a 
una función.

Un paramétro es keyword en Python, cuando al invocar una función, suministramos el paramétro
por su nombre. El interprete de Python cogerá todos estos valores y los meterá en un
diccionario que nosotros podemos iterar y mover de un lado a otro.

En este diccionario, las llaves o las keys serán el nombre del paramétro como texto y 
el value del diccionario será el valor del parámetro que le pasé.

---

¿Que cambios podemos hacer en nuestro código para que acepte keyword arguments?

Pues el cambio va a ser muy fácil porque únicamente tendremos que venir aquí y decir: acepta
**kwargs y cuando llega el momento de ejecutar el código, también acepta todos estos
kwargs.

```python

def versatile_func(df, *args, **kwargs):

    print(args, type(args), len(args))
    print(kwargs, type(kwargs), len(kwargs))

    for arg in args:
        if hasattr(df, arg):
            print(f"El {arg} del df es:")
            func = getattr(df, arg)
            print(func(**kwargs))

```

Hacer este cambio ahora me habilita lo siguiente, desde un único sitio poder contestarle
a todas las dudas que tiene mi jefe.

Fijaos aquí que si me pide las primeras 10 canciones de hoy, yo se lo puedo suministrar
y si me pide la correlación de pearson de este dataset de los valores numéricos también
se lo puedo dar.

En estos casos, df corresponde con el primer paramétros de mi versatile_func, "corr" corresponde
a los *args porque no lo suministro por el nombre.

Y por último method y numeric_only only, serán dos **kwargs porque los llamo por su nombre.

```python

versatile_func(df, "head", n=10)
versatile_func(df, "describe", "head", "sample")
versatile_func(df, "sample", n=3)
versatile_func(df, "corr", method="pearson", numeric_only = True)

```

Evidentemente, si yo intento implementar esta lógica en la solución con los ifs esto va 
a ser muy díficil y quedará una función muy muy larga. Así que mejor ni intentarlo.

---

Ahora bien, hay un tema muy importante aquí y es el siguiente.

Fijaos que tal y como tengo definido ahora mismo mi solución, sólo puedo invocar
un arg o método a la vez.

Si intento hacer esto obtendré un error:

```python
versatile_func(df, "head", "corr", n=10, method="pearson", numeric_only = True)
```

El error me dice que el método head de pandas no tiene ningún paramétro que sea method y
si miramos la documentación, efectivamente vemos que sólo acepta 1 paramétro, y es la
`n` o el número de filas.

Pues bien, esto podría ser un tema menor y realmente podrías quedarnos con la solución
actual e ir invocando la función varias veces con diferentes paramétros y ser felices.

Pero no es la forma como lo hacemos aquí. Aquí queremos ir un paso más adelante y 
profundizar en las cosas que tiene Python.

¿Se os ocurre una forma de cambiar el código de esta función para solventar este error?

Os animo a que pongan en pausa durante unos minutos este vídeo y piensen en una solución.

---

Han pasado ya varios minutos y vamos a relevar una posible implementación.

Para que este error no ocurra, debemos, antes de suministrar los **kwargs en la ejecución
de una función, comprobar que esta función los acepta.

Y la forma más fácil de hacerlo es usar el módulo de inspect de Python.

```python

def versatile_func(df, *args, **kwargs):

    print(args, type(args), len(args))
    print(kwargs, type(kwargs), len(kwargs))

    for arg in args:
        if hasattr(df, arg):
            print(f"El {arg} del df es:")

            func = getattr(df, arg)

            signature = inspect.signature(func)
            params = {
                name: value
                for name, value in kwargs.items()
                if name in signature.parameters
            }

            print(f"Los params aceptados por la función son: {params}.")

            print(func(**params))

```

Con inspect podemos, antes de ejecutar una función checkear para cada uno de nuestros
kwargs si la función acepta estos paramétros.

De esta manera, podemos al vuelvo construir un nuevo diccionario llamado params y 
utilizarlo como **kwargs en nuestra ejecución.

De esta manera, ahora tengo realmente 1 única función, muy flexible y versátil para poder
contestar a todas las preguntas de mi jefe de una manera rápida y eficiente.

```python

versatile_func(df, "head", "corr", n=10, method="pearson", numeric_only=True)

```

---
Antes de marchar, eso sí, tengo que hacer un comentario relevante. 

Las funciones que acepta los *args y los **kwargs son muy versátiles y pueden ser
extremadamente útiles en muchos contextos.

Pero un gran poder conlleva una gran responsabilidad y no se deben abusar de ellas.

Ante todo intenten seguir estos consejos:
1. No hay que sobrecomplicar las cosas. En la medida de lo posible debemos intentar
    implementar una solución fácil y sencilla.
2. Tenemos que vigilar que nuestra función se convierta en una "god-function": una función
    que hace demasiadas cosas en demasiados sitios de nuestro proyecto.
3. Si vemos que nuestro código empieza a hacer demasiadas cosas, 
    siempre es mejor simplifcarlo y partirlo en diferentes métodos o funciones más pequeñas.

    Vuestro yo del futuro os lo agradecerá.

---

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

