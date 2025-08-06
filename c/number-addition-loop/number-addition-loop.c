#include <stdio.h>

int main(){
    int usr_num;
    int total = 0;

    printf("Ingrese un número:");
    scanf("%d", &usr_num);
    
    for (int i = 1; i <= usr_num; i++)
    {
        total += i;
    }
    
    printf("La suma total de los números del 1 al %d es:%d", usr_num, total);
    return 0;
}