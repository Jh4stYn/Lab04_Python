# Lab04_Python
## Cuestionario
-¿Qué son los archivos *.pyc?
Los archivos .pyc son archivos de código compilado generados por Python. Cuando se ejecuta un archivo .py, Python compila el código fuente en un código de bytes intermedio llamado bytecode. Este bytecode se guarda en un archivo .pyc para su posterior uso y mejora el rendimiento en ejecuciones futuras.

-¿Para qué sirve el directorio pycache?
El directorio __pycache__, o pycache, es un directorio especial que se crea automáticamente en Python 3 para almacenar los archivos .pyc. Este directorio se utiliza para guardar los archivos de código compilado en bytecode y acelerar la carga y ejecución del código en futuras ejecuciones. Cada módulo o paquete de Python puede tener su propio subdirectorio __pycache__ para almacenar sus archivos .pyc.

-¿Cuáles son los usos y lo que representa el subguión en Python?
El guion bajo (_) en Python tiene varios usos y representaciones:

Convención para variables y métodos privados: Por convención, se utiliza un guion bajo al comienzo de un nombre de variable o método para indicar que es privado y no debería ser accedido directamente desde fuera de la clase o módulo. Sin embargo, Python no impide el acceso a estas variables o métodos, ya que no existe un mecanismo de acceso estricto.

Nombre especial en interpretación interactiva: En el intérprete interactivo de Python, el guion bajo (_) se usa para almacenar el resultado del último cálculo o expresión. Por ejemplo, si ejecutas 3 + 4 en el intérprete interactivo, el resultado se almacenará en _ y podrás usarlo posteriormente en otros cálculos.

Convención para nombres de módulos y paquetes privados: Por convención, se utiliza un guion bajo al comienzo de un nombre de módulo o paquete para indicar que es privado y no debería ser importado directamente desde fuera del paquete. Sin embargo, Python no impide la importación de estos módulos o paquetes.


