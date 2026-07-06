----
Hola amigos, ¿que tal todo?

Bienvenidos a un nuevo video.

En el vídeo de hoy vamos a hablar sobre Programación Orientada a Objetos: en adelante
OOP.

La Programación Orientada a Objetos es un tema muy largo que podríamos estar discutiendo
durante muchos meses, en cambio en este vídeo lo vamos a enfocar desde una óptica muy
práctica.

El objetivo que busco es: enseñar e implementar nuestra primera clase en Python desde 
cero.

Por tanto, si nunca has visto una clase de Python antes, este vídeo te podrá ayudar a
esclarecer algunos conceptos.

Además, si trabajas en Data Science, Data Engineering o bien Data Analytics: el ejemplo
que voy a enseñar será muy útil porque usaremos como punto de partida un Transformer de
scikit-learn (scikit-learn es una librería muy utilizada dentro del mundo de los datos).

Empecemos.

----
Primero de todo, para todas aquellas personas que nunca han escuchado sobre clases u 
objetos o bien que creen que es algo muy complicado: quiero tranquilizaros y 
aseguraros que es mucho más fácil de lo que parece.

De hecho, si alguna vez habéis usado un `pandas DataFrame` o bien `StandardScaler de 
scikit-learn` significa que ya habéis interactuado con una clase de Python.

De hecho, muchas veces cuando usamos librerías externas de Python aprendemos a utilizar
las clases que nos proporcionan.

Como podemos ver aquí: si navegamos hasta pandas DataFrame es una clase y lo mismo
ocurre con StandardScaler.

Nuestro objetivo en este vídeo será escribir una clase que haga el mismo comportamiento
que el StandardScaler de `scikit-learn`.

Es decir: learning by doing.

----
Para el resto del vídeo, yo voy a usar el entorno de trabajo de Jupyter Notebook.

Si no tienes un entorno virtual de trabajo de Python creado, te dejaré un enlace a un 
notebook de Kaggle donde de manera gratuita y sin necesidad de instalar nada, vas a 
poder seguir con este ejemplo.

Dicho esto, vamos a importar el StandardScaler de scikit-learn y vamos a importar pandas
como pd.

----
Primero de todo: que hace el StandardScaler. 

Veamos con un ejemplo sencillo: aquí tenemos unos datos dummy dentro de un pandas 
DataFrame.

Muchas veces cuando estamos trabajando con datos, necesitamos escalar los datos.

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

Mirad como las columnas en el dataset X_scaler tienen un rango más similar.

Además, si aplicamos ahora X_scaler.describe() podemos ver como la media del dataset
resultante es cero y la desviación típica es 1.

Tras ver este ejemplo muy sencillo: podemos intuir que vamos a tener que hacer 3 cosas: 
1. Implementar una clase que tenga el método de fit donde se calcula la media y la 
   varianza.
1. Guardar la media y la varianza para poder luego recuperar y usarla en la siguientes
   llamadas. Esto lo hacemos sobre todo para evitar Data Leakage. Pero este tema ya nos
   data para otro vídeo completo.
1. Implementar un método de transform dentro de nuestra clase. Este método debe recibir 
   dataframe de entrada y que utilice la media y la varianza calculada en el paso 
   1 para escalar nuestro dataset de tal manera que la media y la desviación típica del 
   dataset resultante sea 0 y 1 respectivamente.

Antes de implementarlo todo con clases de Python, vamos a hacerlo con pandas para 
asegurarnos del todo que entendemos el funcionamiento interno del StandardScaler.

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
el código necesario, así que de alguna manera sólo nos hace falta refactorizar y 
organizar ligeramente nuestro código.

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

Y de hecho, una forma muy útil de ver las clases son como "organizadores de código".

Es decir: la programación orientada a objetos ofrece una forma muy útil y cómoda de 
organizar nuestro código. 

Podemos agrupar funcionalidades relacionadas con un ámbito en un única clase.

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

Acordamos que hemos quedado, en que en el método fit, lo que vamos a hacer es calcular
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
1. Un método no es más que una función anclada/indentada a una clase de Python. 

   Y cuando digo que es una función no estoy exagerando: mirad que usamos la misma
   palabra reservada "def" que se usa para definir funciones normales de Python.

   Al añadir ahora este método a MyCustomScaler, MyCustomScaler es el dueño de el y
   lo que conseguimos es justamente organizar nuestro código. Ahora, si decido utilizar
   este método fit, puedo recurir a MyCustomScaler e invocar el fit. Sé en todo momento
   donde buscarla y que hace este código.
   Como os podéis imaginar, puedo añadir todos los métodos o funcionalidades que yo 
   quiero a esta clase.

2. 

----
Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

