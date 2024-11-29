import random
import os

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validarNumero(self, numero):
        self.intentos += 1
        if numero < self.numero_secreto:
            return "Ihh, creo que en mayor"
        elif numero > self.numero_secreto:
            return "MMM talvez es menor"
        else:
            return "Le costo..."

    def registrarIntento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_partidas = []
        self.total_partidas = 0
        self.total_aciertos = 0

    def registrarPartida(self, intentos, ganado):
        self.historial_partidas.append({"intentos": intentos, "ganado": ganado})
        self.total_partidas += 1
        if ganado:
            self.total_aciertos += 1

    def mostrarEstadisticas(self):
        if self.total_partidas == 0:
            porcentaje_aciertos = 0
        else:
            porcentaje_aciertos = (self.total_aciertos / self.total_partidas) * 100
        print(f"Jugador: {self.nombre}")
        print(f"Partidas jugadas: {self.total_partidas}")
        print(f"Aciertos: {self.total_aciertos}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")

    def guardarEstadisticas(self):
        with open("estadisticas.txt", "w") as file:
            file.write(f"{self.nombre},{self.total_partidas},{self.total_aciertos}\n")
            for partida in self.historial_partidas:
                file.write(f"{partida['intentos']},{partida['ganado']}\n")

    def cargarEstadisticas(self):
        if os.path.exists("estadisticas.txt"):
            with open("estadisticas.txt", "r") as file:
                data = file.readlines()
                header = data[0].strip().split(",")
                self.nombre = header[0]
                self.total_partidas = int(header[1])
                self.total_aciertos = int(header[2])
                self.historial_partidas = []
                for line in data[1:]:
                    intentos, ganado = line.strip().split(",")
                    self.historial_partidas.append({"intentos": int(intentos), "ganado": ganado == "True"})

def mostrarMenu():
    print("\n--- Menú ---")
    print("1. Comenzar una nueva partida")
    print("2. Estadísticas del jugador")
    print("3. Salir del juego")

def main():
    print("¡Bienvenido a Adivinan el Número!")
    nombre_jugador = input("Introduce tu nombre: ")
    jugador = Jugador(nombre_jugador)
    jugador.cargarEstadisticas()
    
    while True:
        mostrarMenu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            juego = JuegoAdivinanza()
            print("Tengo un número del 1 al 100. ¡Intenta adivinarlo!")
            while True:
                intento = int(input("Cual cree que es?: "))
                resultado = juego.validarNumero(intento)
                print(resultado)
                if resultado == "Le costo!":
                    jugador.registrarPartida(juego.intentos, True)
                    break
        elif opcion == "2":
            jugador.mostrarEstadisticas()
        elif opcion == "3":
            jugador.guardarEstadisticas()
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
