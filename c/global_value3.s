	.file	"global_value3.c"
	.text
	.globl	word1
	.section	.rodata
	.align 2
	.type	word1, @object
	.size	word1, 2
word1:
	.value	-21555
	.globl	lword2
	.align 4
	.type	lword2, @object
	.size	lword2, 4
lword2:
	.long	305419896
	.align 8
.LC0:
	.string	"word1: addr = 0x%p, value = %hx\n"
	.align 8
.LC1:
	.string	"lword2: addr = 0x%p, value = %x\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB6:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movq	%rsi, -16(%rbp)
	movl	$-21555, %eax
	cwtl
	movl	%eax, %edx
	leaq	word1(%rip), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$305419896, %eax
	movl	%eax, %edx
	leaq	lword2(%rip), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.ident	"GCC: (GNU) 13.2.1 20231110"
	.section	.note.GNU-stack,"",@progbits
