
global _main
extern _printf
extern _ExitProcess@4


section .data
	
section .bss
	dump: resb 8
	
	out: resb 50
	out_ptr: resb 2

section .text
_main:

		
	push 72

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 101

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 108

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 108

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 111

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 44

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 32

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 87

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 111

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 114

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 108

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 100

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 33

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax
		
	push 0

	pop eax ; get value

	mov ecx, [out_ptr] 	;inc pointer
	inc ecx
	mov [out_ptr], ecx

	mov ecx, out ; save value into buffer 
	add ecx, out_ptr
	mov [ecx], eax

	push out
	call _printf

	push dword 0
	call _ExitProcess@4
