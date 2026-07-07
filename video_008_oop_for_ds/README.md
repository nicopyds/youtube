----
Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre Programación Orientada a Objetos: en adelante
OOP.

La Programación Orientada a Objetos es un tema muy largo que podríamos estar discutiendo
durante muchos meses, en cambio en este vídeo lo vamos a enfocar desde un punto de vista
muy práctico.

El objetivo que busco es: enseñar e implementar nuestra primera clase en Python desde 
cero.

Por tanto, si nunca has visto una clase de Python antes, este vídeo te podrá ayudar a
esclarecer algunos conceptos.

Además, si trabajas en Data Science, Data Engineering o bien Data Analytics, el ejemplo
que voy a enseñar será muy útil porque usaremos como punto de partida un Transformer de
scikit-learn.

Para los que no conocen scikit-learn es una librería muy utilizada dentro del mundo de 
los datos.

Empecemos.

----
Primero de todo, para todas aquellas personas que nunca han escuchado sobre clases u 
objetos o bien que creen que es algo muy complicado: quiero tranquilizaros y 
aseguraros que es mucho más fácil de lo que parece.

De hecho, si alguna vez habéis usado un `pandas DataFrame` o bien `StandardScaler de 
scikit-learn` significa que ya habéis interactuado con una clase de Python.

Como podemos ver aquí: si navegamos hasta pandas DataFrame es una clase y lo mismo
ocurre con StandardScaler. Por aquí de hecho podemos ver la palabra reservada class que
nos indica que es una clase de Python.

Nuestro gran objetivo en este vídeo será escribir una clase tenga el mismos 
comportamiento que el StandardScaler de `scikit-learn`.

----
Para el resto del vídeo, yo voy a usar el entorno de trabajo de Jupyter Notebook porque
el output es mucho más visual que no en la terminal.

Si tienen cualquier dificultad, ponedlo en los comentarios y os intentaré ayudar lo antes
posible.

Dicho esto, vamos a importar el StandardScaler de scikit-learn y vamos a importar pandas
como pd.

----
Primero de todo: que hace el StandardScaler. 

Veamos con un ejemplo sencillo: aquí tenemos unos datos dummy dentro de un pandas 
DataFrame.

Muchas veces cuando estamos trabajando con datos, necesitamos estandarizar los datos.

Una de las operaciones más comunes que hacemos en este caso es restar la media a un 
dataset y luego dividir entre la desviación típica.

Con scikit-learn y el StandardScaler, podemos conseguir esto de manera muy fácil.

Primero vamos a instanciar el StandardScaler.

Cuando tenemos el scaler instanciado, podemos "calcular" cual es la media y la varianza
de este dataset con el método de fit.

Recuerden que la desviación típica es la raíz cuadrada de la varianza así que nos da lo 
mismo calcular una o la otra.

Después de haber llamado el método de fit(X), podemos ahora preguntar a nuestro scaler
cuales son los estadísticos de este dataset.

Si hacemos scaler.mean_ y scaler.var_ podemos ver estos valores.

Ahora, si yo decido escalar mi dataset, puedo usar el método scaler.transform(X) y de
esta manera obtengo un dataset escalado.

Mirad como las columnas en el dataset X_scaler tienen un rango más parecido.

Además, si aplicamos ahora X_scaler.describe() podemos ver como la media del dataset
resultante es cero y la desviación típica es 1.

Tras ver este ejemplo muy sencillo: podemos intuir que vamos a tener que hacer 3 cosas: 
1. Implementar una clase que tenga el método de fit donde se calcula la media y la 
   varianza.
1. Guardar la media y la varianza para poder luego recuperar y usarla en la siguientes
   llamadas. Esto lo hacemos sobre todo para evitar Data Leakage. Pero este tema lo 
   veremos en un víde futuro.
1. Implementar un método de transform dentro de nuestra clase. Este método debe recibir 
   dataframe de entrada y que utilice la media y la varianza calculada en el paso 
   1 y guardado en el paso 2 para escalar nuestro dataset de tal manera que la media 
   y la desviación típica del dataset resultante sea 0 y 1 respectivamente.

Antes de implementarlo todo con clases de Python, vamos a hacerlo con pandas para 
asegurarnos del todo que entendemos el funcionamiento interno del StandardScaler.

Este paso es opcional, pero nos ayudará mucho antes de entrar en la POO.

----
Para hacer los pasos de antes con pandas es muy sencillo:
1. Primero guardamos en una variable mean_ el resultado de X.mean()
   El método de DataFrame.mean() permite calcular la media de cada columna númerica en 
   un DataFrame de pandas.
1. Vamos a hacer los mismo con la varianza. Guardamos el resultado de X.var(ddof=0) en
   la variable var_.
1. Ahora que tenemos todo calculado, podemos replicar el cálculo que hace el 
   StandardScaler. Fijamos que si hago: (X-mean_)/(var_ ** 0.5) obtento exactamente el 
   mismo resultado que con el StandardScaler.
   Tanto 1 dataframe como el otro son idénticos.

----
Ahora vamos a implementar nuestro propio Transformer usando la programación orientada a
objetos.

Creo que va a ser muy fácil, porque sabemos la interfaz que tiene que tener nuestra 
clase (usando el ejemplo de StandardScaler) y además hemos implementado con pandas todo
el código necesario, así que sólo nos hace falta refactorizar y organizar ligeramente 
nuestro código.

Dicho lo anterior, para implementar una clase en Python empezamos por la palabra 
reservada class seguida de un nombre y los dos puntos.

