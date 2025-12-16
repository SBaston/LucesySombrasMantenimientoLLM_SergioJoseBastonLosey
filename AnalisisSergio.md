# Análisis individual de app.py

1. Faltan comentarios para comprender más fácil el código.
2. Utilizar un switch en vez de emplear tantas condiciones. Esto mejoraría la legibilidad del código y no habría tanto anidamiento.
3. Utilizar nombres más largos y específicos para las variables y no una sola letra.
4. Declarar y definir las variables fuera de cada condición para que sea más reutilizable.

# Resultados de la primera ejecución de los tests
......
----------------------------------------------------------------------
Ran 6 tests in 0.460s

OK

# Comparación entre app.py y RefactoringSergio.py
1. Ha añadido comentarios, además bastante útiles. 
2. Ha ordenado mejor la estructura del código, poniendo las clases y el main en mejores posiciones para que se distinga más fácilmente.
3. Ha creado una serie de constantes para facilitar la reutilización.
4. Los nombres de las variables son más largas y más específicas sobre lo que se refieren.
5. No ha empleado un switch.

Comparado con mi compañero a mí me ha escrito los comentarios en español y a él en inglés. Por lo demás, nos ha devuelto prácticamente el mismo código.

# Nueva ejecución del test
1. ¿Habéis obtenido el mismo resultado? Si no, ¿a qué se debe?
......
----------------------------------------------------------------------
Ran 6 tests in 0.540s

OK

[Done] exited with code=0 in 1.644 seconds

Se ha obtenido el mismo resultado pero con más tiempo. Se debe a que ha añadido bastante código que sacrifica tiempo de ejecución por legibilidad.