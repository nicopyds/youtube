----

Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

El vídeo de hoy va a ser una declaración de amor.

En concreto, una declaración de amor a `Vim`: el mejor editor de texto de la historia.

Este vídeo no pretender ser un tutorial ni tampoco una intro.

Tomandlo más bien como un vídeo de divulgación.

Mi idea es explicar que es `Vim`, los motivos que me han llevado a aprender `Vim` y 
también mostrar algunos ejemplos muy sencillos que os permitan a vosotros entender
su potencial y espero, despertar vuestra curiosidad hacia el editor.

Empecemos.

----

`Vim` es un editor de texto multimodal de la terminal. Permite manipular texto
con muchisima velocidad y agilidad.

Sus raíces se remotan a 1971 con la creación por parte de Ken Thompson 
(por cierto: el co-creador de Unix) del editor de texto `ed`.

Posteriormente en 1976, Bill Joy creó `vi` basándose en el código de Ken Thompson.

Tenemos que hacer un salto de más de 15 años, hasta que en 1992 Bram Moolenaar 
publicó `Vim`: un acrónimo de vi improved.

La última incorporación a la familia de `Vim` es `Neovim`, un fork de `Vim` pero con
algunos cambios relevantes como la sustitución de VimScript (un lenguaje de 
programación arcaico del propio `vim`) por Lua (un lenguaje scripting mucho versátil), 
un lavado de cara mucho más moderno entre otras cosas.

Actualmente `NeoVim` tiene casi a 100k estrellas en GitHub haciendolo uno de los 
proyectos más populares en la plataforma.

Como podéis apreciar, `Vim`, después de 50 años, no sólo sigue vivo sino que cuenta 
con una comunidad muy entusiasta de usuarios que hacen muchas contribuciones y se 
añaden mejoras constantes.

Para que vean el amor que sienten los usuarios de `Vim` hacia el editor, 
en el Developer Survey de StackOverflow de 2025, `Vim` y `Neovim` aparecen como los 
editores de texto más utilizados hoy en día.

En la sección de los editores de texto/IDES más admirados, `Neovim` se lleva el primer 
puesto con mucha diferencia.

https://survey.stackoverflow.co/2025/technology#most-popular-technologies-dev-envs-dev-envs-prof

----

¿Que es lo que hace que `Vim` sea tan especial?

Os expondré los principales motivos:
1. Vim es ubicuo. 
1. Vim es rápido.
1. Vim te hace sentir guay. Bromas aparte, `vim` te empuja a mejorar y aprender nuevas
cosas constantemente.

El primer motivo para mi es el más relevante y es el que me llevó a aprender `Vim`.

Yo trabajo en una empresa muy regulada y con altos estandares de seguridad.

Por este motivo, tengo prohibido la instalación de software externo. Esto hace que tengo
que utilizar aquellas herramientas que se me proporcionan de partida. El proceso de 
homologación de software suele ser muy lento y la mayoría acaban en un `no` por parte del
equipo de seguridad.

Además, a esto se suma que tengo que trabajar en diferentes entornos: máquina de Windows 
en local, servidor OnPremise que corre Linux y también en 2 entornos diferentes en 
Google Cloud.

El problema consiste que los entornos están muy fragmentados. En algunos entornos puedes 
llegar a tener una versión de VSCode con algunas extensiones y en otro otras. 

Quizás un día tienes que trabajar en el Cloud y otro día en Windows. Un día usas
Jupyter Notebooks, otro usas VSCode y otro día tienes que tirar de JupyterLab. Cada uno
tiene su forma de navegación, sus atajos, su filosofía.

Todo esto hace que la experiencia de desarrollo no sea del todo placentera porque en todo
momento tienes  que "readaptar" tu forma de trabajo.

Para mi esto suponía todo el rato "fricciones" innecesarias y me llevo a buscar 1 
editor de texto que esté presente en todos estos entornos. 

Me acuerdo de buscar en Google y me salieron dos opciones: `emacs` y `vim`.

Miré si tenía `emacs` instalado, no lo estaba (por suerte) y me quedé con `vim`.

Resulta ser, que `vim` es el editor de texto que viene con la mayoría de las distribuciones
de Linux dado que para ser POSIX-compliant, debes tener una versión de `vim` instalada.

POSIX: Portable Operating System Interface

Buuuuum, de golpe, todos los entornos de Linux pasan a ser homogéneos. Todo empieza a 
encajar.

Quedaba por resolver el problema de Windows y la verdad que allí tuve algo de suerte.

Tenía instalado `Gitbash` en Windows y este también viene con Vim.

Así, una vez encontrado el denominador común. Sólo faltaba aprender Vim. 

Y en la siguiente sección os contaré mi historia y como aprendí `Vim`.

----

