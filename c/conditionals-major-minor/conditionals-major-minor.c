#include <stdio.h>

int main(){
    int a, b, c;
    printf("Ingrese 3 números:");
    scanf("%d %d %d", &a, &b, &c);
    if (a >= b && a >= c)
    {
        printf("El número mayor es:%d\n", a);
    } else if (b >= a && b >= c)
    {
        printf("El número mayor es:%d\n", b);
    } else
    {
        printf("El número mayor es:%d\n", c);
    }

    if (a <= b && a <= c)
    {
        printf("El número menor es:%d", a);
    } else if (b <= a && b <= c)
    {
        printf("El número menos es:%d", b);
    } else
    {
        printf("El número menor es:%d", c);
    }
    
    return 0;
}