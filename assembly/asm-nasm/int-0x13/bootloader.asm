[bits 16]
[org 0x7C00]

_start:
    mov ah, 0x02
    mov al, 1
    mov ch, 0
    mov cl, 2
    mov dh, 0
    mov dl, 0x80
    mov bx, 0x8000
    mov ax, 0x0000
    mov es, ax
    int 0x13
    jc _fallo

    ; Imprimir Registros (Crudo) - Depuración
    mov ah, 0x0E ; Función teletipo

    mov al, 'C'  ; Imprimir 'C' para CS
    int 0x10

    mov al, 'I'  ; Imprimir 'I' para IP
    int 0x10

    mov al, 'E'  ; Imprimir 'E' para ES
    int 0x10

    mov al, 'B'  ; Imprimir 'B' para BX
    int 0x10

    jmp 0x0000:0x8000

_fallo:
    mov ah, 0x0E
    mov al, 'E'
    int 0x10
    jmp $

times 510-($-$$) db 0
dw 0xAA55