Como os decía, `Vim` es ubicuo. Esta presente en la mayoría de los sistemas de Linux y 
en muchos casos es el editor de texto por defecto. 

Pero aprender `Vim` no es fácil, requiere tiempo y paciencia.

La curva de aprendizaje puede llegar a ser bastante pronunciada porque `vim` hace las 
cosas a su manera: the vim way.

Una cosa que yo tuve que cambiar nada más empezar es aprender a escribir con las dos manos.

Cuando usas Vim, casi no usas el ratón, toda la navegación y toda la edición se hace
a través atajos y las teclas del teclado. Para algunos esto puede ser un rollo, a mi 
en cambio esto me encanta.

# mirar esto bien
<Ahora bien, para ser eficiente, debes escribir correctamente y aquí tuve que "reeducar"
mi forma de usar el teclado. Lo que quiero decir con esto es usar los diez dedos, tener
escribir correctamente.>

Si el concepto de "fila guía o fila central" es algo nuevo para ti, lo más probable es 
que estas en la misma situación en la que yo me encontraba.

Un cosa que me ayudó mucho es la página web 
https://www.edclub.com/sportal/
que tiene un montón de cursos de mecanografía tanto en inglés como en español.

Además, el diseño de los cursos es muy intuivo y visual: engancha enseguida y se hace
muy liviano seguir los tutoriales.

Yo no llegué a completar todo el curso pero tampoco hace falta, en cuanto 
empiezas a notar que escribes más rápido, usas los diez dedos y te sientes cómodo, 
no necesitas mirar el teclado para buscar una tecla puedes parar el curso de mecanografía
y pasar a aprender `vim`.

Posteriormente, usé los siguientes recursos para aprender:
1. El libro de `Practical Vim`.
2. El tutorial oficial de `Vim` que se puede activar con el comando de: <vimtutor>
3. Y los siguientes tutoriales online:
    - https://www.youtube.com/watch?v=XA2WjJbmmoM
    - https://www.youtube.com/watch?v=wlR5gYd6um0
    - https://www.youtube.com/watch?v=_NUO4JEtkDw

Con estos recursos y tras casi 2 meses de práctica, `Vim` poco a poco empezaba a formar
parte de mi día a día.

----

¿Algunos se preguntarán si esto realmente vale la pena? 

Para mi la respuesta es que sí. Porque una vez que te manejas bien con `Vim` empiezas 
a ser muy rápido. Y aquí os quiero mostrar algunos ejemplos.

Lo primero mirad que estoy dentro de la terminal y puedo ejecutar `vim --version` y 
veis que tengo `vim` instalado. Como podéis observar yo voy a tirar de `Neovim` pero esto
mismo lo tienen para `vim`.

Para aquellos que están en Windows, os recomiendo que instalen `vim` desde la página 
oficial o bien `Gitbash` y usen `vim` desde la terminal del `Gitbash`.

Si yo ejecuto `vim` a secas entro dentro del programa de `vim` y puedo ver algunas 
opciones: como por ejemplo el manual de ayuda y otras cosas.

Para salir del programa debo escribir `:q`.

`Vim` sobre todo se usa para leer o editar ficheros de texto, por este motivo vamos a 
abrir un fichero y probar a editarlo.

Si escribo `vim <nombre_fichero>` puedo empezar a editarlo. En realidad, lo que voy a
editar es un fichero "temporal" con el contenido original. De esta manera, en cualquier
momento puedo sobreescribir el contenido o bien descartar los cambios.

Antes os había comentado que `vim` es un editor multimodal. Esto quiere decir que para
diferentes "tareas o flujos de trabajo" suele haber un modo especial optimizado para
esta tarea.

Si yo únicamente quiero leer el contenido de un texto, `vim` proporciona el modo "normal".

Esto quiere decir que yo ahora mismo puedo navegar por este fichero, me puedo desplazar
pero no lo puedo modificar. Para desplazarse uso la fila: "hjkl" para moverme hacía
izquierda, abajo, arriba o bien a la derecha.

Fijaos que la diferencia con respecto a `Word` o `Visual Studio Code` es relevante: el 
modo normal en `vim` es de lectura y en cambio en la inmensa mayoría de otros 
programas cuando abres un fichero inmediatamente lo puedes editar o insertar texto en 
él.

Esto tiene que ver con que los creadores de `vim` saben que la mayoría de las veces, 
lees un fichero mucho más a menudo que lo editas.

Si yo quiero salir ahora de este fichero, lo hago con `:q` o `:q!`.

Si ahora decido abrir el fichero puedo teclar `vim <nombre_fichero> +75` y voy a saltar
a la línea 75.

----

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribiros y darle
al like. Esto me ayuda mucho a crecer el canal.

Si creen que hay alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

----

