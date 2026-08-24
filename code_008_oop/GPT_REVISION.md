# Guion revisado --- Programación Orientada a Objetos en Python

------------------------------------------------------------------------

Hola amigos, ¿qué tal todo?

Bienvenidos a un nuevo vídeo.

En el vídeo de hoy vamos a hablar sobre Programación Orientada a
Objetos, en adelante POO.

La Programación Orientada a Objetos es un tema muy amplio que podríamos
estar explicando durante muchos meses. Sin embargo, en este vídeo vamos
a enfocarlo desde un punto de vista muy práctico.

El objetivo que busco es muy sencillo: vamos a implementar nuestra
primera clase en Python desde cero.

Por tanto, si nunca antes has visto una clase de Python, este vídeo te
ayudará a aclarar muchos conceptos.

Además, si trabajas en Data Science, Data Engineering o bien Data
Analytics, el ejemplo que voy a enseñar será muy útil porque usaremos
como punto de partida un Transformer de scikit-learn.

Para quienes no conozcan scikit-learn: es una librería muy utilizada en
Data Science y Machine Learning y ofrece muchas herramientas para
preprocesar datos y entrenar modelos de Inteligencia Artificial.

Empecemos.

------------------------------------------------------------------------

Primero de todo, para todas aquellas personas que nunca han escuchado
sobre clases u objetos o bien creen que es algo muy complicado: quiero
tranquilizaros y aseguraros que es mucho más fácil de lo que parece.

De hecho, si alguna vez habéis usado un `pandas.DataFrame` o
`StandardScaler` de scikit-learn, significa que ya habéis interactuado
con una clase de Python.

Como podemos ver aquí: si navegamos hasta `pandas.DataFrame`, veremos
que `DataFrame` es una clase y lo mismo ocurre con `StandardScaler`.

Por aquí de hecho podemos ver la palabra reservada class que nos indica
que es una clase de Python.

Nuestro gran objetivo en este vídeo será escribir una clase que tenga el
mismo comportamiento que el StandardScaler de `scikit-learn`.

------------------------------------------------------------------------

Para el resto del vídeo, yo voy a usar Jupyter Notebook porque el
resultado es mucho más visual que en la terminal.

Si tenéis cualquier dificultad, ponedlo en los comentarios y os
intentaré ayudar lo antes posible.

Dicho esto, vamos a importar el StandardScaler de scikit-learn y vamos a
importar pandas como pd.

------------------------------------------------------------------------

Primero de todo: ¿qué hace `StandardScaler`?

Veamos un ejemplo sencillo: aquí tenemos unos datos de prueba dentro de
un `pandas.DataFrame`. Un `DataFrame` no es más que una tabla con filas
y columnas.

Muchas veces cuando estamos trabajando con datos, necesitamos
estandarizar los datos.

Una de las operaciones más comunes que hacemos en este caso es restar la
media a un dataset y luego dividir entre la desviación típica.

Con scikit-learn y el StandardScaler, podemos conseguir esto de manera
muy fácil.

Primero vamos a instanciar el StandardScaler.

Cuando tenemos el scaler instanciado, podemos calcular cuál es la media
y la varianza de este dataset con el método `fit`.

Recordad que la desviación típica es la raíz cuadrada de la varianza,
así que podemos obtenerla a partir de la varianza cuando la necesitemos.

Después de haber llamado al método `fit(X)`, podemos preguntar a nuestro
scaler cuáles son los estadísticos que ha aprendido de este dataset.

Si hacemos scaler.mean\_ y scaler.var\_ podemos ver estos valores.

Ahora, si decido escalar mi dataset, puedo usar el método
`scaler.transform(X)` y de esta manera obtengo un dataset escalado.

Mirad como las columnas en el dataset X_scaler tienen un rango más
parecido.

Además, si aplicamos ahora X_scaler.describe() podemos ver como la media
del dataset resultante es cero y la desviación típica es 1.

Tras ver este ejemplo muy sencillo: podemos intuir que vamos a tener que
hacer 3 cosas:

1.  Implementar una clase que tenga un método `fit` donde se calculen la
    media y la varianza.
2.  Guardar la media y la varianza como atributos para poder
    recuperarlas y utilizarlas posteriormente en `transform`. De esta
    manera, cuando transformemos nuevos datos, utilizaremos exactamente
    los estadísticos aprendidos durante el `fit` y no volveremos a
    calcularlos. Además, es importante que el `fit` se haga únicamente
    con los datos de entrenamiento para evitar data leakage.
