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
scikit-learn` significa que ya habéis interactuado con una clase de Python de manera
satisfactoria.

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
   llamadas.
1. Implementar un método de transform dentro de nuestra clase que acepte un dataframe
   de entrada y que utilice la media y la varianza calculada en el paso 1 para escalar
   nuestro dataset de tal manera que la media y la desviación típica del dataset 
   resultante sea 0 y 1 respectivamente.

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

----
Esto es todo por hoy. Si os ha gustado el vídeo no os olvidéis de suscribirse y darle
al like. Esto me ayuda mucho al canal.

Si conocen a alguien que puede encontrar útil este video, compartidlo con ellos.

Y si os queda alguna duda o sugerencia, poned un comentario y yo intentaré contestarlo
cuanto antes.

Cuidaros y nos vemos pronto.

Chao.

