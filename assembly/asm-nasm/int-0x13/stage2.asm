[bits 16]
[org 0x8000]

_start:
    mov ah, 0x0E
    mov al, '2'
    int 0x10
    
    jmp $