3.  Por último, implementar el método `transform` dentro de nuestra
    clase. Este método debe recibir un DataFrame de entrada y utilizar
    la media y la varianza calculadas en el paso 1 y guardadas en el
    paso 2 para escalar nuestro dataset.

Sé que acabo de mencionar muchas cosas nuevas como: métodos y atributos,
clase, fit, transform etc

Os pido que sigáis con el vídeo porque todo esto lo iremos aclarando a
lo largo de los próximos minutos.

Antes de implementarlo todo con clases de Python, vamos a hacerlo con
pandas para asegurarnos al 100% de que entendemos lo que debemos
escribir.

Este paso es opcional, pero nos ayudará mucho antes de entrar en la POO.

------------------------------------------------------------------------

Para hacer los pasos anteriores con pandas es muy sencillo:

1.  Primero guardamos en una variable mean\_ el resultado de X.mean() El
    método de DataFrame.mean() permite calcular la media de cada columna
    númerica en un DataFrame de pandas.
2.  Vamos a hacer los mismo con la varianza. Guardamos el resultado de
    X.var(ddof=0) en la variable var\_.
3.  Ahora que tenemos todo calculado, podemos replicar el cálculo que
    hace el StandardScaler. Fijamos que si hago: (X-mean\_)/(var\_ \*\*
    0.5) obtento exactamente el mismo resultado que con el
    StandardScaler. Tanto 1 dataframe como el otro son idénticos.

------------------------------------------------------------------------

Ahora vamos a implementar nuestro propio Transformer usando la
programación orientada a objetos.

Creo que va a ser muy fácil, porque sabemos la interfaz que tiene que
tener nuestra clase, usando el ejemplo de `StandardScaler`, y además
hemos implementado con pandas todo el código necesario. Así que solo nos
hace falta refactorizar y organizar ligeramente nuestro código.

Dicho lo anterior, para implementar una clase en Python empezamos por la
palabra reservada class seguida de un nombre y los dos puntos.

Nosotros aquí la vamos a llamar

    class MyCustomScaler:
        pass

Enhorabuena, acabas de implementar tu primera clase.

De hecho, nosotros ahora podemos instanciar un objeto de MyCustomScaler:

    my_scaler = MyCustomScaler()

El problema con nuestro código es que nuestra clase ahora mismo no sabe
hacer nada.

Para que MyCustomScaler sea útil, debo añadirle funcionalidades.

Y de hecho, una forma muy útil de ver las clases en el mundo de la
programación es que son "organizadores de código".

Es decir: la programación orientada a objetos ofrece una forma muy útil,
cómoda y ordenada de organizar nuestro código.

Podemos agrupar funcionalidades relacionadas con un ámbito en una única
clase.

Os pongo un ejemplo:

Pensemos por un momento en un reloj y sus posibles funcionalidades:

1.  Un reloj me debe saber dar la hora.
2.  Pero quizás una funcionalidad adicional que podría tener es calcular
    cuántas horas quedan hasta una hora determinada.
3.  También podría tener sentido añadir otra funcionalidad que consista
    en convertir una duración expresada en horas a microsegundos.
4.  Quizás un reloj me debe poder medir la hora en diferentes zonas
    temporales o diferentes ciudades.
5.  Y un largo etc.

Fijaos que de alguna manera podría implementar todas estas
funcionalidades en un objeto reloj porque dentro de mi aplicativo esto
tiene lógica y sentido.

Pues bien, dentro de la programación orientada a objetos, cuando
hablamos de añadir funcionalidades estamos hablando de añadir un método
o métodos a nuestra clase.

Dado que, en nuestro caso, queremos replicar `StandardScaler`, vamos a
añadir el método `fit`.

Hemos acordado que, en el método `fit`, vamos a calcular la media y la
varianza de nuestro dataset `X`.

Nosotros lo vamos a calcular y luego printear estos valores.

    class MyCustomScaler:

        def fit(self, X):
            mean_ = X.mean()
            var_ = X.var(ddof=0)

            print(mean_)
            print(var_)

            self.mean_ = mean_
            self.var_ = var_

            return self

Quiero llamar la atención a dos cosas:

