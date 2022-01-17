class deber:
    def ejercicio2(self):   
        numero1_como_cadena = input("Escribe un número: ")
        numero2_como_cadena = input("Escribe el otro número: ")
     # convertir a flotantes
        numero1 = float(numero1_como_cadena)
        numero2 = float(numero2_como_cadena)
        if (numero1 < 0 and numero2 > 0) or (numero2 < 0 and numero1 > 0):
            resta = numero1 - numero2
            print("La resta es: {}".format(resta))
     # Si ambos son negativos
        elif numero1 < 0 and numero2 < 0:
             multiplicacion = numero1 * numero2
             print("El producto es: {}".format(multiplicacion))
     # Si son distintos
        elif numero1 != numero2:
             suma = numero1 + numero2
             print("La suma es: {}".format(suma))
             suma = 10 + 5 + 7
             resta = 10 - 5 - 7
             multiplicacion = 10 * 5 * 7
             division = 10 / 5 / 7
             print("Suma: " , suma ,  "\nResta: " , resta , "\nMultiplicación: " , multiplicacion , "\nDivisión: " , division)
    def ejercicio3(self):
        a=float(input("Primer número:"))
        b=int(input("Segundo número:"))
        c=a+b
        print("El resultado de la suma es", c)
    def ejercicio4(self):
        n1=int(input("Ingresá un número:"))
        n2=int(input("Ingresá otro número:"))
        suma=n1+n2
        print("Suman:", suma)
        n3=int(input("Ingresá un nuevo número:"))
        print("Multiplicación de la suma por el último número:",suma*n3)
    def ejercicio5(self):
        frase="Estoy programando"
        print(frase[0])
        i=6
        print(frase[i]) 
    def ejercicio6(self):
        cadena=input("Ingresá una frase:")
        longitud=len(cadena)
        print(longitud%2 == 0)
    def ejercicio7(self):
          lista = []
        # numero = int(input("Introduce un número en la lista:"))
        # while numero>=0:
	    #      lista.append(numero)
        #     for numero in lista:
	    #         print(numero," ",end="")
    def ejercicio8(self):
         def f(x: int)->bool:
            print('f:', x)
            return True
         def g(x: int)->bool:
             print('g:', x)
             return False     
    def ejercicio9(self):
        print("Caso 1 - f or f or f :")
        print(f(1) or f(2) or f(3))
        print("Caso 2 - f or f or g :")
        print(f(1) or f(2) or g(3))
        print("Caso 3 - g or f or g :")
        print(g(1) or f(2) or g(3))
        print("Caso 4 - g or g or g :")
        print(g(1) or g(2) or g(3))
    def ejercio10(self):
        print("Caso 1:", not f(1) and f(2))
        print(not f(1) and f(2))
        print("Caso 2:", not g(1) and f(2))
        print(not g(1) and f(2))
    def ejercicio11(self):
        nombre = input("¿Cómo te llamas? ")
        n = input("Introduce un número entero: ")
        print((nombre + "\n") * int(n))
    def imprimir_numeros_ascii(s):
         for i in s:
          print(ord(i))
          s = input("Ingrese string")
    def ejercicio12(self):
           N=input("tu nombre:")
           print("ahora estas en la matrix,  ",N)
           costo=float(input("costo de la cena:$"))
           servicio=costo*0.062
           propina=costo*0.1
           print("costo total de la comida:$ , costo+servicio+propina")
           dia=int(input("dia de nacimiento:"))
           mes=int(input("mes de tu nacimiento:"))
           año=int(input("año de tu nacimiento:"))
           print(dia,"/",mes,"/",año)
           fecha=int(input("fecha en DDMMAA:"))
           print(dia+"/"+mes+"/"+año)
           año= fecha%1000
           dia=fecha//100000
           mes=(fecha//1000)%100
           print(dia,"/",mes,"/",año)
           capacidad=float(input("capacidad del tanque:"))
           kmxl=float(input("rendimiento(km por litro):"))
           rrecorido=float(input("km totales a rrecorer:"))
           kmxtanque=capacidad*kmxl
           print("seran necesarios",rrecorido/kmxtanque)
    def ejercicio13(self):
        capacidadm2=4
        porcentajegradas=0.2
        porcentajespeciales=0.3
        porcentajecomunes=0.7
        dimensiones=float(input("dimensiones del estadio (en m2):"))
        personasengradas=int(input("cantidad de personas que caben en las gradas:"))
        porcentajeescenario=int(input("porcentaje que ocupa el escenario:"))
        m2gradas=dimensiones*porcentajegradas
        m2escenario=dimensiones*(porcentajeescenario/100)
        m2disponibles=dimensiones-m2gradas-m2escenario
        personastotales=(m2disponibles*4+personasengradas)
        print("caben",personastotales,"personas")
        precioentradacomun=float(input("precio entrada comun:"))
        precioentradaespecial=float(input("precio entrada especial:"))
        print("ingreso total de ventas",personastotales*precioentradaespecial +personastotales*porcentajecomunes*precioentradacomun)
        #declar el n=1000 para saber si es el ganador 
    def ejercicio14(self):
        num=int(input("N.de cliente: "))
        if num==1000:
            print("Ganastes un premio ")
     #ingresar un numero para saber si es mayor o menor 
    def ejercicio1(self):
        a=int(input("Ingrese un numero 1: "))
        b=int(input("Ingrese un numero 2: "))
        if a<b:
            print("El primero es menor")
        elif b<a:
            print("El segundo es menor")
        else:
            print("Son igual")
     #solicitar al usuario un dia de la semana 
    def ejercicio2(self):
        dia=input("Dia de la semana: ")
        if dia=="lunes":
            print("oh, no!")
        elif dia=="viernes":
            print("¡ya casi!")
        elif dia=="sabado" or dia=="domingo":
            print("Ahora si se puede descansar")
        else:
            print("A esperar el fin de semana!")        
     #Escribir un programa que dado un numero entero, muestre su valor absoluto
    def ejercicio15(self):
        num=int(input("Numero: "))
        if num<0:
            num=num*-1
        print("El valor absoluto es", num)
     #Solicitar al usuario que ingrese nombre de dos personas las cuales se almacena
     #en dos variables imprimir si el nombre si conciden con las msmas letras
    def ejercicio1(self):
        nombre1=input("Ingrese nombre: ")
        nombre2=input("Ingrese nombre: ")
        indice_final_nombre1=len(nombre1)-1
        indice_final_nombre2=len(nombre2)-1
        if nombre1[0]==nombre2[0] or nombre1[indice_final_nombre1]==nombre2[indice_final_nombre2] :
            print("cincidencia")
        else:
            print("No hay concidencia") 
     #crear un progrma en el que el usuario le permita elegir un candidato
    def ejercicio2(self):
        candidato=input("Candidato elegido: ")
        if candidato.upper()=="A":
            print("Usted ha votado por el partido rojo")
        elif candidato.upper()=="B":
            print("Usted ha votado por el partido azul")
        elif candidato.upper()=="C":
            print("Usted ha votado por el partido verde")
        else:
            print("Opcion erronea")    
     #Escribir un programa que solicite al usuario una letra y si es una vocal,
     #se debe validar que el usuario ingrese solo un caracter. Si ingresa un string
     #de mas informarle que no se puede procesar dato.       
    def ejercicio3(self):
        letra=input("Ingrese letra: ")
        if len(letra)!=1:
            print("Debe ser solo una letra")
        else:
            if letra.lower() in "aeiou":
                print("Es vocal")
            else:
                print("No es vocal")
     #hacer un programa que permita saber si un año es bisiesto.
     #para ser un año sea bisiesto debe ser divisible por 4 y no 
     #debe ser divisible por 100, excepto que tambien sea divisible por 400
    def ejercicio4(self):
        añio=int(input("Ingrese año: "))
        if añio %4 != 0:
            print("No es bisiesto.")
        else:
            if añio%100!=0 or añio%400 ==0:
                print("Es bisiesto")
            else:
                print("No es bisiesto")
     #Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. 
     # El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés para viajeros.
     # Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. 
     # Si el usuario ingresa un día de la semana inexistente o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. 
     # Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
     # Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará el porcentaje de aprobados.
     # Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
     # Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego imprimir el ingreso total en $.
    def ejercicio16(self):
        fecha=input("Fecha (día, DD/MM'): ")
        fecha=fecha.lower()
        diasemana=fecha[0:fecha.find(',')]
        dianro=int(fecha[fecha.find(',')+2:fecha.find("/")])
        mesnro=int(fecha[fecha.find('/')+1:])
        if dianro>31 or mesnro>12:
          print("Fecha incorrecta")
        else:
            if diasemana in "lunes,martes,miércoles":
               respuesta=input("¿Se tomaron exámenes? S/N: ")
               if respuesta.lower()=="s":
                aprobados=int(input("Cantidad de aprobados: "))
                reprobados=int(input("Cantidad de reprobados: "))
                print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
            elif diasemana=="jueves":
                 asistencia=int(input("Porcentaje de asistencia: "))
                 if asistencia>50:
                    print("Asistió la mayoría")
                 else:
                    print("No asistió la mayoría")
            elif diasemana=="viernes":
                if dianro==1 and (mesnro==1 or mesnro==7):
                   print("Nuevo ciclo")
                alumnos=int(input("Cantidad de alumnos: "))
                arancel=float(input("Arancel: $"))
                print("Ingreso total: $", alumnos*arancel)
            else:
              print("Fecha incorrecta")
        print("Fin del programa")
     #ejercicios con estructura for   
    def ejercicio17(self):    
        # for x in range (10):
        #     print(x)
        # for x in range (100,200):
        #     print(x)
        # for x in range (5,20,3):
        #     print(x)
        # n=int(input("Ingrese numero: "))
        # for x in range(n,n*2):
        #     print(x)
        # c=int(input("Cantidad de numero: "))
        # total=0
        # for variable in range(c):
        #     numero=int(input("Numero a sumar: "))
        #     total=total+numero
        # print("total de la suma: ",total)
        frase=input("Frase: ")
        cantidad=0
        for x in frase:
            if x in "aeiou":
                cantidad+=1
        print("cantidad de vocales:", cantidad)
     #Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.
    def ejercicio18(self):
        total=0
        for i in range(101):
            if i%3 == 0:
             total+=i
        print("Sumatoria de los múltiplos de 3:", total)
     #Dado un número entero positivo, mostrar su factorial. 
     #El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.      
    def ejercicio1(self):
       numero=int(input("Número:"))
       f=1
       if numero!=0:
          for i in range(1,numero+1):
              f=f*i
       print("Factorial:", f) 
     #  Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
     #  La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es 
     #  la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…           
    def ejercicio2(self):
        n1=0
        n2=1
        print(n1)
        print(n2)
        for i in range(8):
          n3=n1+n2
          print(n3)
          n1=n2
          n2=n3  
     #  Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. 
     #  Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
     # No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.    
    def ejercicio3(self):
        sumaNegativos=0            
        sumaPositivos=0
        cantidadPositivos=0
        for i in range(6):
            nro=int(input("Número: "))
            if nro>0:
               sumaPositivos=sumaPositivos+nro
               cantidadPositivos=cantidadPositivos+1
            else:
                sumaNegativos=sumaNegativos+nro
        print("Sumatoria de los negativos: ", sumaNegativos)
        if cantidadPositivos!=0:
           print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
        else:
           print("No se ingresaron números positivos")
     #Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”. 
     # La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes.
     # Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares. 
     # Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
     # Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. Escribir un programa que permita encriptar los 5 mensajes. 
     # El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento.
     # Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. 
     # Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
     # Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.
    def ejercicio19(self):
        alfabeto="abcdefghijklmnñopqrstuvwxyz"
        corrimiento=int(input("Corrimiento: "))
        for i in range(5):
            mensaje=input("Mensaje a encriptar: ")
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                   indice=alfabeto.find(caracter.lower())
                   indice=(indice+corrimiento)%27
                   encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter
            print("*** Mensaje encriptado: ", encriptado)
     #Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
     # Finalmente, mostrar la sumatoria de todos los números ingresados.       
    def ejercicio20(self):
        total=0
        nro=int(input("Número: "))
        while nro != 0:
            total+=nro
            nro=int(input("Número: "))
            print("Total:",total)
     #Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
     # Finalmente, mostrar la sumatoria de todos los números positivos ingresados.        
    def ejercicio1(self):
        positivos=0
        n=int(input("Número (0 para terminar): "))
        while n!=0:
              if n>0:
                positivos+=1
                n=int(input("Número (0 para terminar): "))
        print("Cantidad de positivos:", positivos)    
     # Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
     # Informar cuál fue el mayor número ingresado.  
    def ejercicio2(self):
        mayor=-1
        n=int(input("Número positivo:"))
        while n>=0:
            if n>mayor:
                mayor=n
                n=int(input("Número positivo:"))
        print("Mayor número ingresado:", mayor) 
     #Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.      
    def ejercicio3(self): 
         suma=0
         n=int(input("Número positivo:"))
         while n!=0:
            digito=n%10
            suma+=digito
            n=n//10
         print("Suma de los dígitos:", suma)
     # solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
     # La condición de corte es que se ingrese el número-1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares. 
    def ejercicio4(self):
        pares=0
        n=int(input("Número (-1 para terminar el programa): "))
        while n!=-1:
             if n%2 == 0:
               pares+=1
             suma=0
             while n!=0:
              digito=n%10
              suma+=digito
              n=n//10
             print("Suma de sus dígitos:", suma)
             n=int(input("Número (-1 para terminar el programa): "))
        print("Se ingresaron", pares, "números pares")
     #Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, 
     # la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
     # Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
     # Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.      
    def ejercicio21(self):
        total=0
        monto=float(input("Monto de una venta: $"))
        while monto!=0:
            if monto<0:
                print("Monto no válido.")
            else:
                  total+=monto
            monto=float(input("Monto de una venta: $"))
        if total>1000:
          total-=total*0.1
        print("Monto total a pagar: $", total)
     #Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. 
     # Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
     # Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.                    
    def ejercicio1(self):
        numero=int(input("numero: "))
        totalPares=0
        totalImpares=0
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:   
                ultimodigito=numero%10
                if ultimodigito%2==0:
                   pares+=1
                   totalPares+=1
                else:
                   impares+=1
                   totalImpares+=1
                numero=numero//10
            print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
            numero=int(input("Otro número: "))
        print("Total de dígitos pares:", totalPares)
        print("Total de dígitos impares:", totalImpares)
     # Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). 
     # Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. 
     # Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.
     # **Ejemplo de ejecución:**
     # Libro: Los 3 mosqueteros
     # Libro: Historia de 2 ciudades
     # Libro: /
     # Línea completa. Aparecen 2 dígitos numéricos.
     # Libro: 20000 leguas de viaje submarino
     # Libro: El señor de los anillos
     # Libro: /
     # Línea completa. Aparecen 5 dígitos numéricos.
     # Libro: 20 años después
     # Libro: *
     # Fin. Se leyeron 2 líneas completas.  
    def ejercicio2(self):
        DigitosEnLaLinea=0
        Cantlineas=0
        titulo=input("Titulo del libro: ")
        while titulo!="*":
            if titulo=="/":
                Cantlineas+=1
                print("Linea completa. Aparecen", DigitosEnLaLinea,"digitos")
            else:
                for caracter in titulo:
                    DigitosEnLaLinea+=1
            titulo=input("Titulo del libro: ")
        print("fin. Se leyeron",Cantlineas,"lineas")
     #Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. 
     # Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
    def ejercicio22(self):
        frase=input("Frase: ")
        frase=input("Frase: ").strip()
        cantidad=0
        len_p_mas_larga=0
        while len(frase) != 0:
            cantidad=cantidad+1
            i=frase.find(" ")
            if i != -1:
               palabra=frase[0:i]
               while i < len(frase) and frase[i] == " ":
                     i=i+1
               frase=frase[i:]
            else:
               palabra=frase
               frase=""
            if len(palabra) > len_p_mas_larga:
               len_p_mas_larga=len(palabra)
               p_mas_larga=palabra
        if cantidad > 0:
           print("Palabra más larga:", p_mas_larga)
        print("Cantidad de palabras:", cantidad)           
     # Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
     # A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. 
     # El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
     # Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.    
    def ejercicio23(self):
        while True:
            print("Opción 1 - comenzar programa")
            print("Opción 2 - imprimir listado")
            print("Opción 3 - finalizar programa")
            opcion=int(input("Opción elegida: "))
            if opcion==1:
                print("¡Comenzamos!")
            elif opcion==2:
                 print("Listado:")
                 print("Nadia, Esteban, Mariela, Fernanda")
            elif opcion==3:
                 print("Hasta la próxima")
                 break
            else:
               print("Opción incorrecta. Debe ingresar 1, 2 o 3")             
     #Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). 
     # Recorrer la frase, carácter a carácter, comparando con la letra buscada. 
     # Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar.
     # Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.   
    def ejercicio1(self):
        frase=input("Frase: ")
        l=input("Letra para buscar su posición: ")
        i=0
        while i!=len(frase):
            if l!=frase[i]:
               print("No se encontró en la posición", i)
               i+=1
               continue
            print("Se encontró en la posición", i)
            break
     #Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. 
     # Imprimir la cantidad de números primos ingresados.   
    def ejercicio24(self):
        cantidad=0
        n=int(input("Número: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                   primo=False
                   break
            if primo:
               cantidad+=1
            n=int(input("Número: "))
        print("primos: ", cantidad)
     #Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. 
     # Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.  
    def ejercicio1(self):
       añioInicio=int(input("Año inicial:"))
       añioFin=int(input("Año final:"))
       for añio in range(añioInicio, añioFin+1):
           if not añio%10==0:
             continue
           if not añio%4==0:
             continue
           if añio%100!=0 or añio%400==0:
              print(añio) 
     #Solicitar al usuario que ingrese su dirección email. 
     # Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. 
     # Una dirección se considerará válida si contiene el símbolo "@".
     #def ejercicio25(self):
       
# def validar(email):
#     caracterBuscado="@"
#     emailValido=False
#     for c in email:
#         if c==caracterBuscado:
#             return True
#     return False

# #programa principal
# direccion=input("Tu email: ")
# if validar(direccion):
#     print("Dirección válida")
# else:
#     print("Dirección inválida")
     # Solicitar números al usuario hasta que ingrese el cero. 
     # Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).   
    #def ejercicio26(self):
        
# def sumaDigitos(numero):
#     suma=0
#     while numero!=0:
#         digito=numero%10
#         suma=suma+digito
#         numero=numero//10
#     return suma
# sumatoria=0
# num=int(input("Número a procesar: "))
# while num!=0:
#     print("Suma:",sumaDigitos(num))
#     sumatoria=sumatoria+num
#     num=int(input("Número a procesar: "))
# print("Sumatoria:", sumatoria)
# print("Dígitos:", sumaDigitos(sumatoria))
# pass

def primo(num):
       for i in range(2,num):
           if num%i==0:           
              return False
           return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=suma+digito
      numero=numero//10
  return suma

#programa principal
mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
          mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))       
        
from re import X
from tkinter import Y

class deber:
    #Decidir si un numero es primo o no
    def ejercicio27 (self):
        def primo(numero):
            for i in range(2,numero):
                if numero%i==0:
                    return False
                return True
    numero=int(input("numero: "))
    if primo(numero): 
        print("es primo")
    else: 
        print("no es primo")
    #Realizar un programa que pida numeros al usuario, muiestre el factorial
    #de cada uno y luego la cantidad totalde numeros leidos.
    def ejercicio1 (self):
        def factorial():
            cantidad=0
            n=int(input("Numeros:"))
            while n!=-1:
                f=1
                if n!=0:
                    for i in range(1,n+1):
                        f=f*i
                print("factorial", f)
                cantidad+=1
                n=int(input("Numero: "))
                return cantidad
    #Realizar un programa que pida numeros positivos al usuario
    #muestre el numero cuya sumatoria de digitos fue mayor, y la cantidad de numeros
    #cuya sumatoria de digitos fue menor que 10.
    def ejercicio28 (self):
        cantidad=0
        mayor=-1
        numero=int(input("numero positivo:"))
        while numero>=0:
            sumaDigitos(numero)
            if sumaDigitos > mayor:
                mayor=sumaDigitos
                n_mayorsuma=numero
            if sumaDigitos < 10:
                cantidad+=1
                numero=int(input("numero positivo: "))
            print("sumatoria de digitos de",n mayorsuma,":",mayor)
            print("cantidad con sumatoria menor a 10:", cantidad)
    #Determine cual es la salida en pantalla si se ingresan los valores x=6, y=7:
    def ejercicio29 (self):
        def coordenadaZ(x,y):
            x=x+10
            y=y+15
            return x+y
        x=int(input("coordenada eje x:"))
        y=int(input("coordenada eje y:"))
        for i in range(3):
            z=coordenadaZ(x,y)
            x=x+1
            y=y+1
            print(x,".",y)
    #En el siguiente programa se debera imprimir el numero 2 si se le ingresan
    #como valores x=5, y=1.
    def ejercicio1 (self):
        def maximo(a,b):
            if x>y:
                return X
            else:
                return Y
        def minimo(a,b):
            if x<y:
                return X
            else:
                return Y
        x=int(input("un numero:"))
        y=int(input("otro numero:"))
        print(maximo(x-3, minimo(x+2, y-5)))     
    #Escribir una funcion que, dado un numero de DNI, retorne True si el numero
    #es valido y False si no lo es. Para que un numero de DNI sea valido debe tener entre
    #7 y 8 digitos.
    def ejercicio30 (self):
        def DNIvalido(dni):
            cantidad=0
            while dni!=0:
                cantidad=cantidad+1
                dni=dni//10
                return cantidad==7 or cantidad==0
    #Escribir una funcion que, dado un string, retorne la longitud de la
    #ultima palabra. Se considera que las palabras estan separadas por uno o mas espacios
    #Tambien podria haber espacios al principio o al final del string pasado por parametro.
    def ejercicio1 (self):
        def lenUltimaPalabra(frase):
            if len(frase)==0:
                return 0
            cantidad=0
            for i in range(len(frase)):
                if frase[i]!=' ':
                    cantidad+=1
                else:
                    if i<len(frase)-1 and frase[i+1]!=' ':
                        cantidad=0
                        return cantidad
    #Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacío.
    #Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1 nombre2 apellido. Si un socio tuviera más de un apellido, el usuario sólo ingresará uno.
    #Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
    #Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los primeros 3 dígitos de su DNI.
    def ejercicio31 (self):
        def lenUltimaPalabra(cadena):
            longitud=len(cadena)
            if longitud==0:
                return 0
            cantidad=0
            for i in range(longitud):
                if cadena[i]!=' ':
                    cantidad+=1
                else:
                    if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                        cantidad=0
                        return cantidad
                    def DNIvalido(dni):
                        cantidad=0
                        while dni!=0:
                            cantidad+=1
                            dni//=10
                            return cantidad==7 or cantidad==8
                        def primerosTresDigitos(numero):
                            while numero >= 1000:
                                numero = numero // 10
                                return numero
                            def obtenerIdentificador(nombre, dni):
                                nombre=nombre.strip()
                                id=nombre[:nombre.find(" ")]
                                id=id+str(lenUltimaPalabra(nombre))
                                id=id+str(primerosTresDigitos(dni))
                                return id
    #Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la 
    #primera letra de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados 
    #los demás caracteres. Precondición: el separador de palabras es el espacio: " ". 
    #Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor 
    #esperado ante distintos argumentos.
    def ejercicio32 (self):
        def titulo(cadena):
            def titulo(cadena):
                '''
                Recibe una cadena de caracteres y retorna una copia que tiene la
                primera letra de cada palabra en mayúsculas y el resto de las letras
                en minúsculas.
                >>> titulo('esto es una frase')
                'Esto Es Una Frase'
                >>> titulo('ESTO ES UNA FRASE')
                'Esto Es Una Frase'
                >>> titulo('palabra')
                'Palabra'
                >>> titulo('   esto es una frase')
                '   Esto Es Una Frase'
                >>> titulo('esto es una frase   ')
                'Esto Es Una Frase   '
                >>> titulo('esto   es   una   frase')
                'Esto   Es   Una   Frase'
                >>> titulo('')
                ''
                >>> titulo(' ')
                ' '
                >>> titulo('123')
                '123'
                >>> titulo('-1esto 2es 3una 4frase')
                '-1Esto 2Es 3Una 4Frase'
                >>> titulo('esto1 es2 una3 frase4---')
                'Esto1 Es2 Una3 Frase4---'
                '''
            nueva=""
            inicioPalabra=True              #indica el inicio de una palabra
            for caracter in cadena:
                if not caracter.isalpha():
                    nueva=nueva+caracter
                    inicioPalabra=True
                else:
                    if inicioPalabra:
                        nueva=nueva+caracter.upper()
                        inicioPalabra=False  #ya no es el inicio de una palabra 
                    else:
                        nueva=nueva+caracter.lower()
        return nueva
    #Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. Finalizar al ingresar el número 0, el cual no debe guardarse.
    #B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
    #C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
    #D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
    #E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
    def ejercicio33 (self):
         def sumatoria(lista):
        suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#A
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#B
print("Sumatoria de los números:", sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#C
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")
    #Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
    #-Agregar pasajeros a la lista de viajeros.
    #-Agregar ciudades a la lista de ciudades.
    #-Dado el DNI de un pasajero, ver a qué ciudad viaja.
    #-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
    #-Dado el DNI de un pasajero, ver a qué país viaja.
    #-Dado un país, mostrar cuántos pasajeros viajan a ese país.
    #-Salir del programa.
    def ejercicio34 (self):
         def agregarPasajeros(pasajeros):
        nombre=input("Nombre -x para cortar: ")
    while nombre!="x":
        dni=int(input("DNI: "))
        destino=input("Ciudad destino: ")
        pasajeros.append((nombre,dni,destino))
        nombre=input("Nombre -x para cortar: ")
    return pasajeros

def agregarCiudades(ciudades):
    ciudad=input("Ciudad -x para cortar: ")
    while ciudad!="x":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("Ciudad -x para cortar: ")
    return ciudades

def buscarCiudad(pasajeros, dni):
    for viaje in pasajeros:
        if viaje[1]==dni:
            return viaje[2]
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    cantidad=0
    for viaje in pasajeros:
        if viaje[2]==ciudad:
            cantidad+=1
    return cantidad

def buscarPaisDestino(pasajeros, ciudades, dni):
    buscada=buscarCiudad(pasajeros, dni)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

#programa principal
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")
    #Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
    #- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
    #- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
    #-Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
    def ejercicio35 (self):
        def cargarNombres(alumnos):
            nombre=input("Nombre: ")
    while nombre!="x":
          alumnos.add(nombre)
       nombre=input("Nombre: ")
    return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)
   #Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
   #[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
   #Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
   def ejercicio36 (self):
       def direcciones(ventas):
            domicilios=set()
            for venta in ventas:
                domicilios.add(venta[3])
            return domicilios
    #Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: "r":5, "%":3, "a":8, "9":1.
    #¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?
    def ejercicio37 (self):
    contadores={}
    for i in range(50):
        cadena=input("Cadena de caracteres: ")
        for caracter in cadena:
            if caracter not in contadores:
                contadores[caracter]=1
            else:
                contadores[caracter]+=1
    print("Frecuencia de cada carácter")
    for caracter, cantidad in contadores.items():
        print(caracter, ": ", cantidad)</code></pre>

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
contadores={}
alfabeto="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
print("Frecuencia de cada letra")
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)
   #Crear un programa para gestionar datos de los socios de un club, permitiendo:
   #-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
   #Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
   #Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
   #Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
   #-Informar cantidad de socios del club.
   #-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
   #-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
   #-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
   #-Imprimir el listado de socios completo.
   def ejercicio38 (self):
       def cargarSocios(socios):
        numero=int(input("Número de socio (0 para cortar): "))
        while numero!=0:
            nombre=input("Nombre y apellido: ")
            fecha=input("Fecha de ingreso (DDMMAAAA): ")
            cuota=input("¿Cuota al día? s/n: ")
            socios[numero]=[nombre,fecha,cuota.lower()=="s"]
            numero=int(input("Número de socio (0 para cortar): "))
   return socios

def modificarFecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numeroSocio(socios, nombre):
   for numero,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero
   return 0

def formatoFecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimirListado(socios):
   for numero,datos in socios.items():
       print("-Número:",numero)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formatoFecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=numeroSocio(socios_activos, nombre)
if numero in socios_activos:
    del socios_activos[numero]

imprimirListado(socios_activos)
    #Crear un programa donde acceda por nombre de variablese existentes a los datos de una lista
    def ejercicio39 (self):
        def cargardatos(diccionario):
            dni=int(input("dni:"))
            while dni!=0:
                nombre=input("nombre:")
                domicilio=input("domicilio:")
                telefono=int(input("telefono:"))
                diccionario(dni)=(nombre,domicilio,telefono)
                dni=int(input("dni:"))
            return diccionario
        def imprimirdatos(diccionario):
            for clave, valor in diccionario.items():
                print(dni, nombre, domicilio, telefono)       
