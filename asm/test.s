	.file "test.s"
	.data
str:
	.ascii "Привет!\n"
	.text
	.global _start
_start:
	movq $1, %rax
	movq $1, %rdi
	leaq str(%rip), %rsi
	movq $15, %rdx
	syscall

	/* exit */
	movq $60, %rax
	movq $0, %rdi
	syscall
