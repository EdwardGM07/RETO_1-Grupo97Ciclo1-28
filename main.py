""" Edward Camilo Gonzalez Monje, 
edwardcamilo2020@gmail.com 
Grupo 97 - ciclo 1,
"""

#Funcion 1
def determinar_notificacion(nota_final):

  #Metodo para decirle al estudiante si gana||recupera||pierde||Error a través de operadores logicos y comparadores
  
  if nota_final >= 3.0 and nota_final<=5.0:
    mensaje = "gana"
  elif nota_final < 3.0 and nota_final >= 2.2:
    mensaje = "recupera"
  elif nota_final < 2.2 and nota_final>=0.0:
    mensaje = "pierde"
  else: 
      mensaje="Error!!"
    
  #devuelve el resultado
  return mensaje

#==================================================
#Funcion 2
def conversion_sistema_americano(nota_final):

   #Metodo para decirle al estudiante su nota en Sistema de Calificación Americano A||B||C||D||F||Error a través de operadores logicos y comparadores
  
  grado_numerico= ((nota_final*100)/5)
  #Convierte de Sistema de Calificación Colombiano a Sistema de Calificación Americano

  if grado_numerico >= 90 and grado_numerico<=100:
    letra_nota="A"
  elif grado_numerico < 90 and grado_numerico >= 80:
    letra_nota="B"
  elif grado_numerico < 80 and grado_numerico >= 70:
    letra_nota="C"
  elif grado_numerico < 70 and grado_numerico >= 69:
    letra_nota="D"
  elif grado_numerico < 69 and grado_numerico>=0:
    letra_nota="F"
  else: 
      letra_nota="Error!!"

 #devuelve el resultado 
  return letra_nota

# recuerda correr donde dice test <-- aparece como un chulo parte izquierda inferior y usar correctamente los tipos de datos float y str
