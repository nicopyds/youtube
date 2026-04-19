Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

El vídeo de hoy va a ser el primero de una serie de 3 donde voy a comentaros diferentes
tecnologías y herramientas que incorporé en mi flujo de trabajo y que han aumentando 
mucho mi productividad en el último año y medio.

Hoy veremos una herramienta que vosotros podéis incorporar con mucha facilidad porque 
es muy sencilla. Únicamente a a requerir aprenderse unos atajos.

En el siguiente video veremos una que tiene una curva de aprendizaje más pronunciada y 
por último veremos una tecnologia muy potente pero también cambiante y que yo uso cada 
día.

Dado que veremos muchos atajos de teclado, voy a activar el `KeyCaster` 
así que a partir de ahora, deberían ver abajo a la izquierda todo lo que escribo en mi 
teclado.
Tened en cuenta que yo estoy en un Mac, pero estos mismos atajos están disponibles 
para Windows y Linux.

Empecemos.

La herramienta de hoy se llama `tmux` y es un gestor de ventanas muy potentes de la
terminal. Permite acomodar cualquier flujo de trabajo y navegar muy rápido entre 
diferentes ventanas.

Antes de ver el beneficio que ofrece tmux, es importante simular un flujo de trabajo
que muchos de vosotros podrían tener en vuestro día a día.

Supongamos que en mi flujo de trabajo yo necesito una sesión con el interpréte de
Python, pero a la vez necesito una ventana en la terminal para otras tareas.

Una posible solución es tener una única ventana e ir entrando y saliendo de Python, 
pero como os podéis imaginar no es muy cómodo ni rápido.

La otra opción es abrir varios terminales, cada uno para un propósito diferente.
Era la solución que usaba yo antes de descubrir tmux, es algo más cómodo que la 
anterior pero implica muchas veces usar el ratón para cambiar entre ventana y esto
puede realentizar tu trabajo.

¿Que solución ofrece para ello tmux? Vamos a verlo, pero antes debemos mencionar 3 
conceptos clave de tmux y estos son:
1. Sesiones.
2. Ventanas.
3. Panes o Paneles.

Cada uno de ellos permite organizar tu trabajo de una forma jerarquica.

Para crear una sesión llamada `main`` en `tmux` debemos escribir en la terminal el 
comando `tmux new -s main`.

Si nos fijamos abajo en la terminal, vemos esta ralla verde lo que significa que 
estamos dentro de `tmux`.

Para salir ahora de esta sesión, podemos usar el el comando `CNTRL + b d`.

La combinación de letas `CNTRL + b` en tmux se llama `PREFIX` o PRÉFIJO y es muy 
relevante porque la mayoría de los atajos y comandos del programa empiezan por esta 
combinación.
De aquí en adelante cuando me van a escuchar decir `PREFIX o PRÉFIJO` que sepan que 
me refiero a `CNTRL + b`.

Si ahora escribo en la terminal el comando, `tmux ls`, puedo ver todas y cada una de
las sesiones que tengo abiertas en `tmux`. En mi caso tengo 1, pero puedo tener todas
las que quiero.

Para volver a conectarse a una sesión de tmux, puedo utilizar el siguiente comando:
`tmux attach -t main`. 

Ahora vuelvo a estar dentro de una sesión de tmux y esta sesión tiene una única 
ventana. 

Si yo quiero abrir ahora otra ventana (pensad en ventana como área de trabajo), lo
hago con el comando `PREFIX + c`.

Ahora, como podemos ver abajo, tengo dos ventanas llamdas zsh. Este nombre no me dice
nada así que vamos a cambiarlo de nombre.

Para cambiar, puedo usar el comando `PREFIX + ,`, pongo el nombre que quiero y le doy
al enter.

Lo mismo ahora lo vamos a hacer con la otra ventana.

Para navegar entre diferentes ventanas, puedo usar el siguiente comando `PREFIX + n` o
`PREFIX + p`. n es next y p es previous por tanto puedo navegar hacía adelante o hacía
atrás.

Vamos a crear ahora otra ventana, `PREFIX + c`, le damos el nombre de servers y vamos
a aprovechar para introducit los panes de `tmux`.

Los panes permiten dividir una ventana en otras más pequeñas para organizar tu trabajo
en otras sub-áreas más pequeñas. Si quiero dividir una ventana verticalmente, lo puedo
hacer con el comando `PREFIX + %`.

Ahora mismo tengo 2 paneles iguales y voy a aprovecar para dividir este panel en otros
más pequeños. Para hacer la división horizontal, puedo utilizar el comando de 
`PREFIX + "`.

Para navegar ahora entre los paneles que tengo en 1 ventana, voy a utilizar el comando
`PREFIX + o` para navegar hacía adelante o `PREFIX + ;` para navegar hacia atrás.

Para que nadie se pierda, vamos a hacer una recapitulación: estamos dentro de una 
sesión de tmux llamda `main` donde tengo 3 ventanas llamadas: `python, vi y servers` y
en la ventana de servers tengo 3 paneles.








