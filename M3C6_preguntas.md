# M3C6 Python Assignment – Preguntas Teóricas

> ### 1. ¿Para qué usamos Clases en Python?

Lo primero que debemos conocer antes de mencionar los usos de las clases es que Python es un lenguaje que soporta la programación orientada a objetos, denominado **OOP** (en inglés '*Object-Oriented Programming*'), esto quiere decir que además de ser un lenguaje que incluye estructuras de datos (listas, colecciones, diccionrios, tuplas, etc) así como estructuras de control (condicionales, bucles, etc) también admite Programación Estructurada y la Programación Orientada a objetos. La OOP es una forma de organizar código y aunque nos permite una gran versatilidad, en Python es posible escribir código sin orientarlo a objetos. Hacer uso del paradigma de orientación a objetos es pensar y organizar el código en términos de *clases* y *objetos*. A los objetos también se los llama *instancias*. [Recursos python](https://recursospython.com/guias-y-manuales/clases-y-orientacion-a-objetos/)

Podemos definir una **clase** (`class`) como una Plantilla o Modelo para crear a partir de ella ciertos Objetos. Esta plantilla es la que contiene la información, características y capacidades que tendrá el objeto que sea creado a partir de ella. De este modo los objetos creados a partir de ella estarán agrupados en esa misma clase. [Pythones.net](https://pythones.net/clases-y-metodos-python-oop/)

Las clases e instancias las podemos concebir con el simil de planos y casas. Al diseñar la casa se deben incluir ciertos elementos que desamos como medida de la vivienda, números de habitaciones y baños y su correspondiente ubicación, número de plantas, materiales, distribución de los espacios, etc. El plano en sí mismo no constituye la casa como tal sino que es una descripción de cómo se verá una vez construida. Del mismo modo, la clase no constituye ningún objeto en particular sino que define las propiedades (variables y funciones) que  tendrán las instancias de dicha clase una vez creadas. Las variables y funciones que están dentro de una clase llevan el nombre de *atributos* y *métodos*, respectivamente. [Recursos python](https://recursospython.com/guias-y-manuales/clases-y-orientacion-a-objetos/)

Los objetos almacenan información y realizan tareas. Los atributos de dicho objeto pueden llamarse **características** las cuales nosotros definimos. Y los **métodos*** son las tareas que son capaces de realizar. Por ejemplo si la `clase` es animal, un objeto instanciado podría ser `perro`: 

|Clase ->| Animal|
|------|-------|
|**Atributos**|
|Color:|Negro|
|Raza:|Pincher|
|**Métodos**|
|Ladra( )|
|Corre( )|
|Olfatea( )|

[Pythones.net](https://pythones.net/clases-y-metodos-python-oop/)

Las clases en Python se utilizan principalmente para los siguientes propósitos:

#### 1. Encapsulación
Las clases permiten encapsular datos y funciones relacionadas en una unidad lógica, facilitando la organización y mantenimiento del código.

#### 2. Reutilización de código
Las clases permiten crear objetos que comparten atributos y métodos, lo que facilita la reutilización de código y evita la duplicación.

#### 3. Abstracción
Las clases permiten abstraer detalles de implementación, simplificando el uso de los objetos.

#### 4. Herencia
Las clases permiten crear nuevas clases a partir de otras existentes, heredando sus atributos y métodos

Las clases se definen utilizando la plalabra `class`seguida del nombre que deseamos asignarle, normalmente con el formato JS, si es un nomnbre con más de una palabra debemos poner en mayúscula la primera letra, por elemplo:

```python
class DatosPersonales:

 def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

```
Justo después de la definición de la clase, se puede incluir una cadena de documentación que describe la funcionalidad de la clase. Esto se hace con el comando para definición de una variable `def` seguida del método. A continuación definimos el método anteponiendo guión bajo dos veces, seguido de la palabra 'init' y cerrando con doble guión bajo. Esto es algo que está disponible para las clases y la forma en que el constructor `__init__` funciona es llamando una función automáticamente cada vez que cree una instancia de la clase. 

Seguido del doble guión tras *init* viene un paréntesis para introducir los argumentos de la función. El primer argumento que debe `self` porque cada función dentro de una clase de Python necesita self. Separado por comas ponemos los nombres de los argumentos que usaremos, en el elemplo `(self, nombre, edad)` y terminamos con dos puntos como en la definición de cualquier función en Python.

Dentro de esta función de inicio, se agregan los datos directamente a la clase y la forma de hacerlo es diciendo **self** seguido de punto y luego crearemos un nombre de la variable donde se va almacenar la información, generalmente corresponde al argumento de las funciones: 

```
 self.nombre = nombre
 self.edad = edad
```
Lo que queremos hacer es que que cualquier cosa que se asigne en los argumentos pase a estas dos nuevas variables.

Para asignar los métodos de la instancia lo hacemos del mismo modo en que se definen las funciones. Estos métodos también utilizan la palabra clave **self** para acceder a los atributos de la instancia. Por ejemplo si queremos devolver una cadena formateada (*'string interpolation'*) podríamos decir:

```python
class DatosPersonales:

 def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
 def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
```
Para crear una instancia (*'instantiate'*) creamos una nueva variable donde se almacenará la información seguida del símbolo igual, invocando a continuación la función y almacenando los valores de los argumentos dentro del paréntesis, por ejemplo: 

`usuarioUno = DatosPersonales("John", 40)` 

Finalmente podemos llamar la función definida como el método dentro de la clase que en este caso es una cadena formateada usando 

`print(usuarioUno.saludar())`

El código completo resultaría como sigue:

```python
class DatosPersonales:

 def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
 def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

usuarioUno = DatosPersonales("John", 40)

print(usuarioUno.saludar())
```

> ### 2. ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
Cuando se crea una instancia de una clase en Python, el método que se ejecuta automáticamente es el método `__init__( )`.
El método `__init__( )` es un método especial, también conocido como **"constructor"**, que se utiliza para inicializar los atributos de la clase cuando se crea un nuevo objeto. Ejemplo anteriormente citado:

```python
# Crear la clase "DatosPersonales" como el esquema en el que se recogen los argumentos de los datos personales de un usuario:
class DatosPersonales:
    """Clase para representar un usuario"""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
# Crear una instancia de la clase DatosPersonales:
usuarioUno = DatosPersonales("John", 40)

# Hacer un llamado para el "usuario Uno" con el método del saludo:
print(usuarioUno.saludar())

# Salida: 
# Hola, mi nombre es John y tengo 40 años.
```
En este ejemplo, cuando creamos la instancia usuarioUno = DatosPersonales("John", 40), el método `__init__()` se ejecuta automáticamente y se inicializan los atributos nombre y edad de la clase `DatosPersonales`.
Algunas características importantes del método **init( )** son:
- Se ejecuta automáticamente cuando se crea una instancia de la clase.
- Permite inicializar los atributos de la clase con valores específicos.
- Puede recibir parámetros que se utilizan para inicializar los atributos.

El método __init__() es fundamental en la programación orientada a objetos en Python, ya que permite crear objetos con estados iniciales específicos y preparados para su uso.

> ### 3. ¿Cuáles son los tres verbos de API?

Los tres verbos HTTP más comunes utilizados en las API son:
- **GET*:** Se utiliza para recuperar datos de un recurso específico. Por ejemplo, obtener información de un usuario.

- **POST:** Se utiliza para crear un nuevo recurso. Por ejemplo, crear un nuevo usuario.

- **PUT:** Se utiliza para actualizar un recurso existente. Por ejemplo, actualizar la información de un usuario.

Estos verbos HTTP forman parte de la arquitectura REST (del inglés *'Representational State Transfer'*), que es un estilo de arquitectura de software ampliamente utilizado en el desarrollo de API.

> ### 4. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL, lo que significa que no utiliza el modelo de datos relacional tradicional de las bases de datos SQL. En su lugar, MongoDB almacena datos en documentos similares a JSON, lo que lo hace más flexible y escalable para manejar grandes volúmenes de datos no estructurados. Regularmente los registros en Mongo son pares clase valor (*key:value*).

El modelo de documentos de MongoDB resulta muy fácil de aprender y usar, y proporciona a los desarrolladores todas las funcionalidades que necesitan para satisfacer los requisitos más complejos a cualquier escala

> ### 5. ¿Qué es una API?

Una **API** o interfaz de programación de aplicaciones (del inglés: *'Application Programming Interface'*) es un conjunto de reglas o protocolos de programación que permite a las aplicaciones informáticas comunicarse entre sí para intercambiar datos, características y funcionalidades de manera **estandarizada** y **segura**. Las API simplifican y aceleran el desarrollo de aplicaciones y software permitiendo a los desarrolladores integrar datos, servicios y capacidades de otras aplicaciones, en lugar de desarrollarlas desde cero. [IBM/blog](https://www.ibm.com/es-es/topics/api)

La API establece especificaciones formales sobre el modo en que se comunican servicios y productos digitales.

### Las API permiten a los desarrolladores:

- Evitar trabajo redundante al incorporar funciones de aplicaciones existentes en nuevas aplicaciones.

- Extraer archivos o datos preexistentes dentro de un software y utilizarlos en otro programa o en uno de sus otros niveles.

- Comunicarse entre aplicaciones de manera segura y eficiente.


### Las API se pueden clasificar por casos de uso: 

API de datos, API de sistemas operativos, API remotas y API web. [IBM/blog](https://www.ibm.com/es-es/topics/api)

- **API de datos** (o bases de datos)
Se utiliza para conectar aplicaciones y sistemas de gestión de bases de datos.

- **API del sistema operativo** (local)
Se usa para definir cómo las aplicaciones usan los servicios y recursos del sistema operativo.

- **API remotas**
Se utiliza para definir cómo interactúan las aplicaciones en diferentes dispositivos.

- **API web**
Se utiliza para permitir la transferencia de datos y funcionalidades a través de Internet mediante el protocolo HTTP.

Hoy en día, la mayoría de las API son API web de tipo remota (utiliza protocolos para manipular recursos externos). Existen varios tipos de API, incluyendo:

- **API de terceros:** se refiere a una API proporcionada por una empresa o organización para que otros desarrolladores la utilicen en sus aplicaciones.

- **API interna:** se refiere a una API utilizada dentro de una aplicación o empresa para comunicarse con otros sistemas o servicios.

Ejemplos:

- La API de Facebook que permite a los desarrolladores crear aplicaciones que se integren con la red social.
- La API de un banco que permite a los desarrolladores crear aplicaciones que permitan realizar transacciones financieras.
- La API de un servicio de pronóstico del tiempo que permite a los desarrolladores crear aplicaciones que muestren el pronóstico del tiempo en tiempo real.
Una API es un conjunto de reglas y protocolos que definen cómo los diferentes software pueden comunicarse e interactuar entre sí. Las API permiten a las aplicaciones acceder a datos o funcionalidades de otros sistemas de manera estandarizada y segura.


> ### 6. ¿Qué es Postman?

Postman es una herramienta de desarrollo de software utilizada para probar y documentar API. Permite enviar solicitudes HTTP, ver las respuestas, y explorar la documentación de las API, en definitiva, comunicarse con API externas.
En el caso de las API recuperas datos en lugar de una página web.

Es muy útil para el desarrollo y la depuración de API debido a que failita la lectura y permite visualizar la estructura de control del código.

Es una forma muy útil de crear aplicaciones y pasar datos de un lado a otro. Postman no es específico de un lenguaje de programación por lo que se puede usar para depurar código de cualquier ambiente de programación, lo que hace de Postman una herramienta muy versátil.

    Postman simplifica cada paso del ciclo de vida de la API y agiliza la colaboración para que puedas crear mejores API y más rápido.


> ### 7. ¿Qué es el polimorfismo?

El polimorfismo es un principio de la programación orientada a objetos que permite que objetos de diferentes clases puedan ser tratados de la misma manera. Esto se logra a través de la herencia y la sobrecarga de métodos. 

El término polimorfismo tiene origen en las palabras ***poly*** (muchos) y ***morfismo*** (de formas) proviene de la palabra que significa cambiar, lo que significa que puede tener muchos cambios o que un elemento puede tener muchas formas. Aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas, lo quiere decir que los **objetos** de diferentes clases pueden ser accedidos utilizando el mismo interfaz, mostrando un comportamiento distinto (tomando diferentes formas) según cómo sean accedidos. [El Libro de Python.](https://ellibrodepython.com/polimorfismo-en-programacion)

Por ejemplo, si tenemos una clase `Animal` con un método `hacer_sonido()`, las clases `Perro` y `Gato` (que heredan de Animal) pueden tener su propia implementación de `hacer_sonido()`, lo que permite tratar a un Perro y a un Gato de manera polimórfica. El polimorfismo por tanto está exhibiendo un comportamiento diferente en diferentes condiciones. En este caso las clases, `Perro` y `Gato` heredan el método de la anterior y además, implementan el método `hacer_sonido()` de una forma distinta. [Cosmiclearn/Blog.](https://www.cosmiclearn.com/lang-es/python-polymorphism.php#overloading)

Ejemplo: 
```python
class Animal:
	def hacer_sonido(self):
		raise NotImplementedError

class Cat(Animal):
	def hacer_sonido(self):
		print("Meoooowwwww")

class Dog(Animal):
	def hacer_sonido(self):
		print("Woooooof")

#Salida:
# Meoooowwwww
# Woooooof

```
De este modo, tenemos un comportamiento bastante poderoso en una cantidad muy corta de código. Aprovechamos la programación orientada a objetos, la herencia y el polimorfismo.


> ### 8. ¿Qué es un método dunder?

Los métodos dunder, también conocidos como métodos mágicos o métodos especiales en Python son métodos que comienzan y terminan con doble guión bajo, como `__init__()` o `__str__()`. En otros lengujes de programación no se requiere el uso de este tipo de sintaxis porque la mayoría cuenta con lo que se denomina métodos privados o protegidos. 

Estos métodos tienen un significado especial para Python y se utilizan para definir el comportamiento de los objetos de una clase. Por ejemplo, el método `__init__()` se utiliza para inicializar los atributos de un objeto cuando se crea una instancia de la clase. En el caso del método `__str__` que corresponde a una cadena puede ser usado como una función que me permite depurar el código y determinar si hay algún error en la definición de las clases, es es una forma de obtener información útil sobre cualquier clase con la que esté trabajando.

Otro método dunder que es frecuente en Python es `__repr__` similar al método de cadena (*'string'*) aunque se usa más para salida sin formato. Es algo que le gustaría enviar a sus registros o a un registro de errores con información completa. Estos son los verdaderos datos sin procesar (*'raw data'*) de la instancia de la clase. De este modo nos ayuda a resolver algunos problemas con el código y a depurarlo. Al programar **repr** por tanto usamos información completa con detalles para que sea más sencillo encontrar errores en el código de esta clase.

```python
class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for ${self.total} USD"

  def __repr__(self):
    return f"Invoice < value: client: {self.client}, total: {self.total})"

# Llamado de la instancia:
inv = Invoice('Google', 500)


print(str(inv))
# Salida: "Invoice from Google for $500 USD"

print(repr(inv))
# Salida:Invoice <value: client: Google, total: 500>

```


> ### 9. ¿Qué es un decorador de python?

Un decorador en Python es una función que toma otra función como argumento, le añade funcionalidad adicional y devuelve una nueva función. Los decoradores nos permiten reducir las líneas de código duplicadas, hacer nuestro código sea legible, fácil de testear y fácil de mantener. 

Los decoradores se utilizan para modificar el comportamiento de una función sin cambiar su código.

Pensemos en tres funciones: ***a***, ***b*** y ***c***, en las que *a* recibe como parámetro *b* para dar como salida a *c*:

> a(b) -> c



```python
def funcion_a(funcion_b):
    def funcion_c():
        print('Antes de la ejecución de la función a decorar')
        funcion_b()
        print('Después de la ejecución de la función a decorar')

    return funcion_c
```
Al utilizar la palabra "decorar" estamos indicando que queremos modificar el comportamiento de una función ya existente, pero sin tener que modificar su código. Esto es muy útil, principalmente, cuando queremos extender nuevas funcionalidades a dicha función. 

Para decorar una función basta con colocar, en su parte superior de dicha función, el decorador con el prefijo ***@***. Usando los parámetros ***args*** y ***kwargs*** podremos reutilizar el decorador, haciendolo aún más flexible. [códigofacilito/Blog](https://codigofacilito.com/articulos/decoradores-python) 

```python
def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return funcion_c

# => decorador = funcion_a(suma)
@funcion_a
def suma(a, b):
    return a + b

#    decorador(10, 20) 
print(suma(10, 20))

# Resultado:
# Antes de la ejecución de la función a decorar
# Entra en la función suma
# Después de la ejecución de la función a decorar
# 30
```
