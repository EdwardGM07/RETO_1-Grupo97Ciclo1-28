# Identificar
a)	¿Cuál es el problema?
Se necesita un sistema de gestión académica y administrativa.
b)	¿Quiénes son los interesados?
La institución educativa.
c)	¿Cuál es el objetivo?
Retornar una notificación respecto a la nota final y convertir la nota final en Sistema de Calificación Americano. 
d)	¿Existen restricciones?
La nota debe ser de 0.0 a 5.0.
# Definir
a)	¿Qué conozco?
La nota final esta en sistema nacional colombiano que es de 0.0 a 5.0 y el sistema de calificación americano es de 0 a 100.
b)	¿Qué debo conocer?
Las condiciones para notificar si la nota final alcanza para ganar, recuperar o perder y la formula para calcular la nota en sistema de calificación americano.
c)	¿Dividir el problema en subproblemas?
1. Solicitar la nota final.
2. Evaluar si gana, recupera, pierde o error.
3. Convertir la nota final a sistema de calificación americano y evaluar si la nota es A, B, C, D, F y error.
4. Decir los resultados.
# Estrategia
a)	Ejemplos particulares 
--Requisito 1--
1. la nota final es -0.1 debe retornar error.
2. la nota final es 5.1 debe retornar error.
3. la nota final es 3.1 debe retornar gana.
--Requisito 2--
4. Si un estudiante obtiene un -0.1 en la institución educativa en el sistema
americano el grado numérico sería -2 por lo cual la letra sería Error.
5. Si un estudiante obtiene un 5.1 en la institución educativa en el sistema
americano el grado numérico sería 102 por lo cual la letra sería Error.
6. Si un estudiante obtiene un 2.5 en la institución educativa en el sistema
americano el grado numérico sería 50 por lo cual la letra sería F.
# Algoritmo
a)	Escribir algoritmo para cada requisito
--Requisito 1--
Entrada: nota_final.
Proceso: Evaluar con condicionales.
Salida: mensaje.
--Requisito 2--
Entrada: nota_final.
Proceso: Ejecutar formula para convertir en sistema de calificación americano y evaluar en condicionales.
Salida: letra_nota.

# Logro --> Programa