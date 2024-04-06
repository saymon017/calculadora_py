def main():
    while True:
        # Inicialización de variables
        n1 = 0
        n2 = 0

        # ingrese los datos
        while True:
            try:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))
                break
            except ValueError:
                print("**ERROR:** Debes ingresar un número válido.")

        # Mostrar menú de opciones
        while True:
            print("""
            Dime, ¿qué quieres hacer?

            1) Sumar los dos números
            2) Restar los dos números
            3) Multiplicar los dos números
            4) Dividir los dos números
            5) Cambiar los números elegidos
            6) Apagar calculadora
            """)

            # Opción seleccionada
            try:
                opcion = int(input("Elige una opción: "))
            except ValueError:
                print("**ERROR:** Ingrese un valor válido (número del 1 al 6).")
                continue

            # Ejecutar la operación
            if opcion == 1:
                print(" ")
                print("RESULTADO: La suma de", n1, "+", n2, "es igual a", n1 + n2)
            elif opcion == 2:
                print(" ")
                print("RESULTADO: La resta de", n1, "-", n2, "es igual a", n1 - n2)
            elif opcion == 3:
                print(" ")
                print("RESULTADO: El producto de", n1, "*", n2, "es igual a", n1 * n2)
            elif opcion == 4:
                if n2 == 0:
                    print(" ")
                    print("**ERROR:** No se puede dividir por cero")
                else:
                    print(" ")
                    print("RESULTADO: La división de", n1, "/", n2, "es igual a", n1 / n2)
            elif opcion == 5:
                break
            elif opcion == 6:
                exit()
            else:
                print("Opción incorrecta")

if __name__ == "__main__":
    main()