1.  Un método de instancia es una función definida dentro de una clase
    de Python.

    Y cuando digo que es una función no estoy exagerando: mirad que
    usamos la misma palabra reservada "def" que se usa para definir
    funciones normales de Python.

    La diferencia es que, al definir esta función dentro de
    MyCustomScaler, fit pasa a formar parte de esa clase.

    Ahora, si quiero utilizar fit, sé que pertenece a MyCustomScaler. Es
    mucho más sencillo localizar dónde está implementada esa
    funcionalidad y entender cuál es su propósito.

    Además, una clase puede contener tantos métodos como necesitemos,
    cada uno encargado de una tarea concreta.

    Así que me permite organizar todo en función de las demandas de mi
    proyecto.

2.  Una segunda cosa muy importante es el primer parámetro dentro de
    nuestro método que es el `self`. El funcionamiento exacto
    de `self` lo vamos a ver al final del video, pero de momento quiero
    que os quedéis con que:

    1.  Casi siempre, un método en una clase llevará como primer
        parámetro self.
    2.  Este self sirve para identificar/referenciar a la instancia con
        la que estamos trabajando.

3.  Por último, una nueva cosa que quiero que sepáis es que los métodos
    normalmente representan acciones de nuestro código: calculamos algo,
    medimos algo, registramos algo en la base de datos, escalamos, etc.

    Es muy diferente a los atributos que veremos más adelante y que
    normalmente son valores "constantes" o bien valores que "determinan
    el comportamiento de nuestra instancia".

Ahora después de haber implementado esto, podemos poner a prueba nuestro
código y ver si vamos a poder calcular correctamente la media y la
varianza de nuestro dataset.

Lo hacemos y vemos que tenemos el print correcto.

Vamos a seguir.

Acordaos que dijimos que nuestra clase no sólo debe calcular la media y
la varianza de un dataset sino que también la debíamos guardar en algún
sitio.

En el ejemplo del StandardScaler, después de llamar el fit, podemos
preguntar al scaler cual es la media y la varianza escribiendo

    scaler.mean_
    scaler.var_

Fijaos en que, al escribir `scaler.mean_` o `scaler.var_`, no abrimos
paréntesis. Esto nos indica que estamos accediendo a atributos de la
instancia. Un atributo es un dato asociado a una instancia o a una
clase. En nuestro ejemplo, la media y la varianza son atributos de
`scaler`.

Podríamos tener otro scaler, aplicado a otro dataset, que tendría otra
media y otra varianza y, por tanto, sería diferente.

Si esto os resulta complicado, pensad en una Persona.

Una persona tiene un nombre y un apellido (atributos que representan
datos de esa persona) y, además, puede saber andar y hablar (acciones
que puede realizar y que podemos representar mediante métodos).

El scaler calcula estos valores internamente durante el `fit`, los
guarda en atributos de la instancia y, cuando le pregunto cuál es la
media o la varianza, puedo acceder directamente a esos atributos.

Evidentemente, lo del cajón es una metáfora. Lo importante es entender
que debemos guardar estos valores en algún lugar de la instancia.

Dentro de nuestro método fit, ya hemos calculado esto valores así que
ahora lo único que nos falta en guardarlos y para guardarlos lo que voy
a hacer es lo siguiente:

    self.mean_ = mean_
    self.var_ = var_

Con estas dos líneas, guardamos estos valores, si ahora ejecutamos de
nuevo nuestro código, podemos preguntar a nuestro my_scaler cual es la
media y la varianza.

Ahora vemos que tenemos un output muy parecido al StandardScaler de
scikit-learn.

Poco a poco nos estamos acercando a nuestro objetivo final.

En el caso de los estimadores de scikit-learn, `fit` normalmente
devuelve `self`, es decir, la propia instancia. Esto permite, entre
otras cosas, encadenar llamadas como veremos a continuación.

Este `return self` permite encadenar métodos en Python. Por ejemplo, más
adelante podremos hacer que `fit` devuelva la propia instancia y, a
continuación, llamar a `transform`.

Además, devolver `self` en `fit` forma parte de la convención habitual
de los estimadores de scikit-learn.

En vuestro código y proyecto, los métodos pueden devolver otra cosa o no
devolver nada, dependiendo de su propósito.

Esto ya dependerá de las necesidades de vuestro proyecto.

