num_1=int(input("ingrese primer numero"))
num_2=int(input("ingrese segundo numero"))

elegir=0
while elegir != 8:
      opciones=int(input("""ingrese el numero de la operacion que desea realizar:
         \t 1)suma
        \t 2)resta
        \t 3)division
        \t.4 multiplicacion
        \t 5)potenciacion
        \t 6)raiz cuadrada"
        \t 7)cambiar numeros
        \t 8) SALIR"""))
elegir=int(input())
if elegir== 1:
  RESULTADO_SUMA = num_1 +num_2
  print(RESULTADO_SUMA)
elif elegir==2:
  RESULTADO_RESTA=num_1-num_2
  print(RESULTADO_RESTA)
elif elegir==3:
  RESULTADO_MULTIPLICACION=num_1 * num_2
  print(RESULTADO_MULTIPLICACION)
elif elegir==4:
    RESULTADO_DIVISION=num_1 /num_2
    print(RESULTADO_DIVISION)
elif elegir==5:
    BASE=int(input("INGRESE EL NUMERO DE LA BASE: "))
    EXPONENTE=int(input("INGRESA EXPONENTE: "))
    RESULTADO_POTENCIA  =pow(BASE,EXPONENTE)
    print(RESULTADO_POTENCIA)
elif elegir==6:
    DATO_RAIZCUADRADA =int(input("INGRESA NUMERO HACER EL CALCULO"))
    RESULTADO_RAIZCUADRADA = Math.sqrt(DATO_RAIZCUADRADA)
    print(RESULTADO_RAIZCUADRADA)
elif elegir==7:
    num_1=int(input("ingrese primer numero"))
    num_2=int(input("ingrese segundo numero"))
else:
    print("adios")


 

    
