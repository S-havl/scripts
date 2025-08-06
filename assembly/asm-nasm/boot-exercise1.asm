[bits 16]        ;Definir 16 bits.
[org 0x7C00]     ;Cargar boot en el sector 0x7C00

start:            ;Funcion start
    call print_A ;Guarda direccion de la siguiente linea y llama a print_A
    call print_B ;Guarda direccion de jmp $ y llama a print_B
    jmp $        ;Bucle que salta encima de la linea infinitamente

print_A:         ;Funcion print_A
    mov ah, 0x0E ;Servicio teletipo de la BIOS
    mov al, 'A'  ;Digito o Caracter a imprimir
    int 0x10     ;Llamar a la BIOS para imprimir
    ret          ;Sacar direccion guardada y saltar a ella

print_B:         ;Funcion print_B
    mov ah, 0x0E ;Servicio teletipo de la BIOS
    mov al, 'B'  ;Digito o Caracter a imprimir
    int 0x10     ;Llamar a la BIOS para imprimir
    ret          ;Sacar direccion guardada y saltar a ella

times 510-($-$$) db 0 ;Llenar de ceros hasta llegar al 510 para boot
dw 0xAA55             ;Firma para indicar que es el bootloader
