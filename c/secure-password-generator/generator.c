#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generar_contraseña(int longitud, int incluir_mayusculas, int incluir_minusculas, int incluir_digitos, int incluir_simbolos)
{
  const char mayusculas[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const char minusculas[] = "abcdefghijklmnopqrstuvwxyz";
  const char digitos[] = "123456789";
  const char simbolos[] = "!@#$%^&*()-_=+[]{}|;:,.<>?/";
  
  char caracteres_posibles[256] = {0};
  int idx = 0;
  
  if (incluir_mayusculas) {
    for (int i = 0; mayusculas[i] != '\0'; i++) {
      caracteres_posibles[idx++] = mayusculas[i];
    }
  }
  
  if (incluir_minusculas) {
    for (int i = 0; minusculas[i] != '\0'; i++) {
      caracteres_posibles[idx++] = minusculas[i];
    }
  }

  if (incluir_digitos) {
    for (int i = 0; digitos[i] != '\0'; i++) {
      caracteres_posibles[idx++] = digitos[i];
    }
  }

  if (incluir_simbolos) {
    for (int i = 0; simbolos[i] != '\0'; i++) {
      caracteres_posibles[idx++] = simbolos[i];
    }
  }

  if (idx == 0) {
    printf("No se seleccionaron caracteres válidos.\n");
    return;
  }
  
  srand(time(NULL));
  printf("Contraseña aleatoria: ");
    for (int i = 0; i < longitud; i++) {
        char caracter_aleatorio = caracteres_posibles[rand() % idx];
        printf("%c", caracter_aleatorio);
    }
    printf("\n");
}

int main()
{
  int longitud;
  int incluir_mayusculas, incluir_minusculas, incluir_digitos, incluir_simbolos;

  printf("¿Cuántos caracteres debe tener la contraseña? ");
  scanf("%d", &longitud);

  printf("¿Incluir mayúsculas? (1 para si, 0 para no): ");
  scanf("%d", &incluir_mayusculas);

  printf("¿Incluir minúsculas? (1 para si, 0 para no): ");
  scanf("%d", &incluir_minusculas);

  printf("¿Incluir digitos? (1 para si, 0 para no): ");
  scanf("%d", &incluir_digitos);

  printf("¿Incluir simbolos? (1 para si, 0 para no): ");
  scanf("%d", &incluir_simbolos);

  generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_digitos, incluir_simbolos);

  return 0;
}










