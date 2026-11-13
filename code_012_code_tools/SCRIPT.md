----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo vídeo.

En el vídeo de hoy vamos a hablar sobre herramientas que nos ayudan a mejorar
nuestro código de manera fácil y rápida.

Vamos a ver 4 herramientas, cada una sirve para un propósito concreto y lo mejor de 
todo: son complementarias, así que se pueden incorporar poco a poco en vuestros 
proyectos y cada una de ellas ayudará a mejorar el código y reducir los errores.

El caso que os traigo es un código funcional y que se puede ejecutar sin fallos.

No obstante, es un código que se puede mejorar.

Nosotros nos vamos a apoyar en estas tools externas para ir gradualmente refinando 
script y al final del video haremos una comparación del código inicial y el código final.

Ya os adelanto que quedará mucho mejor.

Empecemos.

----

La primera herramienta se llama `isort` y su propósito es muy sencillo: se trata de 
ordenar correctamente los imports de tus ficheros de Python. 

La forma de usarlo es muy fácil, lo primero que debes hacer es instalar la herramienta.

Se puede instalar una extensión en tu editor de código favorito, yo no obstante lo voy 
a usar desde la línea de comandos.

Así que tengo un entorno virtual de Python activado y lo que voy a hacer es `pip install isort`.

Por cierto, esto mismo aplica al resto de tools, así que asegúrate de instalarlas antes
de ejecutar los comandos que vas a ver en el tutorial.

Después de la instalación, tendré disponible el comando `isort` en la terminal. 

Con isort, podemos apuntar a un fichero o un carpeta directamente y la herramienta
va a arreglar los imports de nuestros ficheros de acuerdo con PEP8.

El PEP8 ya apareció en varios vídeos del canal así que es un viejo conocido.

Si os apetece indagar un poco más sobre el PEP8 os dejaré un enlace en la descripción 
del vídeo.

Puedo lanzar el comando isort main.py y la herramienta automáticamente cambiará los imports. 

Podemos mirar ahora nuestro fichero y ver que los imports han cambiado: primero vienen 
los imports de las librerías nativas de Python (como os o sys), luego van los imports 
de los paquetes que hemos instalado como pandas y numpy y por último irían los imports 
de nuestra propia aplicación.

Además, una cosa curiosa es que los imports del estilo, `from paquete import class` 
como lo que hacemos con numpy, van después de los imports de toda la librería como 
`import pandas as pd`.

Así que esto es `isort` un mini herramienta para ordenar los imports.

Vamos a por la siguiente.

----

La segunda herramienta que podemos añadir a nuestro proyecto es `black`.

La instalación es idéntica a `isort` hacemos un pip install `black` y tenemos disponible
`black` vía la línea de comandos.

El propósito de `black` es formatear nuestro código de acuerdo, otra vez, con PEP8.

No me voy a detener en explicar todos los consensos que hay alrededor de como hay que
formatear el código en Python, sólo te diré que si instalas y empiezas a usar `black`
la legitibilidad de tu código va a mejorar bastante. 

Otro beneficio de usar `black` es que ya no habrá peleas entre los diferentes miembros 
del equipo, porque como todos formatearán el código de la misma manera, todos verán el 
código igualde la misma manera.

Si miramos nuestro fichero, una persona no entrenada quizás no verá nada, pero es un 
código que haría sangrar los ojos a cualquier senior: el código es 100% funcional, 
pero es feo verlo.

Nunca mejor dicho que es una cuestión de estilos.

Aplicamos `black` y fijaos la diferencia, se han quitando los espacios innecesarios, 
se respeta la separación de 88 carácteres por fila etc.

Nuestro código sigue funcionando como antes, pero ha mejorado su legitibilidad.

Un pequeño truco aquí es: que si hay algo que no queremos que formatee `black` lo podemos
envolver alrededor de los siguientes comentarios:

```python

#fmt: off

def func(): pass

#fmt: on

```

Black verá #fmt: off y desactivará el formateo de código hasta encontrar la línea 
que contenga # fmt: on.

Por supuesto, también se pueden cambiar las reglas y el comportamiento de black con
un fichero `pyprojecto.toml` o `setup.cfg`: aunque a mi las reglas que vienen por
defecto me gustan bastante.

Instala `black` y empieza a usarlo hoy en tus proyectos.

----

La siguiente herramienta es `ruff` y al contrario que las otras dos, está escrita en
`Rust` y no `Python`.

Esto hace de `ruff` una herramienta extremadamente rápida. Y cuando digo que es 
extremadamente rápida quiero decir extremadamente rápida.

`ruff` viene a ser un linter es decir, es una herramienta que hace análisis estático 
de código y lo valida contra una serie de reglas para cazar errores y possibles 
inconsistencias en el código.

Estática quiere decir, que tu código no se llega a ejecutar, sino que únicamente se 
parsea y se analiza.

Otra cosa muy importante es que ruff, también ofrece la posibilidad de formatear el 
código, al igual que black.

De hecho, `ruff` ofrece compatibilidad casi al 100% de `isort` y de `black`: por tanto
si quieres una herramienta todo en 1, usa ruff.

Ahora bien, ¿como nos puede ayudar `ruff`?: básicamente si hacemos `ruff check` un fichero
o directorio, `ruff analizará todos nuestros ficheros` y nos dirá determinados fallos
que se va encontrando.

Cuando estamos conformes con los cambios, podemos hacer `ruff check --fix ./` y ruff
en cuestión de segundos nos aplicará los cambios.

Si quieres `ruff` para formatear, puedes usar el código de `ruff format ./`.

Una cosa muy relevante, las herramientas como black y ruff, cambian nuestros ficheros 
como había dicho antes, esto no afecta al resultado. El código seguiría dando el 
mismo resultado.

----

La siguiente herramienta que quiero contaros es `pylint` y es un paquete de Python que
al igual que ruff hace análisis estático de código, pero su análisis es más profundo e
implementa reglas diferentes a las de ruff. Así que se complementan de maravilla.

Puede encontrar código duplicados entre diferentes ficheros, detecta errores, hace check
si tenemos la documentación escrita y otra muchas cosas. Vamos, que es una auténtica 
maravilla.

Una cosa importante de pylint es que no cambia los ficheros, únicamente nos 
reporta las errores o incosistencias que encuentra. Así que es tarea del programador
entrar y modificar el código.

Veamos que nos reporta a nosotros. Vemos aquí varias mejoras y ahora las podemos 
arreglar rápido.

A nosotros nos sugiere que debemos añadir documentación al código y luego que tenemos
una variable en una función que es igual que una variable definida dentro del fichero y
que esto podría provocar una confusión en el futuro.

Aquí tengo dos opciones, o bien puedo cambiar el nombre de la variable o bien puedo
decirle a pylint que ignore este check.

```python
df = pd.DataFrame(data=dummy_data) # pylint: disable=redefined-outer-name
```

Esto lo puedo hacer con `# pylint: disable=redefined-outer-name`.

Tened en cuenta que esto es un arma de doble filo: puedo ignorar todo los warnings
que me salen de pylint y no me van a salir más errores, así que usad esta herramienta
con responsabilidad.

Os recomiendo mucho que no os agobiéis con la cantidad de errores y warnings que os 
pueda sugerir pylint, sobre todo en proyectos grandes.

Podéis empezar por un fichero, escalar a un módulo y posteriormente al proyecto entero.

Lo importante aquí es dejar el código mejor de lo que nos lo hemos encontrado y trabajar
poco a poco en mejorarlo.

Y nos nos engañemos, si pylint nos reporta que tenemos un código de 10, nos sentimos 
muy bien.

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarla
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

