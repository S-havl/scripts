#include <stdio.h>
#include <string.h>
#include <ctype.h>

char* analizar_contraseña(const char* passwd){
  int longitud = strlen(passwd);
  int tiene_mayuscula = 0, tiene_minuscula = 0, tiene_numero = 0, tiene_simbolo = 0;
  
  if (longitud < 8) {
    return "La contraseña es muy débil, no cumple con la longitud mínima.\n";
  }

  for (int i = 0; passwd[i] != '\0'; i++) {
    if (isupper(passwd[i])) {
      tiene_mayuscula = 1;
    } else if (islower(passwd[i])) {
      tiene_minuscula = 1;
    } else if (isdigit(passwd[i])) {
      tiene_numero = 1;
    } else if (!isalnum(passwd[i])) {
      tiene_simbolo = 1;
    }
  }

  if (tiene_mayuscula && tiene_minuscula && tiene_numero && tiene_simbolo) {
    return "La contraseña es fuerte, cumple con todos los requisitos.\n";
  } else if (tiene_mayuscula && tiene_minuscula) {
    return "La contraseña es moderada, cumple con algunos requisitos.\n";
  } else {
    return "La contraseña es débil.\n";
  }
}

int main()
{
  char contraseña[50];

  while (1) {
    printf("Ingrese la contraseña a verificar: ");
    fgets(contraseña, 50, stdin);
    contraseña[strcspn(contraseña, "\n")] = 0;
    
    if (strlen(contraseña) > 17) {
      printf("La contraseña tiene más de 17 carácteres. Intente de nuevo.\n");
      continue;
    }
    printf("Iniciando verificación de contraseña...\n");
    char* contraseña_analizada = analizar_contraseña(contraseña);
    printf("Analisis finalizado: %s\n", contraseña_analizada);
    break;
  }
  return 0;
}
