.text
.global _start
_start:

movb $0x12, %al
movb $0x34, %ah
shl $16, %rax
movw $0x1234, %bx
movw %bx, %ax
shl $32, %rax
movl $0x12345678, %ecx
movl %ecx, %eax
movq $0x123456789abcdef, %rdx

movq %rsp, %rbp

pushw %ax

movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
