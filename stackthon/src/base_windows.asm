
global _main
extern _printf
extern _ExitProcess@4


section .data
	{dataSect}
section .bss
	dump: resb 8
	{bssSect}
section .text
_main:
	{textSect}
