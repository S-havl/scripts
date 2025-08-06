#include <stdio.h>

int main(){
    int a, b;
    printf("Ingrese dos números:");
    scanf("%d, %d", &a, &b);
    int suma = a + b;
    int resta = a - b;
    int multiplicacion = a * b;
    int division = a / b;
    printf("suma total:%d\n", suma);
    printf("Resta total:%d\n", resta);
    printf("Múltiplicación:%d\n", multiplicacion);
    printf("División:%d\n", division);
    return 0;
}

