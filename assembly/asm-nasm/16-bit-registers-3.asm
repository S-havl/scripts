mov ax, 0x1234 ; valor AX = 0x1234
mov bx, 0x5678 ; valor BX = 0x5678
mov cx, 0x9101 ; valor CX = 0x9101

push ax ; Agregar a la pila el valor de AX
push bx ; Agregar a la pila el valor de BX
push cx ; Agregar a la pila el valor de CX

mov ax, 0x0000 ; "Eliminar" valor de AX
mov bx, 0x0000 ; "Eliminar" valor de BX
mov cx, 0x0000 ; "Eliminar" valor de CX

pop ax ; Recuperar valor de AX de la pila
pop bx ; Recuperar valor de BX de la pila
pop cx ; Recuperar valor de CX de la pila

