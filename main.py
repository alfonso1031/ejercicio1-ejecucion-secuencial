import time


def realizar_tarea(nombre, segundos):
    print(f"Comienza: {nombre}")
    time.sleep(segundos)
    print(f"Termina: {nombre}")


def main():
    inicio = time.perf_counter()

    print("Preparación secuencial del desayuno")
    realizar_tarea("Preparar café", 2)
    realizar_tarea("Tostar el pan", 1)
    realizar_tarea("Cocinar los huevos", 3)

    tiempo_total = time.perf_counter() - inicio
    print(f"Desayuno listo. Tiempo total: {tiempo_total:.2f} segundos")


if __name__ == "__main__":
    main()
