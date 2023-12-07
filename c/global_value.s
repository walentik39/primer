	.file	"global_value.c"
	.text
	.globl	arr1
	.data
	.type	arr1, @object
	.size	arr1, 3
arr1:
	.ascii	"\xab\xcd\xef"
	.globl	arr2
	.align 2
	.type	arr2, @object
	.size	arr2, 6
arr2:
	.value	0x1234
	.value	0x5678
	.value	0xabcd
	.section	.rodata
.LC0:
	.string	"arr1: 0x%p\n"
.LC1:
	.string	"arr2: 0x%p\n"
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
	leaq	arr1(%rip), %rax
	movq	%rax, %rsi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	leaq	arr2(%rip), %rax
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