Y fijaos en que vuelve a aparecer `self`. Al final del vídeo vamos a
entender exactamente qué significa, pero de momento vamos a utilizarlo
así.

A continuación lo que vamos a añadir es un segundo método que se llamará
transform.

Este método debe recibir un dataframe y reutilizar los valores de antes
para estandarizar nuestro dataset.

        def transform(self, X):
            Xt = (X - self.mean_)/(self.var_ ** 0.5)
            return Xt

Con esta implementación, ahora podemos enviar un `pandas.DataFrame` y
estandarizar los datos.

Fijaos en las líneas `self.mean_` y `self.var_`: aquí recuperamos los
valores que aprendimos durante `fit` y los utilizamos para escalar
nuestro dataset.

Con esto ahora tenemos una clase ya plenamente funcional que tiene sus
atributos (mean\_ y var\_) y tiene sus métodos (fit y transform).

------------------------------------------------------------------------

Vamos ahora a explicar un par de conceptos adicionales que son muy
relevantes en OOP.

Primera cosa: tenemos estos dos prints que constantemente escriben algo
en la consola.

Quizás esto nos interesa durante el desarrollo de nuestro modelo, pero
no en producción.

Por supuesto, podríamos añadir un parámetro `verbose` dentro de `fit`,
pero vamos a aprovechar para explicar `__init__` y guardar esta
configuración en la instancia.

Existe un método muy especial en Python que se ejecuta al inicializar
una instancia de una clase y se llama `__init__`.

En Python, `__init__` se utiliza para inicializar la instancia. Puede
recibir parámetros que determinan su estado o configuración inicial.

En nuestro caso, el valor que va a recibir nuestro constructor es el
parámetro verbose que determinará si se deben o no printear los valores
de antes.

Para definir `__init__` es muy fácil: escribimos dos guiones bajos antes
y después de `init`. Los métodos y atributos con este patrón se conocen
habitualmente como *dunder*, abreviatura de *double underscore*.

Quitando estas excentricidades, todo lo demás es como una función o
método normal de Python: lleva el self y los demás parámetros.

Dado que quizás tendré que consultar más adelante el valor de `verbose`,
debo guardarlo en algún sitio. ¿Os suena esto? Es el cajón que hemos
definido antes. Por este motivo, lo guardo en:

        self.verbose = verbose

De esta manera, si ahora cambio ligeramente el código, puedo incorporar
este `verbose`.

    class MyCustomScaler:

        def __init__(self, verbose=False):
            self.verbose = verbose

        def fit(self, X):
            mean_ = X.mean()
            var_ = X.var(ddof=0)

            if self.verbose:
                print(mean_)
                print(var_)

Ahora puedo tener dos scalers, uno con `verbose=True` y otro con
`verbose=False`, y este atributo determina el comportamiento de cada
instancia.

------------------------------------------------------------------------

Otra cosa muy relevante que debéis saber de la programación orientada a
objetos es el concepto de herencia.

Uno de los puntos fuertes de la POO es la reutilización de código entre
clases.

Básicamente, puedo definir funcionalidades en una clase y reutilizarlas
en otras clases mediante la herencia.

Veamos a que me estoy refiriendo.

Si volvemos un minuto a nuestro StandardScaler, podemos ver que tiene
otro método llamado `fit_transform` que básicamente invoca el fit y
luego el transform.

Pues bien, nosotros podríamos definir un método idéntico como sigue:

        def fit_transform(self, X):

            Xt = self.fit(X=X).transform(X=X)

            return Xt

Ahora bien, pensad un segundo, si yo voy a tener que definir otras
clases parecidas a estas, no tiene mucho sentido tener que definit el
fit_transform en todas ellas.

Tendría mucho más sentido tener un único método que invoque a estos dos
y que podamos reutilizarlo.

Pues resulta que podemos hacer esto a continuación con una mini clase.

Os adelanto que vamos a descartar esta clase más adelante, pero para
entender inicialmente el funcionamiento de la herencia nos vendrá muy
bien.

    class MyTransformerMixin():

        
        def fit_transform(self, X):
            print("Hello from TransformerMixin")
            Xt = self.fit(X=X).transform(X=X)

            return Xt

Fijaos como hemos llevaod el fit_transform a otra clase llamada
MyTransformMixin.

