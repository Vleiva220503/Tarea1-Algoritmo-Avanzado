def main():
    # Pedir la cantidad de personas en el rango de 5 a 25
    while True:
        try:
            cantidad_personas = int(input("Ingrese la cantidad de personas (entre 5 y 25): "))
            if 5 <= cantidad_personas <= 25:
                break
            else:
                print("La cantidad de personas debe estar entre 5 y 25.")
        except ValueError:
            print("Ingrese un número válido.")

    personas = []

    # Calcular las deducciones para cada persona
    for i in range(cantidad_personas):
        print(f"Persona {i + 1}:")
        while True:
            try:
                salario = float(input("Ingrese el salario (entre 6000 y 360000): "))
                if 6000 <= salario <= 360000:
                    break
                else:
                    print("El salario debe estar entre 6000 y 360000.")
            except ValueError:
                print("Ingrese un salario válido.")

        inss = salario * 0.07
        ir = (salario - inss) * 0.12
        salario_con_deducciones = salario - (inss + ir)

        personas.append({
            "salario": salario,
            "inss": inss,
            "ir": ir,
            "salario_con_deducciones": salario_con_deducciones
        })

    # Mostrar la tabla de resultados individuales
    print("\nTabla de Resultados Individuales:")
    print(f"{'Persona':<8} | {'Salario':<15} | {'INSS':<8} | {'IR':<8} | {'Salario con Deducciones':<8}")
    print("-" * 62)
    for i, persona in enumerate(personas, start=1):
        print(f"{i:<8} | {persona['salario']:<15.2f} | {persona['inss']:.2f} | {persona['ir']:.2f} | {persona['salario_con_deducciones']:.2f}")

if __name__ == "__main__":
    main()
