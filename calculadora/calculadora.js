const calculadora = (num1, num2, operacion) => {

    let resultado = 0; 

    switch (operacion ) {
        case "suma":
            resultado = num1+num2
            break;
        case "resta":
            resultado = num1-num2
            break;
        case "multiplicacion":
            resultado = num1*num2
            break;
        case "division":
            resultado = num1/num2;
            break;
        default:
            resultado = "no esta esa operacion todavia"
            break;
    }

    return resultado
}

const prueba = calculadora(8, 2, "resta")

console.log(prueba)