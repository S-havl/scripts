#include <stdio.h>

struct Estudiante {
  char Nombre[50];
  int Edad;
  float Nota;
};

int main(){
  struct Estudiante estudiante;

  printf("Ingrese el nombre del estudiante: ");
  scanf("%49s", estudiante.Nombre);
  printf("Ingrese la edad del estudiante: ");
  scanf("%d", &estudiante.Edad);
  printf("Ingrese la nota del estudiante: ");
  scanf("%f", &estudiante.Nota);

  printf("Información del estudiante:\n");
  printf("Nombre: %s\n", estudiante.Nombre);
  printf("Edad: %d años\n", estudiante.Edad);
  printf("Nota: %.2f\n", estudiante.Nota);

  return 0;
}
