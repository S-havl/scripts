#include <stdio.h>

int main(){
    int num;
    printf("Ingrese un número:");
    scanf("%d", &num);
    if (num % 2 == 0){
        printf("El número ingresado es par.");
    } else{
        printf("El número ingresado es inpar.");
    }
    return 0;
}