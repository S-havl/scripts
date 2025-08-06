#include <stdio.h>

int main()
{
  float notas[5];
  float suma = 0;
  int i;

  for (i = 0; i < 5; i++) {
    printf("Ingrese la nota del estudiante %d: ", i + 1);
    scanf("%f", &notas[i]);
  }

  for (i = 0; i < 5; i++) {
    suma += notas[i];
  }

  float promedio = suma / 5;

  printf("El promedio de las notas ingresadas es: %.2f\n", promedio);

  return 0;
}
