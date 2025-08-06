#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <netinet/udp.h>
#include <sys/socket.h>
#include <linux/if_ether.h>
#include <unistd.h>

void procces_packet(unsigned char *buffer, int size)
{
  printf("--------------------------------\n");
  printf("Package received correctly.\n");
  printf("--------------------------------\n");
  printf("Processing package : %d bytes.\n", size);
  
  struct ethhdr *eth_header = (struct ethhdr *) buffer;
  printf("Destination MAC address: %02x:%02x:%02x:%02x:%02x:%02x\n",
           eth_header->h_dest[0], eth_header->h_dest[1], eth_header->h_dest[2],
           eth_header->h_dest[3], eth_header->h_dest[4], eth_header->h_dest[5]);
  printf("Source MAC address: %02x:%02x:%02x:%02x:%02x:%02x\n",
           eth_header->h_source[0], eth_header->h_source[1], eth_header->h_source[2],
           eth_header->h_source[3], eth_header->h_source[4], eth_header->h_source[5]);
  
  
  struct iphdr *ip_header = (struct iphdr *)(buffer + sizeof(struct ethhdr));
  int ip_header_len = ip_header->ihl * 4;
  printf("Source IP: %s\n", inet_ntoa(*(struct in_addr *)&ip_header->saddr));
  printf("Destination IP: %s\n", inet_ntoa(*(struct in_addr *)&ip_header->daddr));

  if (ip_header->protocol == IPPROTO_TCP) {
    struct tcphdr *tcp_header = (struct tcphdr *)(buffer + sizeof(struct ethhdr) + ip_header_len);
    printf("TCP source port: %d\n", ntohs(tcp_header->source));
    printf("TCP destination port: %d\n", ntohs(tcp_header->dest));
  } else if (ip_header->protocol == IPPROTO_UDP) {
    struct udphdr *udp_header = (struct udphdr *)(buffer + sizeof(struct ethhdr) + ip_header_len);
    printf("UDP source port: %d\n", ntohs(udp_header->source));
    printf("UDP destination port: %d\n", ntohs(udp_header->dest));
  } else {
    printf("Unknown protocol.\n");
    printf("Unknown port of origin.\n");
    printf("Unknown destination port.\n");
  }
}

int main(int argc, char *argv[])
{
  int capture_fd;
  unsigned char *buffer = (unsigned char *)malloc(65536);
  
  capture_fd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
  if (capture_fd == -1) {
    perror("Error creating socket.");
    exit(EXIT_FAILURE);
  }

  printf("Capturing packets...\n");

  while (1) {
    ssize_t packet_size = recvfrom(capture_fd, buffer, 65536, 0, NULL, NULL);
    if (packet_size == -1) {
      perror("Error receiving package.");
      return 1;
    }

    procces_packet(buffer, packet_size);
  }
  
  close(capture_fd);
  free(buffer);
  return 0;
}
