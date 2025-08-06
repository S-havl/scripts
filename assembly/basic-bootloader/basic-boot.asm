[bits 16]			; Define 16 bits.
[org 0x7C00]			; Bootloader's starting sector.

_start:				; _start function.
    call _print_message	; Call the _print_message function.
    jmp $   			; Jump onto the instruction (infinite loop). 
_print_message:		; _print_message function.
    mov si, message		; Move the 'message' string to the SI register.
_print_loop:			; _print_loop function.
    lodsb			; 'Load String Byte' Load byte into the AL register.
    or al, al			; Bitwise condition to check if it's 0 or 1.
    jz _end			; 'jump if zero' Jump to the _end function if the string character is zero.
    mov ah, 0x0E		; Teletype function.
    int 0x10			; Call BIOS interrupt to print on screen.
    jmp _print_loop		; Jump back to _print_loop, creating a loop until the string ends (0).
_end:				; _end function.
    ret				; Pop the return address (from _start) and jump back to it.

message db 'HELLO WORLD', 0	; Define byte for the 'HELLO WORLD' string and place a 0 at the end indicating string termination. 0 = NULL

times 510-($-$$) db 0		; Fill the remaining bytes of the file with zeros.
dw 0xAA55			; Bootloader signature.
