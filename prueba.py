import json
import os

GreenGarden = "GreenGarden.json"

def cargar_datos():
    if os.path.exists(GreenGarden):
        with open(GreenGarden, "r") as file:
            return json.load(file)
    else:
        return []

def guardar_datos(ventas):
    with open(GreenGarden, "w") as file:
        json.dump(ventas, file, indent=4)
    print("Datos guardados correctamente")

def ingresar_venta(ventas):
    nombre = input("Ingrese el nombre del cliente: ")
    monto = input("Ingrese el monto: ")
    Id = input("Ingrese el número de la Id: ")
    producto = input("Ingrese el o los productos vendidos: ")

    venta = {
        "Nombre": nombre,
        "Monto": monto,
        "Id": Id,
        "Productos": producto
    }

    ventas.append(venta)
    print("Venta registrada correctamente")

def actualizar_registro(ventas):
    Id = input("Ingrese el número de Id de la venta a actualizar: ")
    for venta in ventas:
        if venta["Id"] == Id:
            monto = input("Ingrese el nuevo monto: ")
            nombre = input("Ingrese el nuevo nombre: ")
            producto = input("Ingrese el/los nuevos productos: ")
            venta["Monto"] = monto
            venta["Nombre"] = nombre
            venta["Productos"] = producto
            print("Actualización exitosa.")
            return
    print("Id no encontrada.")

def eliminar_registro(ventas):
    Id = input("Ingrese el número de Id de la venta a eliminar: ")
    for i, venta in enumerate(ventas):
        if venta["Id"] == Id:
            del ventas[i]
            print("Venta eliminada exitosamente")
            return
    print("Id no encontrada.")


def menu():
    ventas = cargar_datos()
    seguir = "si"
    
    while seguir == "si":
        print("Opciones:")
        print("1. Ingresar una venta")
        print("2. Actualizar una venta")
        print("3. Eliminar una venta")
        print("4. Guardar cambios")
        print("5. Salir")
        print("6. boleta")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ingresar_venta(ventas)
        elif opcion == "2":
            actualizar_registro(ventas)
        elif opcion == "3":
            eliminar_registro(ventas)
        elif opcion == "4":
            guardar_datos(ventas)
        elif opcion == "5":
            break
        elif opcion=="6":
            print("boleta",ventas)
        else:
            print("Opción no válida. Intente de nuevo.")
        
        seguir = input("¿Desea realizar otra operación? (si/no): ")
    

if __name__ == "__main__":
    menu()
