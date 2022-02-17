from sys import argv


iota_counter = 0
def iota():
	global iota_counter
	result = iota_counter
	iota_counter +=1
	return result


OP_PUSH = iota() # push value onto stack
OP_DUP = iota() # duplicate top top item
OP_SWAP = iota() # swap the top 2 items
OP_DROP = iota() # forget top item of stack
OP_PLUS = iota() # add top 2 values of stack
OP_MINUS = iota() # subtract 1st stack item from 2nd
# OP_INC = iota() # increment the top value of the stack
# OP_DEC = iota() # decrement the top value of the stack
OP_DUMP = iota() # print the top stack item to stdout
OP_EXIT = iota() # exit with the 1st value on stack as exit code
OP_CONST = iota() # declare compiletime constant
OP_LABEL = iota() # declare label (memory addr)
OP_JUMP = iota() # jump to label
OP_JEQ = iota() # jump to label if top 2 items of stack are equal
OP_JNE = iota() # jump to label if top 2 items of stack are not equal

compiletime = [OP_CONST, OP_LABEL]


class Run():
	def push(self, value:str|int) -> tuple:
		return (OP_PUSH, value)
	
	def duplicate(self) -> tuple:
		return (OP_DUP, )
	
	def swap(self) -> tuple:
		return (OP_SWAP, )

	def drop(self) -> tuple:
		return (OP_DROP, )

	def plus(self) -> tuple:
		return (OP_PLUS, )

	def minus(self) -> tuple:
		return (OP_MINUS, )
	
	# def inc(self) -> tuple:
	# 	return (OP_INC, )
	
	# def dec(self) -> tuple:
	# 	return (OP_DEC, )
	
	def dump(self) -> tuple:
		return (OP_DUMP, )
	
	def _exit(self) -> tuple:
		return (OP_EXIT, )
	
	def const(self, name:str, value):
		return (OP_CONST, name, value)

	def label(self, name:str) -> tuple:
		return (OP_LABEL, name)
	
	def jump(self, label:str) -> tuple:
		return (OP_JUMP, label)
	
	def jeq(self, label:str) -> tuple:
		return (OP_JEQ, label)
	
	def jne(self, label:str) -> tuple:
		return (OP_JNE, label)

Op = Run()

# TO DO: UNHARDCODE
program = [
	Op.const("times", 15),
	Op.push("$times"),
	Op.label("loop"),
	Op.push("E"),
	Op.dump(),
	Op.push(1),
	Op.minus(),
	Op.push(0),
	Op.jeq("exit"),
	Op.drop(),
	Op.jump("loop"),
	Op.label("exit"),
	Op.push(0),
	Op._exit()

]


def sub_run(program:list):
	namespace = {}
	stack:list[int] = []
	a:int = 0
	b:int = 0

	ip = 0
	for op in program:		# predefine the labels and the constants
		if op[0] == OP_LABEL:
			namespace[op[1]] = ip
		
		elif op[0] == OP_CONST:
			namespace[op[1]] = op[2]
		ip+=1



	ip = 0 # instruction pointer
	run = True
	while run:
		op = program[ip]
		if op[0] == OP_PUSH:

			if isinstance(op[1], int):				#	is the value ready to be pushed onto the stack?
	
				stack.append(op[1] % 256)			#	use 8-bit values
				ip+=1
			
			elif isinstance(op[1], str):			#	does it need more processing?
			
				if op[1][0] == '$':					#	is it a constant?
					a = namespace[op[1][1:]]		#	put the value of the constant onto the stack
					stack.append(
						ord(a) if isinstance(a, str) else a
					)
					ip+=1

	
				else:	
					for c in op[1]:
						stack.append(ord(c))
						ip+=1
	
			else:
				assert 0, f"Invalid value @[{ip}]"
		

		elif op[0] == OP_DUP:
			a = stack.pop()
			stack.append(a)
			stack.append(a)					
			ip+=1

		elif op[0] == OP_SWAP:
			a = stack.pop()
			b = stack.pop()
			stack.append(a)
			stack.append(b)
			ip+=1

		elif op[0] == OP_DROP:
			
			a = stack.pop()							#	pop the top value off, and do absolutely nothing with it
			ip+=1
		
		elif op[0] == OP_PLUS:
			
			a = stack.pop()
			b = stack.pop()
			stack.append(a + b)						#	pop the top 2 values, add them, and push the result
			ip+=1
		
		elif op[0] == OP_MINUS:
	
			a = stack.pop()
			b = stack.pop()
			stack.append(b - a)						#	pop the top 2 values, subtract the lower from the higher, and push the result
			ip+=1
		
		# elif op[0] == OP_INC:
		# 	a = stack.pop()
		# 	stack.append(a+1)
		# 	ip+=1
		
		# elif op[0] == OP_DEC:
		# 	a = stack.pop()
		# 	stack.append(a-1)
		# 	ip+=1

		elif op[0] == OP_DUMP:
	
			a = stack.pop()							
			print(chr(a), end='')							#	print the top value to stdout
			ip+=1
		
		elif op[0] == OP_EXIT:
	
			a = stack.pop()
			exit(a)

		elif op[0] == OP_JUMP:
			ip = namespace[op[1]]

		elif op[0] == OP_JEQ:
			a = stack.pop()
			b = stack.pop()
			if a == b:
				ip = namespace[op[1]]
			else:
				ip+=1
			stack.append(b)
			stack.append(a)
		
		elif op[0] == OP_JNE:
			a = stack.pop()
			b = stack.pop()
			if a != b:
				ip = namespace[op[1]]
			else:
				ip+=1
			stack.append(b)
			stack.append(a)
		
		elif op[0] in compiletime:
			ip+=1
		else:
			assert 0, f"Unreachable opcode @{{{ip}}}"


class Asm:
	def push(self):
		return """
	push {}"""

	def dup(self):
		return """
	pop rax
	push rax
	push rax""" 

	def swap(self):
		return """
	pop rax
	pop rbx
	push rax
	push rbx"""

	def drop(self):
		return """
	pop"""

	def plus(self):
		return """
	pop rax
	pop rbx
	add rax, rbx
	push rax"""

	def minus(self):
		return """
	pop rax
	pop rbx
	sub rax, rbx
	push rax"""

	def dump(self):
		return """
	pop rax
	mov [dump], rax
	mov rax, 0x01
	mov rdi, 0x01
	mov rsi, dump
	mov rdx, 0x00
	syscall"""

	def _exit(self):
		return """
	mov rax, 0x3c
	pop rdi
	syscall"""
	
	def jeq(self):
		return """
	pop rax
	pop rbx
	cmp rax, rbx
	je {}"""

	def jne(self):
		return """
	pop rax
	pop rbx
	cmp rax, rbx
	jne {}"""

	def jmp(self):
		return """
	jmp {}"""

asm = Asm()


def sub_compile(program:list):
	pass


def main():
	try:
		subcommand = argv[1]
	except IndexError:
		assert False, """
		No subcommand provided.
		Usage:
		stackthon run <path>
		stackthon com <path>"""
	if subcommand == "run":
		sub_run(program)
	elif subcommand ==  "com":
		assert 0, "Not implemented"
	else:
		print(f"""
	Invalid subcommand {subcommand}.
	Usage:
	stackthon run <path>
	stackthon com <path>""")

if __name__=="__main__":
	main()