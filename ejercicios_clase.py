#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    
    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    
    if numero_1 > numero_2:
        print("Numero 1 =",numero_1,"es mayor a","Numero 2 =",numero_2)
    else:
        print("Numero 2 =",numero_2,"es mayor a","Numero 1 =",numero_1)
    
    
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print("Numero 1 =",numero_1,"es positivo")
    else:
        if numero_1 < 0:
            print("Numero 1 =",numero_1,"es negativo")
        else:
            print("Numero 1 =",numero_1,"es cero")


    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 > 0 and numero_1 < 100:
        print("Numero 1 =",numero_1,"es mayor a 0 y menor a 100")
    else:
        print("Numero 1 =",numero_1,"no es mayor a 0 ni menor a 100")


    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if (numero_1 < 10) or (numero_2 > -2):
        print("Se cumple la condicion de que Numero 1 =",numero_1,"es menor a 10","o",numero_2,"es mayor a -2")
    else:
        print("No se cumple la condicion de que Numero 1 =",numero_1,"es menor a 10","o",numero_2,"es mayor a -2")

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print(texto_1,"es mayor que",texto_2)
    else:
        print(texto_2,"es mayor que",texto_1)


    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    texto_1_len = len(texto_1)
    texto_2_len = len(texto_2)

    if texto_1_len > texto_2_len:
        print(texto_1,"tiene mas letras que",texto_2)
    else:
        print(texto_2,"tiene mas letras que",texto_1)

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if texto_1[0] > texto_2[0]:
        print("La primera letra de",texto_1,"es mayor que la primera letra de",texto_2)
    else:
        print("la primera letra de",texto_2,"es mayor que la primera letra de",texto_1)

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    
    copia_texto_1 = texto_1  # Copia de la variable texto_1
    
    if texto_1 == copia_texto_1:
        print(texto_1,"es igual a",copia_texto_1)
    else:
        print(texto_1, "no es igual a",copia_texto_1)

     # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if copia_texto_1 != texto_2:
        print(copia_texto_1,"es diferente a",texto_2)
    else:
        print(copia_texto_1,"no es diferente a",texto_2)

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 3
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5) 
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"

    if numero_1 > 5:
        if numero_2 > 0:
            print("Resp=1")
        else:
            print("Resp=2")
    else:
        if numero_2 > 5:
            print("Resp=3")
        else:
            print("Resp=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 20

    if puntaje >= 90:
        print("A")
    else:
        if puntaje >= 80:
            print("B")
        else:
            if puntaje >= 70:
                print("C")
            else:
                if puntaje >= 60:
                    print("D")
                else:
                    if puntaje < 60:
                        print("F")
   

   
   
    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados



def ej4():
    # Ejemplos variables de texto

    numero_1 = 'abcdefg'
    numero_2 = 'abcdeff'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if numero_1 > numero_2:
        print(numero_1,"es mayor alfabeticamente que",numero_2)
    else:
        print(numero_2,"es mayor alfabeticamente que",numero_1)
    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
    
    # ------------------------ Inove -----------------------------------
    # Inove: ¿Cómo transfomar una variable texto (string) a número (int)
    # Aprovecho esta oportunidad para que practiques el pull-request con este comentario
    # Si quisiera convertir una variable texto a número debo usar el operador int()
    # tal como se hace cuando tomamos un valor de la consola
    # valor = int(input())  # Estamos tomando un valor de la consola y transformandolo a número
    # En este caso hubiera aplicado:
    
    # Variables tipo string
    texto_1 = '5'
    texto_2 = '7'
    
    # Variables tipo numércias
    numero_1 = int(texto_1)
    numero_2 = int(texto_2)
    
    # Si ahora verificamos en la ventana de "variables" de Visual Studio Code
    # veremos las variables nuevas creadas como enteros "int"
    # ------------------------ Inove -----------------------------------
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()

