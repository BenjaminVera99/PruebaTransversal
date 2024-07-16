import random,csv

sueldosTtotales = []
Trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def Sueldosytrabajadores():
    for nombre in Trabajadores:
        SueldoRandom = random.randint(300000,2500000)
        print(f"Trabajador: {nombre} tiene sueldo de: {SueldoRandom}")
        sueldosTtotales.append(nombre)
        sueldosTtotales.append(SueldoRandom)




def ClasiSueldos():
    
    print(f"Sueldos Menores a $800.000 Totales:")

    print(f"Sueldos entre $800.000 y $2.000.000 Totales:")
    
    print(f"Sueldos Superiores a $2.000.000 Totales:")
    
    print(f"Total de Todos los Sueldos:")

def estadisticas():
    print(f"Sueldo mas Alto:")
    print(f"Sueldo mas Bajo:")
    print(f"Promedio de Sueldo:")
    print(f"Media Geometrica:")



while True:
    print("-"*30)
    print("1.-Asignar Sueldos Aleatorios")
    print("2.-Clasificar Sueldos")
    print("3.-Ver Estadisticas.")
    print("4.-Reporte de Sueldos")
    print("5.-Salir del Programa.")
    print("-"*30)
    try: 
        opc=int(input("Ingrese una opcion>:"))
        if opc >=1 and opc <=5:
            match opc:
                case 1:
                    print("Asignando Sueldos Aleatorios a los Trabajadores....")
                    (Sueldosytrabajadores())
                case 2:
                    (ClasiSueldos())
                
                case 3:
                    estadisticas()
                    
                case 4:
                    print("")
                
                
                
                case 5:
                    print("Finalizando Programa...")
                    print("Desarrollado por Benjamin Vera.")
                    print("RUT 21.173.956-8")
                    break
        else:
            print("Ingrese una opcion valida.")
    except ValueError:
        print("Solo se deben ingresar Numeros.")