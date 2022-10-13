print("""
Estructura de datos
Las estructuras de datos son una forma de representar la información,
esta manera de reproducir los datos tiene una serie de reglas internas
que ayudan a organizar mejor a la información. Dependiendo de la estructura
usada realizará de una forma mas eficiente determinadas tareas,
lo que permite crear la solución adecuada mediante el lenguaje que se
esté usando para programar.

Lista
Este es una estructura de datos usada en python para almacenar información
y ordenarla, ya que en las lista hay un índice que indica tanto el primer,
segundo y tercer elemento, hasta el último almacenado.
------------------------------------------------------------------------------

list.append(elemento)    Añade como último elemento la información que le
                         estamos indicando
list.clear()             Elimina todos los elementos de la lista
x = list.copy()          Copia una lista ya existente en otra
list.count()             Retorna la cantidad de elementos que hay dentro de
                         la lista, es decir cuantas veces está un elemento
list.extend(iterable)    Inserta los elementos de otra  lista en la que le
                         indicamos.
list.index(elemento)     Retorna el índice del elemento que buscamos
list.insert(posición,    Añade el elemento donde le indiquemos
elemento)
list.pop(posición)       Elimina el elemento indicado, si no se indica se
                         eliminan todos los elementos
list.remove(elemento)    Elimina el elemento indicado
list.reverse()           Invierte el orden de la lista
list.sort                La lista se ordena en orden alfabético, también se
                         puede hacer una función para ordenarlos de otra forma

------------------------------------------------------------------------------

""")
list1 = ["Orange", "Grapple", "Watermelon", "Pinapple", "Avocado"]
print(f"Lista antes de aplicarle el método\n\n{list1}\n\nlist1.append(\"Banana\")\n")
list1.append("Banana")
print(f"La lista después de añadirle un elemento\n\n{list1}\n")

print(f"Lista antes de aplicarle el método\n\n{list1}\n\nlist1.clear()\n")
list1.clear()
print(f"Lista después de quitarle todos los elementos\n{list1}")

list1 = ["Orange", "Grapple", "Watermelon", "Pinapple", "Avocado"]
print(f"\nLista antes aplicarle el método count\n\n{list1}\n\nlist1.count()\n")
x = list1.count("Grapple")
print(f"Cantidad de veces que está el string Grapple en la lista\n{x}")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(f"Lista a y b antes de sumar b a a\n\na = {a}\nb = {b}\n")
a.extend(b)
print(f"Lista a después de añadirle la lista b\n{a}")

print(f"\nLista antes de aplicarle el método para hallar el ìndice del elemento al cual deseamos saber su posición\n\n{list1}\n\nlist1.index()\n")
x = list1.index("Watermelon")
print(f"Índice del elemento Watermelon obtenido mediante el método\n{x}")

print(f"\nLista antes de añadirle el elemento con el método\nlist1.insert(3,\"Peach\")\n\n{list1}")
list1.insert(3, "Peach")
print(f"Lista despues de insertarle un elemento en la posición 3\n{list1}")

print(f"\nLista antes de usar el método pop\n\n{list1}")
list1.pop(3)
print(f"\nLista después de eliminar el elemento con índice 3\n{list1}")

print(f"\nLista antes de eliminar un elemento mediante el método remove\n{list1}\nlist1.remove(\"Pinapple\"))")
list1.remove("Pinapple")
print(f"\nLista después de haberle quitado el elemento Pinapple\n{list1}\n")

print(f"Lista antes de invertir su orden median el método reverse\n\n{list1}\nlist1.reverse()\n")
list1.reverse()
print(f"lista después de invertir el orden\n{list1}\n")

