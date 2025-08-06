# Network Packet Sniffer (sniff.c) - Basic Practice

This folder contains a simple C program, `sniff.c`, that functions as a basic network packet sniffer. It's designed as a practice exercise to understand packet capture and analysis at a fundamental level.

## Key Features

* **Raw Packet Capture**: Captures network traffic directly from the interface using `PF_PACKET` sockets. This allows for reading entire data link layer frames.
* **Basic Header Analysis**: Extracts and prints essential information from Ethernet, IP, TCP, and UDP headers. This involves understanding the structure of these headers and how to cast raw byte buffers to the appropriate C structs (`struct ethhdr`, `struct iphdr`, `struct tcphdr`, `struct udphdr`).
* **Network Byte Order Conversion**: Utilizes functions like `ntohs` (network to host short) and `inet_ntoa` (integer to network address) to correctly interpret multi-byte values (like port numbers) and IP addresses that are stored in network byte order.

## What I Learned from This Basic Script

Creating this simple packet sniffer provided valuable insights into:

* **Low-Level Network Programming**: Understanding how to open and interact with raw sockets (`SOCK_RAW`) to bypass the typical operating system network stack processing.
* **Packet Structure**: Gaining a hands-on understanding of the common network protocol headers (Ethernet, IP, TCP, UDP) and their respective fields, including their fixed offsets and variable lengths (like `ip_header->ihl` for IP header length).
* **Byte Order**: The importance of handling network byte order versus host byte order when parsing multi-byte data like port numbers and IP addresses.
* **C Structs and Pointers**: Using C structs to overlay on raw packet data and pointer arithmetic to navigate through different headers within a single packet.
* **Error Handling**: Basic error checking for socket creation and packet reception.

## Requirements

* C compiler (e.g., GCC)
* Linux environment (uses Linux-specific functions like `PF_PACKET` and `linux/if_ether.h` for raw sockets).

## How to Compile and Run

1.  **Compile**:
    ```bash
    gcc sniff.c -o sniff
    ```
2.  **Run (requires root privileges)**:
    ```bash
    sudo ./sniff
    ```
    The program will start displaying information about captured packets. Press `Ctrl+C` to stop it.

## Security Warning

This script opens raw sockets, which allows it to see all network traffic. For this reason, it requires `sudo` privileges to run. Use it with caution, as it can expose sensitive information. This is a practice tool and is not intended for use in production environments without significant modifications and additional security considerations.

## Purpose

This program serves as an educational practice to understand how networks operate at a low level, demonstrating how data can be extracted from packet headers.
