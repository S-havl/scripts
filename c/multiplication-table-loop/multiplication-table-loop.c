#include <stdio.h>

int main(){
    int num;

    printf("Ingrese el número a ver la tabla de múltiplicar:");
    scanf("%d", &num);

    printf("Tabla de múltiplicar de %d es:\n", num);
    for (int i = 1; i <= 10; i++)
    {
        printf("%d x %d = %d\n", num, i, num * i);
    }
    
    return 0;
}