mov ax, 0x1234
push ax
mov ax, 0x0000 
pop ax

1- el valor 0x1234 se coloca en ax.
2- empujamos ax a la pila.
3- el valor 0x1234 cambia a 0x0000.
4- sacamos ax de la pila.
5- el valor final de ax es 0x0000 
