.text
.global _start
_start:
movq %rsp, %rbp

sub $5, %rsp
movb $0x54, (%rsp)
movb $0x65, 1(%rsp)
movb $0x73, 2(%rsp)
movb $0x74, 3(%rsp)
movb $0x0A, 4(%rsp)

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $5, %rdx
syscall

movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
