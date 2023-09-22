.text
.global _start
_start:
mov $5, %rax
mov $7, %rbx
jmp m
mov %rax, %rcx
mov %rbx, %rdx

//exit
m: mov $60, %rax
mov $0, %rdi
syscall
