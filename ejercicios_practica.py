#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    numero_1 = int(input("Ingrese el primer número:\n"))

    numero_2 = int(input("Ingrese el segundo número:\n"))

    resta = numero_1 - numero_2

    if resta > 0:
      print("El resultado de la diferencia entre",numero_1,"y",numero_2,"es positivo")
    elif resta < 0:
      print("El resultado de la diferencia entre",numero_1,"y",numero_2,"es negativo")
    elif resta == 0:
      print("El resultado de la diferencia entre",numero_1,"y",numero_2,"es cero")


def ej2():
    # Ejercicios de práctica con números

    numero_1 = int(input("Ingrese el primer número:\n"))

    numero_2 = int(input("Ingrese el segundo número:\n"))

    numero_3 = int(input("Ingrese el tercer número:\n"))

    if numero_1 % 2 == 0:
      print(numero_1,"es par")
    else:
      print(numero_1,"es impar")

    if numero_2 % 2 == 0:
      print(numero_2,"es par")
    else:
      print(numero_2,"es impar")

    if numero_3 % 2 == 0:
      print(numero_3,"es par")
    else:
      print(numero_3,"es impar")

  

def ej3():
    # Ejercicios de práctica con números

    numero_1 = 33
    numero_2 = 47
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2
    potencia = numero_1 ** numero_2
    
    operador = str(input("Ingrese el simbolo de la operacion que desea ejecutar:\n"))

    if operador == "+":
      print("El resultado de la suma entre",numero_1,"y",numero_2,"es",suma)
    
    elif operador == "-":
      print("El resultado de la resta entre",numero_1,"y",numero_2,"es",resta)

    elif operador == "*":
      print("El resultado de multiplicar",numero_1,"y",numero_2,"es",multiplicacion)
    
    elif operador == "/":
      print("El resultado de dividir",numero_1,"dividido",numero_2,"es",division)

    elif operador == "**":
      print("El resultado de",numero_1,"elevado a la",numero_2,"es",potencia)
  

def ej4():
    # Ejercicios de práctica con cadenas
    
    palabra_1 = str(input("Ingrese la primera palabra:\n"))
    
    palabra_2 = str(input("Ingrese la segunda palabra:\n"))

    palabra_3 = str(input("Ingrese la tercera palabra:\n"))

    tipo_orden = int(input("Ingrese '1' para ordenar alfabeticamente o '2' para ordenar segun cantidad de letras: "))

    if tipo_orden == 1:
      
      if palabra_1 > palabra_2 and palabra_1 > palabra_3 and palabra_2 > palabra_3:
        print(palabra_1,palabra_2,palabra_3)
      
      elif palabra_1 > palabra_2 and palabra_1 > palabra_3 and palabra_3 > palabra_2:
        print(palabra_1,palabra_3,palabra_2)

      elif palabra_2 > palabra_1 and palabra_2 > palabra_3 and palabra_1 > palabra_3:
        print(palabra_2,palabra_1,palabra_3)

      elif palabra_2 > palabra_1 and palabra_2 > palabra_3 and palabra_3 > palabra_1:
        print(palabra_2,palabra_3,palabra_1)

      elif palabra_3 > palabra_2 and palabra_3 > palabra_1 and palabra_1 > palabra_2:
        print(palabra_3,palabra_1,palabra_2)
      
      elif palabra_3 > palabra_2 and palabra_3 > palabra_1 and palabra_2 > palabra_1:
        print(palabra_3,palabra_2,palabra_1)

    elif tipo_orden == 2:

      if (len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3)
          and len(palabra_2) > len(palabra_3)):
        print(palabra_1,palabra_2,palabra_3)
      
      elif (len(palabra_1) >= len(palabra_2) and len(palabra_1) >= len(palabra_3)
            and len(palabra_3) >= len(palabra_2)):
        print(palabra_1,palabra_3,palabra_2)

      elif (len(palabra_2) >= len(palabra_1) and len(palabra_2) >= len(palabra_3)
            and len(palabra_1) >= len(palabra_3)):
        print(palabra_2,palabra_1,palabra_3)

      elif (len(palabra_2) >= len(palabra_1) and len(palabra_2) >= len(palabra_3)
            and len(palabra_3) >= len(palabra_1)):
        print(palabra_2,palabra_3,palabra_1)

      elif (len(palabra_3) >= len(palabra_2) and len(palabra_3) >= len(palabra_1)
            and len(palabra_1) >= len(palabra_2)):
        print(palabra_3,palabra_1,palabra_2)
      
      elif (len(palabra_3) >= len(palabra_2) and len(palabra_3) >= len(palabra_1)
            and len(palabra_2) >= len(palabra_1)):
        print(palabra_3,palabra_2,palabra_1)

    







def ej5():
    # Ejercicios de práctica con números
       
    t_1 = int(input("Ingrese la temperatura 1:\n"))
    t_2 = int(input("Ingrese la temperatura 2:\n"))
    t_3 = int(input("Ingrese la temperatura 3:\n"))

    if t_1 > t_2 and t_1 > t_3:
      print("La temperatura de mayor °C es",t_1)
    elif t_2 > t_3 and t_2 > t_1:
      print("La temperatura de mayor °C es",t_2)
    elif t_3 > t_2 and t_3 > t_1:
      print("La temperatura de mayor °C es",t_3)

    if t_1 < t_2 and t_1 < t_3:
      print("La temperatura de menor °C es",t_1)
    elif t_2 < t_3 and t_2 < t_1:
      print("La temperatura de menor °C es",t_2)
    elif t_3 < t_2 and t_3 < t_1:
      print("La temperatura de menor °C es",t_3)

    suma = t_1 + t_2 + t_3
    promedio = suma / 3
    print("El promedio de las tres temperaturas ingresadas es",promedio)

    



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
