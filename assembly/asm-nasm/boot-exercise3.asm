[BITS 16]		; Indicar que trabajamos con 16 bits.
[org 0x7C00]		; Origen donde se carga el bootloader.

_start:			; Funcion _start.
    mov ax, 0xAAAA	; Mover 0xAAAA a AX.
    push ax		; Guardar AX dentro de la pila.
    call _modificarAX   ; Hacer call, guardar siguiente instruccion y saltar a la funcion llamada. 
    pop ax		; Recuperar AX de la pila con su valor original. 
    mov ah, 0x0E	; Servicio teletipo.
    mov al, 'L'		; Letra L a imprimir para indicar que sigue con vida (Life).
    int 0x10		; Llamar a la BIOS para imprimir.

_modificarAX:		; Funcion _modificarAX.
    mov ax, 0xBBBB	; Mover 0xBBBB a AX, supuestamente "Reemplazando" su valor inicial. 
    mov ah, 0x0E	; Servicio teletipo.	
    mov al, 'H'		; Letra H a imprimir para indicar cambio.
    int 0x10		; Llamar a la BIOS para imprimir.
    ret			; Recuperar instruccion guardada por el call y saltar a ella de regreso.

times 510-($-$$) db 0	; Llenar con ceros el espacio restante.
dw 0xAA55		; Firma que indica ser un bootloader.