Ahora podemos incorporar este método a nuestro scaler de una manera muy
sencilla. Después del nombre de la clase, abrimos paréntesis y añadimos
nuestra clase anterior.

Con este pequeño cambio, hemos conseguido una cosa muy relevante,
incorporar el fit_transform a nuestro scaler sin necesidad de definirlo
dentro de la clase.

Fijaos que si ahora vuelvo a crear una instancia, tengo disponible un
nuevo método.

He heredado un método de MyTransformerMixin y lo tengo dentro de
MyCustomScaler.

Si luego tengo otro scaler, podría hacer lo mismo y me estaría ahorrando
un montón de código.

Pero como os decía, este ejemplo sirve para explicar el concepto.

Ahora lo que vamos a hacer es reutilizar un montón de cosas directamente
de la librería de scikit-learn.

Vamos a importar `TransformerMixin` y `BaseEstimator`, y veréis cómo
podemos reutilizar capacidades ya definidas por scikit-learn dentro de
nuestro proyecto.

En nuestro caso, añadiendo esto dentro de MyCustomScaler, fijaos ahora
como la representación visual de mi instancia ha cambiado (esto es
gracias a BaseEstimator) y también tengo ahora el método de
fit_transform gracias a TransformerMixin.

Todo esto sin escribir ni una línea adicional de código y gracias a la
herencia de la POO.

------------------------------------------------------------------------

Vamos a explicar ahora, por último, el parámetro `self`.

`self` es una referencia a la instancia con la que estamos trabajando.
Dado que podemos tener muchos scalers, con diferentes valores de
`verbose` y aplicados a diferentes datasets, cada instancia necesita
mantener sus propios atributos.

Pues el parámetro self le ayuda en esta organización.

Pero en realidad hay otra forma mucho más sencilla de entender `self`.

Fijaos en que `self` aparece como primer parámetro de cada método de
instancia. Esto no significa que el método tenga obligatoriamente dos
parámetros: por ejemplo, un método `reset(self)` solo tiene un parámetro
explícito.

¿Qué pasa si le intento suministrar dos parámetros?

Dependiendo de cómo hagamos la llamada, Python puede mostrarnos un error
indicando que se han recibido más argumentos de los esperados. La clave
está en entender que la instancia se pasa automáticamente como primer
argumento.

¿Que ocurre aquí?

Cuando hago `my_scaler.fit(X=X)`, conceptualmente podemos verlo como una
llamada equivalente a:

    MyCustomScaler.fit(my_scaler, X)

¿Que hace aquí el Python?

Python busca la implementación de `fit` en la clase y le pasa
automáticamente la instancia como primer argumento.

¿Y por qué puede hacer esto Python? Porque las distintas instancias de
una misma clase comparten la definición de sus métodos.

Lo que diferencia principalmente a una instancia de otra son los datos
que tiene asociados, es decir, sus atributos.

El ejemplo que siempre pongo es el de una persona: si en tu programa
tienes una clase `Persona` que sabe andar y hablar, las distintas
instancias comparten la definición de esos métodos. Cada persona tendrá
sus propios atributos, como su nombre, mientras que los métodos están
definidos en la clase.

Así, cada instancia mantiene sus propios datos y Python puede utilizar
la implementación de los métodos definida en la clase.

------------------------------------------------------------------------

Hagamos ahora un breve recap:

1.  Una clase en Python empieza por la palabra reservada class.
2.  Los métodos de instancia son funciones definidas dentro de una clase
    y reciben normalmente la instancia como primer parámetro, que por
    convención llamamos `self`. Los métodos suelen representar acciones
    que puede realizar la clase. Una persona puede andar.
3.  Los atributos son datos asociados a una instancia o a una clase y
    representan su estado o configuración. Una persona puede tener un
    nombre y un DNI.
4.  La herencia en POO es un patrón muy potente para reutilizar y
    extender código entre clases.
5.  Cuando llamamos a un método de instancia mediante un objeto, Python
    pasa automáticamente esa instancia como primer argumento.

------------------------------------------------------------------------

Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de
suscribirse y darle al like. Esto me ayuda mucho al canal.

Si conocéis a alguien a quien le pueda resultar útil este vídeo,
compartidlo con esa persona.

Y si os queda alguna duda o tenéis alguna sugerencia, dejad un
comentario e intentaré responderlo cuanto antes.

Cuidaros mucho y nos vemos pronto.

Ciao.