Nosotros aquí la vamos a llamar 

```python
class MyCustomScaler:
    pass

```

Enhorabuena, acabas de implementar tu primera clase.

De hecho, nosotros ahora podemos instanciar un objeto de MyCustomScaler:

```python
my_scaler = MyCustomScaler()
```

El problema con nuestro código es que nuestra clase ahora mismo no sabe hacer nada.

Para que MyCustomScaler sea útil, debo añadirle funcionalidades.

Y de hecho, una forma muy útil de ver las clases son como "organizadores de código".

Es decir: la programación orientada a objetos ofrece una forma muy útil y cómoda de 
organizar nuestro código. 

Podemos agrupar funcionalidades relacionadas con un ámbito en un única clase.

Os pongo un ejemplo:

Pensemos por un momento en un reloj y sus posibles funcionalidades:
1. Un reloj me debe saber dar la hora.
2. Pero quizás una funcionalidad adicional que podría tener es descontar cuantas horas
   quedan hasta una hora determinada.
3. También podría tener sentido añadir otra funcionalidad que consiste en hacer 
   transformaciones de horas a microsegundos.
4. Y un largo etc.

Fijaos que de alguna manera podría organizar todas estas funcionalidades entorno a un
objeto reloj porque dentro de mi aplicativo esto tiene cierta lógica.

Pues bien, dentro de la programación orientada a objetos, cuando hablamos de añadir
funcionalidades estamos hablando de añadir un método a nuestra clase.

Dado que en nuestro caso, queremos replicar el StandardScaler vamos a añadir el método
de fit.

Acordamos que hemos quedado, que en el método fit, lo que vamos a hacer es calcular
la media y la varianza del nuestro dataset X.

Nosotros lo vamos a calcular y luego printear estos valores.

```python
class MyCustomScaler:
    def fit(self, X):
        mean_ = X.mean()
        var_ = X.var(ddof = 0)

        print(mean_)
        print(var_)

```

Quiero llamar la atención a dos cosas:
1. Un método no es más que una función definida dentro de una clase de Python. 

   Y cuando digo que es una función no estoy exagerando: mirad que usamos la misma
   palabra reservada "def" que se usa para definir funciones normales de Python.

   La diferencia es que, al definir esta función dentro de MyCustomScaler, 
   fit pasa a formar parte de esa clase.

   Ahora, si quiero utilizar fit, sé que pertenece a MyCustomScaler.
   Es mucho más sencillo localizar dónde está implementada esa funcionalidad y 
   entender cuál es su propósito.

   Además, una clase puede contener tantos métodos como necesitemos, 
   cada uno encargado de una tarea concreta.

2. Una segunda cosa muy importante es el primer parámetro dentro de nuestra función que
    es el `self`. El funcionamiento exacto de `self` lo vamos a ver al final del video, 
    pero de momento quiero que os quedéis con que:
    1. Casi siempre, un método en una clase llevará como primer parámetro self.
    2. Este self sirve para identificar/referenciar a la instancia con la que estamos 
        trabajando.

Ahora después de haber implementado esto, podemos poner a prueba nuestro código y ver
si vamos a poder calcular correctamente la media y la varianza de nuestro dataset.

Lo hacemos y vemos que tenemos el print correcto.

Vamos a seguir y acordaos que dijimos que nuestra clase no sólo debe calcular la media
y la varianza de un dataset sino que también la debíamos guardar en algún sitio.

En el ejemplo del StandardScaler, después de llamar el fit, podemos preguntar al scaler
cual es la media y la varianza escribiendo

```python
scaler.mean_
scaler.var_
```

Fijaos que al escribir, no abrir paréntesis. Esta diferencia sútil indica que estoy
delante de un atributo de la clase. Un atributo nos es más que un valor que define
el comportamiento de esta clase. En nuestro ejemplo: esta media y varianza son atributos
de scaler.

El scaler calculó estos atributos internamente en el fit, los ha guardado en un bolsillo 
y yo ahora cada vez que yo le pregunto cual es la media y la varianza, el scaler mete 
la mano el bolsillo y nos dice estos valores.

Evidentemente, uso el bolsillo como una metáfora lo importante es entender que debemos
guardar en algún lugar estos valores.

Dentro de nuestro método fit, ya hemos calculado esto valores así que ahora lo único que
nos falta en guardarlos y para guardarlos lo que voy a hacer el

```python
self.mean_ = mean_
self.var_ = var_
```

Con estas dos líneas, guardamos estos valores, si ahora ejecutamos de nuevo nuestro 
código, podemos preguntar a nuestro my_scaler cual es la media y la varianza.

Ahora vemos que tenemos un output muy parecido al StandardScaler de scikit-learn.

Poco a poco nos estamos acercando a nuestro objetivo final.

Una buena praxis en Python y en programación en general es que tus funciones tengan
un return. Nosotros aquí vamos a hacer un return de self.

Y fijaos que vuelve aparecer self otra vez y os prometo que al final del vídeo lo vamos
a desmitificar pero de momento lo hacemos a implenatar así.

Ojo, una nota muy importante, nosotros aquí devolvemos self porque queremos que
nuestra clase sea compatible con scikit-learn pero en vuestra clase o proyecto quizás
el return debe ser otra cosa. Aquí podéis devolver lo que toca y lo que se necesita.

No siempre el return debe ser self. En nuestro caso esto tiene sentido y es necesario.

A continuación lo que vamos a añadir es un segundo método que se llamará transform.

----
Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

