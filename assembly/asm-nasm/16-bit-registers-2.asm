mov ax, 0xAAAA ; Mueve 0xAAAA a AX
mov bx, ax ; Copia AX en BX
mov al, 0x55 ; Cambia AL a 0x55
mov cx, ax ; Copia AX en CX

; Demostracion de impresion porque son pasos complejos:
mov ah, 0x0E ; Funcion teletipo
mov al, '1' ; Caracter a imprimir (uno por uno)
int 0x10 ; Llamar la interrupcion de BIOS para mostrar en pantalla
