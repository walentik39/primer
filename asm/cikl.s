.text
.global _start
_start:

movq %rsp, %rbp
subq $4, %rsp

movb $65, 0(%rsp)
movb $97, 1(%rsp)
movb $44, 2(%rsp)
movb $32, 3(%rsp)

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $4, %rdx

m:
cmpb $91, 0(%rsp)
je n
movq $1, %rax
syscall
addb $1, 0(%rsp)
addb $1, 1(%rsp)
jmp m

n:

movb $8, 0(%rsp)
movb $8, 1(%rsp)
movb $32, 2(%rsp)
movb $10, 3(%rsp)
movq $4, %rdx
movq $1, %rax
syscall


movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall

