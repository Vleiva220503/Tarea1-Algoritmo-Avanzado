function calcularSalario() {
    // Pedir cantidad de personas en el rango de 5 a 25
    let cantidadPersonas;
    do {
        cantidadPersonas = parseInt(prompt("Ingrese la cantidad de personas (entre 5 y 25):"));
    } while (isNaN(cantidadPersonas) || cantidadPersonas < 5 || cantidadPersonas > 25);

    // Inicializar variables para almacenar los totales
    let totalINSS;
    let totalIR;
    let totalSalarioDeducciones;

    // Calcular para cada persona
    for (let i = 1; i <= cantidadPersonas; i++) {
        // Pedir salario en el rango de 6000 a 360000
        let salario;
        do {
            salario = parseFloat(prompt(`Ingrese el salario de la persona ${i} (entre 6000 y 360000):`));
        } while (isNaN(salario) || salario < 6000 || salario > 360000);

        // Calcular INSS y IR
        const inss = salario * 0.07;
        const ir = (salario - inss) * 0.12;
        const salarioTotalDeducciones = salario - (inss + ir);

        // Acumular totales
        totalINSS += inss;
        totalIR += ir;
        totalSalarioDeducciones += salarioTotalDeducciones;
    }

    // Mostrar resultados
    console.log(`Total INSS: ${totalINSS.toFixed(2)}`);
    console.log(`Total IR: ${totalIR.toFixed(2)}`);
    console.log(`Total Salario con Deducciones: ${totalSalarioDeducciones.toFixed(2)}`);
}

// Llamar a la función para comenzar el cálculo
calcularSalario();
