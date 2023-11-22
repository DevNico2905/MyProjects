import sys, subprocess, os

Petro, Fico, Rodolfo, masculino, femenino = 0, 0, 0, 0, 0

candidatos = ["Petro #1", "Fico #2", "Rodolfo #3"]
ciudades = ["Bogotá", "Medellín", "Cali", "Bucaramanga", "Villavicencio"]
petro_x_cities = [0,0,0,0,0]
contador11, contador12, contador13, contador14, contador15 = 0, 0, 0, 0, 0
fico_x_cities = [0,0,0,0,0]
contador21, contador22, contador23, contador24, contador25 = 0, 0, 0, 0, 0
rodolfo_x_cities = [0,0,0,0,0]
contador31, contador32, contador33, contador34, contador35 = 0, 0, 0, 0, 0

def votar():
    global petro_x_cities, fico_x_cities, rodolfo_x_cities
    print("Registro de votantes\n")
    nombre = input("-Nombre: ")
    cedula = int(input("-Cédula: "))
    for i in range(5):
        print(f"({i + 1}) {ciudades[i]} | ", end="")
    ciudad = int(input("\n-Ciudad: "))

    if ciudad >= 1 and ciudad <=5:

        sexo = input("-Sexo (M) o (F): ")
        print("\nIngrese el número del candidato por el cual desea votar: ")
        print("[", candidatos[0],"|",candidatos[1],"|",candidatos[2],"]")
        voto = int(input("Candidato #"))

        if voto >= 1 and voto <= 3:

            if sexo == "M" or sexo == "m":
                global masculino
                masculino += 1
            elif sexo == "F" or sexo == "f":
                global femenino
                femenino += 1

            if voto == 1:
                global Petro
                Petro += 1
                print("\n¡Ha votado exitosamente!")
                input("Presione Enter para finalizar...")
                os.system("CLS")
            elif voto == 2:
                global Fico
                Fico += 1
                print("\n¡Ha votado exitosamente!")
                input("Presione Enter para finalizar...")
                os.system("CLS")
            elif voto == 3:
                global Rodolfo
                Rodolfo += 1
                print("\n¡Ha votado exitosamente!")
                input("Presione Enter para finalizar...")
                os.system("CLS")
            
            #Conteo votos por ciudad: Petro
            if voto == 1 and ciudad == 1:
                global contador11
                contador11 += 1
                petro_x_cities[0] = contador11
            elif voto == 1 and ciudad == 2:
                global contador12
                contador12 += 1
                petro_x_cities[1] = contador12
            elif voto == 1 and ciudad == 3:
                global contador13
                contador13 += 1
                petro_x_cities[2] = contador13
            elif voto == 1 and ciudad == 4:
                global contador14
                contador14 += 1
                petro_x_cities[3] = contador14
            elif voto == 1 and ciudad == 5:
                global contador15
                contador15 += 1
                petro_x_cities[4] = contador15

            #Conteo votos por ciudad: Fico
            if voto == 2 and ciudad == 1:
                global contador21
                contador21 += 1
                fico_x_cities[0] = contador21
            elif voto == 2 and ciudad == 2:
                global contador22
                contador22 += 1
                fico_x_cities[1] = contador22
            elif voto == 2 and ciudad == 3:
                global contador23
                contador23 += 1
                fico_x_cities[2] = contador23
            elif voto == 2 and ciudad == 4:
                global contador24
                contador24 += 1
                fico_x_cities[3] = contador24
            elif voto == 2 and ciudad == 5:
                global contador25
                contador25 += 1
                fico_x_cities[4] = contador25

            #Conteo votos por ciudad: Rodolfo
            if voto == 3 and ciudad == 1:
                global contador31
                contador31 += 1
                rodolfo_x_cities[0] = contador31
            elif voto == 3 and ciudad == 2:
                global contador32
                contador32 += 1
                rodolfo_x_cities[1] = contador32
            elif voto == 3 and ciudad == 3:
                global contador33
                contador33 += 1
                rodolfo_x_cities[2] = contador33
            elif voto == 3 and ciudad == 4:
                global contador34
                contador34 += 1
                rodolfo_x_cities[3] = contador34
            elif voto == 3 and ciudad == 5:
                global contador35
                contador35 += 1
                rodolfo_x_cities[4] = contador35

            

        else:
            print("\nEl número del candidato no es válido.")
            input("Presione Enter para reiniciar...")
            os.system("CLS")

    else:
        print("\nEl número de la ciudad no es válido.")
        input("Presione Enter para reiniciar...")
        os.system("CLS")
        
