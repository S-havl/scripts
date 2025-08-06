#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <errno.h>

void scan_ports(const char *ip, int puerto_inicial, int puerto_final){
  struct sockaddr_in target;
  int sock, result;

  for (int port = puerto_inicial; port <= puerto_final; port++) {
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
      perror("Error al crear el socket.");
      continue;
    }

    memset(&target, 0, sizeof(target));
    target.sin_family = AF_INET;
    target.sin_addr.s_addr = INADDR_ANY;
    target.sin_port = htons(port);
    if (inet_pton(AF_INET, ip, &target.sin_addr) <= 0) {
      perror("Error al convertir la IP.");
      close(sock);
      continue;
    } 

    result = connect(sock, (struct sockaddr *)&target, sizeof(target));

    if (result < 0) {
      printf("No se pudo conectar al puerto %d\n", port);
    } else {
      printf("Conexión exitosa al puerto %d\n", port);
    }

    close(sock);
  }

}

int main(int argc, char *argv[]){
  if (argc != 4) {
    printf("Uso: %s <IP> <Puerto_inicial> <Puerto_final>\n", argv[0]);
    return 1;
  }

  char *ip = argv[1];
  int puerto_inicial = atoi(argv[2]);
  int puerto_final = atoi(argv[3]);
  
  if (puerto_inicial < 1 || puerto_final > 65535 || puerto_inicial > puerto_final) {
    printf("Rango de puertos inválidos. Los puertos deben estar entre 1 a 65535 y el puerto inicial no debe ser mayor al puerto final.\n");
    return 1;
  }

  scan_ports(ip, puerto_inicial, puerto_final);

  return 0;
}
