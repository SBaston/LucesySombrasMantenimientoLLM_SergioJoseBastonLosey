# Caso Práctico: Luces y sombras del uso del LLMs para el mantenimiento del software

Bienvenido a nuestro caso práctico donde abordaremos el uso del LLMs para el mantenimiento del software. 

Para la realización de este caso práctico queremos que os pongais en la siguiente situación/escenario: 

"Sois unos nuevos trabajadores de una gran empresa la cual os ha contratado hace varios meses. Tras los primeros meses de adaptación y aprendizaje al estilo de trabajo de la empresa, se os ha encomendado la gran primera tarea de manera individual. 
Esta tarea consiste en entender un código en Python que realizó un antiguo desarrollador que lamentablemente ya no se encuentra en la empresa. Este código es de vital importancia para el siguiente proyecto de la empresa. 
Vuestro jefe os ha pedido que cogais ese código y lo entendais y que le realiceis las modificaciones necesarias que veais oportunas ya que la semana que viene tendréis que presentarselo a vuestros superiores."

Aquí vuestros ángeles de la guarda David y Adrián os van a ayudar a realizar esta tarea para que vuestro jefe no os eche y podais conservar este trabajo que tanto sudor y lágrimas os ha costado conseguir. Os proponemos el uso de una IA para detectar errores y mejorar la legebilidad del código. 
La IA que usaries es Codium que es una plataforma de revisiones de código con IA que detecta errores y ayuda a mantener la calidad del código. 

A continuación os mostraremos los pasos tanto previos como principales, además de las tareas que debeis de realizar para superar esta práctica y que le podais entregar el mejor resultado a vuestro jefe.

# Pasos previos: 
- Tener descargado Visual Studio Code
- Tener descargado python 3, si no lo teneis descargado a través de este enlace os lo podeis descargar (https://www.python.org/downloads/).
- Descargaros la extensión Qodo (imagen de un oso hormiguero) en VSCode. 
- Forkear este mismo repositorio (https://github.com/davidabuinESI/LucesySombrasMantenimientoLLM.git) , añadiendole vuestro nombre.
- Clonar vuestro repositorio forkeado localmente, obteniendo los archivos "app.py" y "app_test.py".

# Pasos a seguir: 
1. Abrir el repositorio en VSCode para poder acceder a los archivos.
2. Crear un archivo markdown (.md) llamado AnalisisNombre.md, siendo Nombre vuestro Nombre
3. Realizar un breve ánalisis de manera individual del archivo "app.py" donde debereis de apuntar en el nuevo markdown creado (mirar paso 2) los cambios que vosotros mismo realizariais a este código.
4. Una vez realizado el ánalisis ejecutar el test y apuntar el resultado que os de. Para ejecutar y obtener el resultado del test unicamente teneis que ejecutar el archivo nombre.py y se os ejecutará el test. 
5. Abrir el chat de Qodo e insetarle esta línea de texto (usaremos inglés para obtener un mejor resultado):
    "Refactor this code to make it clean, use descriptive variable names, add Type Hints and docstrings. Refactor this code       to make it clean, use descriptive variable names, add Type Hints and docstrings. Refactor and improve this code in a         new file called "RefactoringName.py" (cambiar Name por vuestro nombre). "
6. Comprar los archivos "app.py" con "RefactoringName.py". Tendreis que ver las diferencias entre las modificaciones que ustedes habeis pensado y las modificaciones que ha realizado nuestra IA.
7. Añadir al markdown (mirar paso 2) las principales diferencias que ustedes habeis visto entre vuestro análisis y el análisis generado por IA.
8. Volver a ejecutar el test (mirar paso 4). ¿Habéis obtenido el mismo resultado? Si no es así, ¿a qué se ha debido? Responder estas preguntas en el markdown
9. Revisar el código refactorizado por la IA e intentar encontrar alguna modificación innecesaria o alguna introducción de bugs lógicos o deudas técnica que la IA haya introducido a la hora refactorizar.

# Archivos a entregar
- Archivo python "RefactoringName.py" con la refactorización que os ha generado la IA
- Archivo markdown "AnalisisNombre.md" con los análisis, preguntas y diferencias que se os ha pedido en el enunciado
- La entrega del campus será el enlace a vuestro repositorio forkeado en la parte de comentarios + el archivo markdown creado por ustedes
