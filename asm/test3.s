.text
.global _start
_start:

mov $5, %rax
mov $8, %rbx

sub %rax, %rbx
je a
jne b

a:mov $2, %rdx
jmp c
b:mov $1, %rdx
c:
//exit
mov $60, %rax
mov $0, %rdi
syscall
