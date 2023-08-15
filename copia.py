def solicitar_numero(entrada_msg, error_msg, rango):
    while True:
        try:
            numero = float(input(entrada_msg))
            if rango[0] <= numero <= rango[1]:
                return numero
            else:
                print(error_msg)
        except ValueError:
            print("Ingrese un número válido.")

def solicitar_nombre(entrada_msg):
    while True:
        nombre = input(entrada_msg)
        if nombre.isalpha():
            return nombre
        else:
            print("Ingrese un nombre válido (solo letras).")

def calcular_deducciones(nombre, salario):
    inss = salario * 0.07
    ir = (salario - inss) * 0.12
    salario_con_deducciones = salario - (inss + ir)
    return {
        "nombre": nombre,
        "salario": salario,
        "inss": inss,
        "ir": ir,
        "salario_con_deducciones": salario_con_deducciones
    }

def main():
    cantidad_personas = solicitar_numero(
        "Ingrese la cantidad de personas (entre 5 y 25): ", 
        "La cantidad de personas debe estar entre 5 y 25.", 
        (5, 25))

    personas = []
    for i in range(int(cantidad_personas)):
        print(f"\nPersona {i + 1}:")
        nombre = solicitar_nombre("Ingrese el nombre: ")
        salario = solicitar_numero(
            "Ingrese el salario (entre 6000 y 360000): ", 
            "El salario debe estar entre 6000 y 360000.", 
            (6000, 360000))
        personas.append(calcular_deducciones(nombre, salario))

    print("\nTabla de Resultados:")
    print(f"{'Nombre':<15} | {'Salario':<12} | {'INSS':<8} | {'IR':<8} | {'Salario con Deducciones':<8}")
    print("-" * 75)
    for i, persona in enumerate(personas, start=1):
        print(f"{persona['nombre']:<15} | {persona['salario']:.2f} | {persona['inss']:.2f} | {persona['ir']:.2f} | {persona['salario_con_deducciones']:.2f}")
    print()

if __name__ == "__main__":
    main()