list1 = ["Orange", "Grapple", "Watermelon", "Pinapple", "Avocado"]
print(f"Lista antes de ordenarla por orden alfabético\n\n {list1}\nlist1.sort()")
list1.sort()
print(f"\nLista después de haber sido ordenada mediante el método sort\n{list1}")
"""
------------------------------------------------------------------------------
Listas como pilas

Se pueden usar las listas como pilas, ya que el nuevo elemento que se a va insertar será el último en la lista, a su vez será el primero en ser eliminado. Esto se hace gracias a los métodos pop y append.
------------------------------------------------------------------------------

Ejemplo
"""
list = [1,2,3]
list.append(4)
list.append(5)
print(f"\nGraficación de los elementos de la lista tras un append\n{list}")
list.pop()
print(f"\nLista tras haber eliminado el último elemento con el método pop\n{list}")
list.pop()
print(f"\nLista tras haber eliminado el último elemento con el método pop\n{list}")

"""
------------------------------------------------------------------------------
Listas como colas

Se pueden usar las listas como colas, es decir que el primer elemento en ser
añadido es el primero en ser retirado de la lista, por eso se dice que se usan como
colas, ya que el primero que llega es el primero en irse. Esto se hace gracias a la
colección deque
------------------------------------------------------------------------------
"""

from collections import deque

list = deque(["Mario", "Maicol", "Nicol"])
list.append("Maria")
list.append("Jose")
print(f"\nLista después de añadir los elementos\n{list}")

list.popleft()
#Esto elimina el primer elemento de la lista, el primero en llegar
print(f"\nLista después de eliminar el primer elemento\n{list}")
#Este código elimina el segundo elemento en la cola
list.popleft()
#Esto elimina el segundo elemento de la lista, el segundo en llegar
print(f"\nLista después de eliminar el segundo elemento\n{list}")

"""
------------------------------------------------------------------------------
Comprensión de listas

Las comprensiones permiten crear listas de una forma concisa. Se usan para la
creación de una lista que se va creando a aprtir de los resultados de otra
operacición, por lo que son usadas en casos muy específicos. Es una forma práctica
de escrbir las listas ahorrando líneas de código.

En pcoas palabras la comprensión de listas es poder ingresar un dato en una lista
mediante ciclos for e if, todo dentro de una sola línea
------------------------------------------------------------------------------
"""

#En este caso lo que se busca es almacenar la potencia cuadratica del índice del ciclo, pero todo se va a hacer en tan solo una líne de código
list = [x*x for x in range(10)]
print(f"""\nAhora vamos a ver que en la lista solo se almacenaron las potencias
cuadradas de cero a nueve\n{list}""")

#También se pueden anidar ciclos y sentencias if en una lista, lo que ayuda a ahorrar líneas de codificación
list = []
list1 = [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y]
print(f"\nAhora vamos a ver como se creo un arreglo con las caracteristicas que dimos\n{list1}")

"""
------------------------------------------------------------------------------
Las listas por crompesión anidadas
Las listas de comprensión anidadas no facilitan con la tarea de crear arreglos con
mucha mas facilidad, ya que nos permite dividir una lista por filas y columnas con
mucha mas facilidad.

Lo que podemos hacer es que dentro de una lista que está dentro de otra lista hacer
una compresnsión y en lista de primer nivel seguir con la compresión de la lista.
------------------------------------------------------------------------------
"""

#Ejemplo de comprensión de lista anidada
matrix = [1,2,3,4],[5,6,7,8],[9,10,11,12]
list = [[row[i] for row in matrix] for i in range (4)]

print(f"""\nLista que se creo a partir de la matriz, donde el primer dato es el
primero de cada lista de la matriz y el segundo es el segundo de cada lista de la
misma matriz y así sucesivamente\n{list}""")

"""
------------------------------------------------------------------------------
La instrucción del

la instrucción del sirve para eliminar el elemento que queremos de una lista
mediante si índice. Este es diferente al método pop, ya que retorna un valor.

La instrucción del sirve a su vez para quitar secciones de código como lo
haríamos cuando queremos que solo se muestre una parte del código con los dos
puntos en donde el valor de la izquierda determina desde que parte se secciones y
el de la derecha muestra hasta cual parte llega la sección, pero sin incluir este
valor.

del también sirve para eliminar variables
------------------------------------------------------------------------------
"""
#Aquí creamos una lista a la cual posteriormente vamos a modificar con del
list = [5, 7 ,-5, 99.15, 456]
del list[0]
print(f"\nLista después de haber eliminado su primer método con del\n{list}")


