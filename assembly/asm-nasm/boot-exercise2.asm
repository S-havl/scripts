[BITS 16]         ;Define 16 bits
[org 0x7C00]      ;El bootloader se carga en el primer sector (direccion)

_start:           ;Funcion _start
    ;Llamar a la funcion _print_S 5 veces
    call _print_S
    call _print_S
    call _print_S 
    call _print_S
    call _print_S
    jmp $         ;Saltar en el mismo sitio (bucle) 

_print_S:         ;Funcion _print_S
    mov ah, 0x0E  ;Servicio teletipo de BIOS
    mov al, 'S'   ;Caracter a imprimir
    int 0x10      ;Llamar a la BIOS para imprimir
    ret           ;Sacar la direccion guardada de la pila y saltar a esta

times 510-($-$$) db 0 ;Llenar de ceros hasta 510
dw 0xAA55             ;Firma para indicar que es un bootloader

