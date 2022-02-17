[bits 32]
global _start
%macro print 1
	mov eax, %1
    mov ebx, 0
    %%printLoop:
        mov cl, [eax]
        cmp cl, 0
        je %%endPrintLoop
        inc ebx
        inc eax
        jmp %%printLoop
    %%endPrintLoop:
    mov eax, 0x01
    mov edi, 0x01
    mov esi, %1
    mov edx, ebx
    syscall
%endmacro

%macro exit 1
	
%endmacro
section .data
text:
	db "Hello, World!", 0x0a, 0x00
section .text
	print text