"""
------------------------------------------------------------------------------
Tuplas

Las tuplas son otra forma de guardar un conjunto de elementos que resulta siendo
similar a las listas, pero se usan en diferentes casos. Las listas normalmente se
usan cuando se necesitan almacenar datos heterogéneos, es decit que puede
contener desde datos booleanos, strings, valores etc en una misma tupla, además
de que permite que la información no cambie, ya que esa es otra propiedad de la
tupla, que es inmutable.

Además las tuplas solo se pueden crear declarando la varaible insertando su valor
y poniendo una coma al final.

ejemplo
x = "rice",
------------------------------------------------------------------------------
"""

#Ejemplo de empaquetado de una tupla
x = 1
y = 2
z = "Berries"
tuple = x,y,z
print(f"\nEmpaquetado de elementos en una tupla\n{tuple}")

#Desempaquetado de elementos de una tupla
tuple2 = ("Alemania", 472, "Rusia")
(country, val, second_country) = tuple2
print(f"\nDesempaquetado de elementos en una tupla\n{country} {val} {second_country}")

"""
------------------------------------------------------------------------------
Conjuntos

Los conjuntos al igual que las anteriores colecciones de datos nos permiten
almacenar información, pero con la diferencia de que los conjuntos restringen la
información repetida, es decir que no puedo volver a alamacenar un dato que
previamente ya había almacenado. Se pueden crar declarando una varibale y
poniendo los elementos dentro de las llaves {}, pero para declarar un conjunto
vacío se usa la función set(), y así mismo se pueden crear conjuntos sin el uso
de las llaves. Son usados para saber si un elementos pertenece a un conjunto o
para evitar la repetición de información.

Los conjuntos también pueden ser operados, es decir se pueden hacer uniones, intersecciones, diferencias y diferencia simétrica.
------------------------------------------------------------------------------
"""

#Preguntas de verificación sí berries está en setExample

setExample = {"Berries", "Watermelon", "soursop", "tangerine"}
x = "orange" in setExample
print(f"\nResultado de la pregunta de sí orange está en setExample\n{x}")

#Ver las únicas letras que se manejan en un conjunto
setExample = set("pensilvania")
print(f"Letras de la palabra pensilvania\n{setExample}")

#Diferencia de conjuntos
x = set("california")
y = setExample - x
print(f"\nDiferencia de los conjuntosx setExample y y \n{y}")

#Elementos que están en setExample y x
y = setExample | x
print(f"\nElementos que tienen los conjuntos setExample y y\n{y}")

#Elementos en común de los elementos
y = setExample & y
print(f"\nElementos que tienen en común los conjuntos setExample y y\n{y}")

#Comprensión de listas en conjuntos
setExample = {x for x in "adventure" if x not in "past"}
print(f"\nMostrar sí determinados elementos están en el conjunto, usando compresión\n{setExample}")

"""
------------------------------------------------------------------------------
Los diccionarios se usan para guardar elementos y que tengan como índice una
clave, que puede ser un string, valor o tupla, desde que esta no poseea ningún
valor que sea modificable, ya que si esto es así no podrá crear el diccionario de
forma exitosa. Las llaves tienen que ser únicas como un ID para cada elemento.
------------------------------------------------------------------------------
"""

#Forma de declarar un diccionario
dictionary = {"oreo" : "8.1.0",
        "snow cone" : "12.1.0",
        "jelly bean" : "4.1.0",
        "marshmellow" : "6.0",
        "nougat" : "7.0"
       }
print(f"\nDiccionario impreso en consola\n{dictionary}")

#Usando la clave para llamar un elemeneto
x = dictionary["oreo"]
print(f"\nElemento de la clave oreo\n{x}")

#Eliminando un elemento mediante su clave
del dictionary["oreo"]
print(f"\nEliminación del elemento con clave jelly bean\n{dictionary}")

#Listar claves del diccionario
x = dictionary.keys()
print(f"\nListar claves del diccionario\n{dictionary}")

