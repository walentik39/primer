.text
.global _start
_start:

movq %rsp, %rbp
sub $13, %rsp
movb $0x48, 0(%rsp)
movb $0x65, 1(%rsp)
movb $0x6c, 2(%rsp)
movb $0x6c, 3(%rsp)
movb $0x6f, 4(%rsp)
movb $0x0a, 5(%rsp)
movb $0x57, 6(%rsp)
movb $0x6f, 7(%rsp)
movb $0x72, 8(%rsp)
movb $0x6c, 9(%rsp)
movb $0x64, 10(%rsp)
movb $0x0a, 11(%rsp)
movb $0x40, 12(%rsp)

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $13, %rdx
syscall

movq %rbp, %rsp
movq $60, %rax
movq $0, %rdi
syscall
