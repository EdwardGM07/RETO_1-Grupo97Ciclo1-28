
# RET0 1 

Usted ha sido contratado por una institución educativa para desarrollar el sistema de
gestión académica y administrativa, dentro de los requisitos el rector de la institución ha
expresado que el sistema debe permitir realizar la gestión de notas de los estudiantes. Para
esto debe implementar las fases de la metodología IDEAL.
En el plantel se maneja el sistema de calificación colombiano el cual califica de 0.0 a 5.0,
donde 0.0 es la nota más baja y 5.0 la más alta. 

## Funcion 1
Se debe implementar una función tal que
reciba la nota que obtuvo un estudiante y retorne un mensaje el cual se refiere al estado de
aprobación con la materia, para esto se debe de tener las siguientes consideraciones, si la
nota final es mayor o igual a 3.0 retornar “gana”. Si la nota es menor a 3.0 y mayor o igual
a 2.2 retornar “recupera”, si la nota es menor a 2.2 retornar “pierde”.

# Funcion 2

Por cuestiones de acreditaciones internacionales los estudiantes deben conocer su nota en
el sistema de calificación americano, el cual utiliza letras. Para hallar la letra
correspondiente que exige la acreditación internacional, en la institución educativa se debe
realizar un proceso de conversión, pasando de la escala colombiana (0.0 a 5.0) a el grado
numérico (0 a 100) de la escala americana y finalmente la letra correspondiente teniendo
en cuenta la siguiente tabla. 

Grado Numérico Grado en Letra
Grado mayor o igual a 90 A
Menor de 90 pero mayor o igual a 80 B
Menor de 80 pero mayor o igual a 70 C
Menor de 70 pero mayor o igual a 69 D
Menor de 69 F
Tabla 1. Referencia conversión notas sistema americano
A continuación, se brindan algunos ejemplos:
Ejemplo 1: La nota más alta que un estudiante puede obtener en la institución es de 5.0
esto en el sistema americano corresponde al grado numérico de 100 puntos por tanto la
calificación en letra es A.
Ejemplo 2: La nota más baja que puede obtener un estudiante en la institución educativa
es 0.0, dicha nota en el sistema americano el grado numérico sería de 0.0, por lo cual la
calificación en letra es F.
Ejemplo 3: Si un estudiante obtiene un 3.8 en la institución educativa en el sistema
americano el grado numérico sería 76 por lo cual la letra sería C.
Implemente una función tal que reciba la nota final de un estudiante y retorne la letra que
le corresponde en la escala americana.
# Entrega
Fecha y modo de entrega
Domingo 13 de junio de 2021 a las 23:59
Se debe subir a la plataforma un documento explicando y aplicando las etapas del proceso
IDEAL.
Se debe escribir un programa en Python en la plataforma Replit para solucionar el
problema, siguiendo el esquema planteado por el docente. ¡Mucha suerte!