#Oordenar las claves del diccinario
print(f"\nDiccionario ordenado\n{sorted(dictionary)}")

#Consultar si una clave está en el diccionario
x = "oreo" in dictionary
print(f"\nConsultando si la clave oreo está en dict\n{dictionary}")

#Creando un diccionario con la función dict
dictionary = dict([("oreo", "8.1.0"),
                  ("snow cone", "12,1,0"),
                  ("jelly bean", "4.1.0"),
                  ("marshmellow", "6.0"),
                  ("nougat", "7.0")
                  ])
print(f"\nDiccionario hecho con la función dict\n{dictionary}")

#Comprensión usada en listas
dictionary = {x: x**2 for x in (1, 2, 3, 4, 5)}
print(f"\nDiccionario hecho mediante compresión\n{dictionary}")

#Diccionario hecho de otra forma con dict
dictionary = dict(jelly_bean = 4.1,
                  marshmellow = 6.0,
                  nougat = 7.0)
print(f"\nDiccionario hecho mediante dict\n{dictionary}")

"""
------------------------------------------------------------------------------
Técnicas de iteración

Son las formas en que podemos obtener tanto la llave como su contenido de una
secuencia de datos.
------------------------------------------------------------------------------
"""
#Primera técnica para iterar
dictionary = {"oreo" : "8.1.0",
        "snow cone" : "12.1.0",
        "jelly bean" : "4.1.0",
        "marshmellow" : "6.0",
        "nougat" : "7.0"
       }
print("\nAccediendo a las claves y su información al tiempo")
for x, y in dictionary.items():
  print(x,y)

#Usando una función para darle un índice incremental a la información
print("""\nAsignandole un índice a las claves que parte de cero hasta el números
de elementos que hay en el diccionario""")
for x, y in enumerate(["Are you ready?", "Go", "Run"]):
  print(x, y)

#Obtener las llaves e información de dos secuencias
dictionary = ["Oreo", "Snow cone", "Jelly bean", "Marshmellow", "Nougat"] 
dictionary2 = ["8.1.0", "12,1.0", "4.1.0", "6.0", "7.0"]
print("""\nEl primer elemento de la primera lista está relacionado con el primer elemento de la segunda lista""")
for x, y in zip(dictionary, dictionary2):
  print("El nombre en clave de la versión android {0}, y su número de versión es: {1}".format(x,y))

#Para invertir el orden de los datos se usa reversed
print("\nVamos a inveritr el orden de la secuencia de los datos")
for i in reversed(range(1,10)):
  print(i)

#Se puede imprimir una secuencia de datos sin necesidad de modificar la orginal
print("\nVamos a ordenar los últimos datos que recibimos en la variable list, esto lo hará de menor a mayor")
for x in sorted(set(list)):
  print (x)

"""
------------------------------------------------------------------------------
Mas cerca de las condiciones

Las condiciones while e if pueden contener cualquier tipo de operador, no solo comparativo.

El opereador in y not in comprueba si un valor está o no un en contenedor. Los operador is y not is comprueban si dos objetos son realmente el mismo.

Los comparadores booleanos también pueden usarse para que se cumplan mas de una condicioón u otra en las sentencias if.
------------------------------------------------------------------------------
"""

string1, string2, string3 = "The hammer Jam", "Exploit", "Fruit explosion"
no_nulo = string1 or string2 or string3
print(f"\nAlmacenando una comparaión en una variable\n{no_nulo}")

"""
------------------------------------------------------------------------------
Comparación de secuencias y otros tipos de datos

También se pueden comparar otros tipos de datos como strings, tuplas, listas. Esto nos permite hacer operaciones de comparación para poder por ejemplo saber que string contiene mas carácteres que otro, cual tupla posee mas datos y si nos ponemos a mirar con mas profundidad hacer sentencias if para que se realice determinada acción si la cantidad de información en las tuplas no es la misma
------------------------------------------------------------------------------
"""

a = (1,2,3) < (5,6,7)

print(f"Imprimiendo el resultado de comparar dos tuplas.\n{a}")