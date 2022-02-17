section .bss

section .data

section .text
	global _start
_start:
	mov rax, 0x46
	push rax
	pop rax
	mov rax, 0x3c
	mov rdi, 0
	syscall