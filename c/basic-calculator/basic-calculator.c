#include <stdio.h>

float sumar(float a, float b){
    return a + b;
}

float restar(float a, float b){
    return a - b;
}

float multiplicar(float a, float b){
    return a * b;
}

float dividir(float a, float b){
    if (b != 0)
    {
        return a / b;
    } else
    {
        printf("No se puede dividir por 0.");
        return -1;
    }  
}

int main(){
    int operacion;
    float num1, num2, resultado;

    printf("Selecione la operación que desea realizar:\n");
    printf("1. Sumar\n");
    printf("2. Restar\n");
    printf("3. Múltiplicar\n");
    printf("4. Dividir\n");
    scanf("%d", &operacion);

    printf("Ingrese el primer número: ");
    scanf("%f", &num1);
    printf("Ingrese el segundo número: ");
    scanf("%f", &num2);

    switch (operacion)
    {
    case 1:
        resultado = sumar(num1, num2);
        printf("El resultado de la suma es: %.2f\n", resultado);
        break;
    case 2:
        resultado = restar(num1, num2);
        printf("El resultado de la resta es: %.2f\n", resultado);
        break;
    case 3:
        resultado = multiplicar(num1, num2);
        printf("El resultado de la multiplicación es: %.2f\n", resultado);
        break;
    case 4:
        resultado = dividir(num1, num2);
        if (resultado != -1)
        {
            printf("El resultado de la división es: %.2f\n", resultado);
        }
        break;
    default:
        printf("Operación no válida.\n");
        break;
    }
    return 0;
}