def total_votantes():
    global totalVotantes, Petro, Fico, Rodolfo
    totalVotantes = Petro + Fico + Rodolfo
    print("Personas que han votado:", totalVotantes)
    input("\nPresione Enter para finalizar...")
    os.system("CLS")

def total_x_candidatos():
    global Petro, Fico, Rodolfo, candidatos, resultados
    resultados = [Petro, Fico, Rodolfo]
    print("Número de votos por candidatos\n")
    for i in range(3):
        print(candidatos[i] + ":", resultados[i])
    input("\nPresione Enter para finalizar...")
    os.system("CLS")

def genero_votantes():
    global masculino, femenino
    print("Género de los votantes:\n")
    print(f"Hombres: {masculino}")
    print(f"Mujeres: {femenino}")
    input("\nPresione Enter para finalizar...")
    os.system("CLS")

def candidato_ganador():
    global Petro, Fico, Rodolfo
    if Petro > Fico and Petro > Rodolfo:
        print(f"El ganador es: Petro con {Petro} votos.\n")
    elif Fico > Petro and Fico > Rodolfo:
        print(f"El ganador es: Fico con {Fico} votos.\n")
    elif Rodolfo > Petro and Rodolfo > Fico:
        print(f"El ganador es: Rodolfo con {Rodolfo} votos.\n")
    elif Petro == 0 and Fico == 0 and Rodolfo == 0:
        print("¡No hubo ganador!\n")
    else:
        print("¡Empate!\nAl parecer habrá 2da vuelta.\n")


bandera = True
while bandera == True:
    print("Elecciones Presidenciales: Colombia\n")
    print("Menú")
    print(" 1) Votar.")
    print(" 2) Total votantes.")
    print(" 3) Número de votantes por candidatos.")
    print(" 4) Género de los votantes.")
    print(" 5) Resultados.\n")
    print("¿Qué opcion desea realizar? ", end="")
    decision_Usuario = int(input())
    os.system("CLS")

    match decision_Usuario:
        case 1:
            votar()
        case 2:
            total_votantes()
        case 3:
            total_x_candidatos()
        case 4:
            genero_votantes()
        case 5:
            bandera = False
            candidato_ganador()
            print("Mira los resultados:\n")
            print(f"        | {ciudades[0]} | {ciudades[1]} | {ciudades[2]} | {ciudades[3]} | {ciudades[4]} |")
            print(f"Petro   |", end="")
            print(f"    {petro_x_cities[0]}   |     {petro_x_cities[1]}    |   {petro_x_cities[2]}  |      {petro_x_cities[3]}      |       {petro_x_cities[4]}       |")
            print(f"Fico    |", end="")
            print(f"    {fico_x_cities[0]}   |     {fico_x_cities[1]}    |   {fico_x_cities[2]}  |      {fico_x_cities[3]}      |       {fico_x_cities[4]}       |")
            print(f"Rodolfo |", end="")
            print(f"    {rodolfo_x_cities[0]}   |     {rodolfo_x_cities[1]}    |   {rodolfo_x_cities[2]}  |      {rodolfo_x_cities[3]}      |       {rodolfo_x_cities[4]}       |")

            print("\n¡Hasta luego!")
print("¡Gracias por participar!")