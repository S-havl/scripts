# Basic Bootloader

This folder contains a simple 16-bit bootloader written in assembly language. This bootloader is designed to be loaded by the BIOS at `0x7C00` and will print "HELLO WORLD" to the screen.

## How it Works

The bootloader operates in 16-bit real mode. Here's a breakdown of the key components:

* **`[bits 16]`**: Specifies that the code should be assembled for a 16-bit architecture.
* **`[org 0x7C00]`**: Sets the origin address for the code to `0x7C00`, which is the standard loading address for boot sectors by the BIOS.
* **`_start`**: The entry point of the bootloader. It calls the `_print_message` function.
* **`_print_message`**: This function is responsible for displaying the "HELLO WORLD" message.
    * It loads the address of the `message` string into the `SI` (Source Index) register.
    * **`_print_loop`**: This loop iterates through each character of the `message` string.
        * **`lodsb`**: Loads a byte from the memory location pointed to by `SI` into the `AL` (Accumulator Low) register and increments `SI`.
        * **`or al, al`**: This instruction checks if the loaded character is null (0).
        * **`jz _end`**: If `AL` is zero (indicating the end of the string), it jumps to the `_end` label.
        * **`mov ah, 0x0E`**: Sets the `AH` register to `0x0E`, which is the BIOS teletype output function.
        * **`int 0x10`**: Invokes BIOS interrupt `0x10` to print the character in `AL` to the screen.
        * **`jmp _print_loop`**: Jumps back to the beginning of the `_print_loop` to process the next character.
* **`_end`**: After printing the message, it returns control. In this specific bootloader, the `_start` function has a `jmp $` instruction, which creates an infinite loop, effectively halting execution after the message is displayed.
* **`message db 'HELLO WORLD', 0`**: Defines the string "HELLO WORLD" followed by a null terminator (`0x00`), which signifies the end of the string.
* **`times 510-($-$$) db 0`**: This directive fills the remaining bytes of the boot sector with zeros until byte 510. A standard boot sector is 512 bytes long.
* **`dw 0xAA55`**: This is the boot sector signature. The BIOS checks for this signature at the end of the sector to validate it as a bootable disk.

## What I Learned From This Practice Script

Creating this basic bootloader was an insightful experience that deepened my understanding of several fundamental concepts:

* **Assembly Language Basics**: I reinforced my knowledge of basic assembly instructions, register usage (e.g., `SI`, `AL`, `AH`), and control flow (e.g., `call`, `jmp`, `ret`, `jz`).
* **BIOS Interrupts**: I gained practical experience using BIOS interrupts, specifically `INT 0x10` for video services (teletype output). This demonstrated how low-level programs interact with system hardware.
* **Boot Process**: Understanding the `[org 0x7C00]` directive and the `0xAA55` signature solidified my comprehension of how the BIOS loads and executes a boot sector.
* **Memory Addressing**: Working with `SI` and `lodsb` provided a clearer picture of how strings are handled in memory and iterated over at a low level.
* **Null Termination**: The importance of null termination for strings in assembly, allowing loops to gracefully identify the end of a string, became very clear.
* **Infinite Loops**: The `jmp $` instruction, while simple, highlighted a common technique for halting execution in low-level programming when no further operations are intended.

This exercise served as an excellent introduction to the very foundation of how an operating system starts and interacts with hardware.
