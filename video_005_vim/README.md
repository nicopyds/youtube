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

`Vim` es un editor de texto multimodal de la terminal. 

Sus raíces se remotan a 1971 con la creación por parte de Ken Thompson 
(por cierto: el co-creador de Unix) del editor de texto `ed`.

Posteriormente en 1976, Bill Joy creó `vi` basándose en el código de Ken Thompson.

Tenemos que hacer un salto de más de 15 años, hasta que en 1992 cuando Bram Moolenaar 
publicó `Vim`: un acrónimo de vi improved.

La última incorporación a la familia de `Vim` es `Neovim`, un fork de `Vim` pero con
algunos cambios relevantes como sustitución de VimScript por Lua, un look mucho más 
moderno entre otros. 

Actualmente `NeoVim` tiene casi a 100k estrellas en GitHub haciendolo uno de los 
proyectos más populares en la plataforma.

Como podéis apreciar, `Vim`, después de 50 años, no sólo sigue vivo sino que cuenta 
con una comunidad muy entusiasta de usuarios y muchas contribuciones y mejoras constantes.

Para que vean el amor que sienten los usuarios de `Vim` hacia el editor, 
en el Developer Survey de StackOverflow de 2025, `Vim` y `Neovim` aparecen como los 
editores de texto más utilizados hoy en día.

En la sección de los editores de texto/IDES más admirados, `Neovim` se lleva el primer 
puesto con mucha diferencia.

----

¿Que es lo que hace que `Vim` sea tan especial?

Os expondré los principales motivos:
1. Vim es ubicuo. 
1. Vim es rápido.
1. Vim te hace sentir guay. 

El primer motivo para mi es el más relevante y es el que me llevó a aprender `Vim`.

Yo trabajo en una empresa muy regulada y con altos estandares de seguridad.

Por este motivo, tengo prohibido la instalación de software externo. Esto hace que tengo
que utilizar aquellas herramientas que se me proporcionan de partida. El proceso de 
homologación de software suele ser muy lento y la mayoría acaban en un `no` por parte del
equipo de seguridad.

Además, a esto se suma que tengo que trabajar en diferentes entornos: máquina de Windows 
en local, servidor OnPremise que corre Linux y tamibén en 2 entornos diferentes en 
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

La curva de aprendizaje puede llegar a ser bastante pronunciada pero creo que a la larga
es una inversión que vale la pena hacer.

Una cosa que yo tuve que cambiar nada más empezar es aprender a escribir con las dos manos.

Cuando usas Vim, casi no usas el ratón, toda la navegación y toda la edición se hace
a través atajos y las teclas del teclado. Para algunos esto puede ser un rollo, a mi 
en cambio esto me encanta.

Ahora bien, para ser eficiente, debes escribir correctamente y aquí tuve que "reeducar"
mi forma de usar el teclado.

Un cosa que me ayudó mucho es la página web de https://www.edclub.com/sportal/ que tiene
un montón de cursos de mecanografía tanto en inglés como en español.

Además, el diseño de los cursos es muy intuivo y visual: engancha enseguida y se hace
muy liviano seguir los tutoriales.

Yo no obstante, no llegué a completar todo el curso pero tampoco hace falta, en cuanto 
empiezas a notar que escribes correctamente, usando los diez dedos y te sientes 
cómodo puedes parar el curso de mecanografía.

Posteriormente, usé los siguientes recursos para aprender:
1. El libro de `Practical Vim`.
2. El tutorial oficial de `Vim` que se puede activar con el comando de:
3. Y los siguientes tutoriales online:
    - https://www.youtube.com/watch?v=XA2WjJbmmoM
    - https://www.youtube.com/watch?v=wlR5gYd6um0
    - https://www.youtube.com/watch?v=_NUO4JEtkDw

Con estos recursos y trás un mes y pico de práctica, `Vim` poco a poco empezaba a ser 
una herramienta que 

----

Soy mega fan de aprender los atajos en todas las herramientas que uso porque hace que 
llegues a ser mucho más rápido y productivo.

Si no queda claro que quiere decir `multimodal`, esperad hasta que lleguemos a la 
sección de ejemplos y lo veréis mucho más claro.

----


Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribiros y darle
al like. Esto me ayuda mucho a crecer el canal.

Si creen que hay alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

----

https://survey.stackoverflow.co/2025/technology#most-popular-technologies-dev-envs-dev-envs-prof
