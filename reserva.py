def reservar(reservas):
    nombre = input("Nombre del comprador:").lower()
    if nombre in reservas:
        print("ERROR, ya tienes una reserva")
    else:
        clave_ingresada = input("Ingrese la clave para confirmar la reserva: ")
        if clave_ingresada == clave:
            reservas[nombre] = 1
            print(f"Reserva lista para {nombre}")
        else:
            print("Clave incorrecta, reserva no realizada")

def buscar(reservas):
    nombre = input("Nombre del comprador que busca: ").lower()
    if nombre in reservas:
        print(f"Reserva encontrada: {nombre} - {reservas[nombre]} par(es)")
        if reservas[nombre] == 1:
            vip = input("¿Desea agregar reserva VIP y tener 2 pares? (s/n): ")
            if vip.lower() == "s":
                reservas[nombre] = 2
                print(f"Reserva VIP lista. Ahora {nombre} tiene 2 pares ")
    else:
        print("No se encontró ninguna reserva con ese nombre!!")

def ver_stock(reservas, stock_total):
    reservados = sum(reservas.values())
    disponibles = stock_total - reservados
    print("Pares reservados:", reservados)
    print("Pares disponibles:", disponibles)

def menu():
    reservas = {}
    stock_total = 20
    while True:
        print("****TOTEM RESERVA STRIKE****")
        print("1. Reservar zapatillas")
        print("2. Buscar zapatillas reservadas")
        print("3. Ver stock de reservas")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            reservar(reservas)
        elif opcion == "2":
            buscar(reservas)
        elif opcion == "3":
            ver_stock(reservas, stock_total)
        elif opcion == "4":
            print("Programa terminado")
            break
        else:
            print("Opción inválida")

clave = "EstoyEnListaDeReserva"
menu()
