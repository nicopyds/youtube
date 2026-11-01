----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo vídeo.

En el vídeo de hoy vamos a hablar sobre herramientas que nos ayudan a mejorar
nuestro código de manera fácil y rápida.

Vamos a ver 5 herramientas, cada una sirve para un propósito bien diferenciado y lo mejor 
de todo: estas tools son complementarias. 

Así que si las aplicas, el resultado final será un repo mucho mejor.

Empecemos.

----

La primera herramienta se llama `isort` y su propósito es ordenar correctamente los
imports de tus ficheros de Python. 

La forma de usarlo es muy fácil, lo primero que debes hacer es instalar esta herramienta.

Yo voy a usar la línea de comandos, así que teniendo un entorno virtual activado en Python
lo que voy a hacer es `pip install isort`.

Después de la instalación, tendré el comando de isort disponible.

Con isort, podemos apuntar a un fichero o un carpeta directamente y la herramienta
va a arreglar los imports que tenemos de acuerdo con PEP8.

Podemos mirar ahora nuestro fichero y ver que los imports han cambiado: primero vienen 
los imports de las librerías nativas de Python, luego van los imports de los paquetes 
que hemos instalado como pandas y numpy y por último irían los imports de nuestra 
propia aplicación.

Una cosa curiosa es que los imports del estilo, `from paquete import class` como lo
que hacemos con numpy, van después de los imports de toda la librería como 
`import pandas as pd`.

Así que esto es `isort` un mini herramienta para ordenar los imports.

Vamos a por la siguiente.

----

La segunda herramienta que podemos añadir a nuestro proyecto es `black`.

La instalación es idéntica a `isort` hacemos un pip install `black` y tenemos disponible
`black` vía la línea de comandos.

El propósito de `black` es formatear nuestro código de acuerdo, otra vez, con PEP8.

Ya veís que PEP8 es quizás el más influyente dentro de la comunidad de Python. 

No me voy a detener en explicar todos los consensos que hay alrededor de como hay que
formatear el código en Python, sólo te diré que si instalas y empiezas a usar `black`
la legitibilidad de tu código va a mejorar bastante. 

Otro beneficio de usar `black` es que ya no habrá peleas entre los diferentes miembros 
del equipo, porque como todos formatearán el código de la misma manera, todos lo verán
de la misma manera.

Si miramos nuestro fichero, un ojo no entrenado quizás no verá nada, pero es código 
haría sangrar a cualquier senior y OJO: el código es 100% funcional, es nunca mejor dicho
una cuestión de estilos.

Aplicamos `black` y fijaos la diferencia, se han quitando los espacios innecesarios, 
se respeta la separación de 80 carácteres por fila etc.

Nuestro código sigue funcionando como antes, pero ha mejora su legitibilidad.

Un pequeño truco aquí es: que si hay algo que no queremos que formateé `black` lo podemos
envolver alrededor de los siguientes comentarios:

```python

#fmt: off

def func(): pass

#fmt: on

```

Black verá #fmt: off y desactivará el formateo de código hasta encontrar la línea 
que contenga # fmt: on.

Por supuesto, también se pueden cambiar las reglas y el comportamiento de black con
un fichero `pyprojecto.toml` o `setup.cfg`: aunque a mi las reglas que ya vienen por
defecto me gustan bastante.

Instala `black` y empieza a usarlo hoy en tus proyectos.

----

La siguiente herramienta es `ruff` y al contrario que las otras dos, está escrita en
`Rust` y no `Python`.

Esto hace de `ruff` una herramienta extremadamente rápida.

`ruff` viene a ser un linter (es decir, hace análisis estático de código) pero también
es capaz de formatear código. 

De hecho, `ruff` ofrece compatibilidad casi al 100% de `isort` y de `black`: por tanto
si quieres una herramienta todo en 1, usa ruff.

Ahora bien, como nos puede ayudar `ruff`: básicamente si hacemos `ruff check` un fichero
o directorio, `ruff analizará todos nuestros ficheros` y nos dirá determinados fallos
que se va encontrando.

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarla
cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.

