.text
.global _start
_start:

mov $8, %rax
mov $9, %rbx
mov $3, %rcx

mov %rcx, %rsi
sub $1, %rcx
jne a
add %rbx, %rax
jmp z
a:
mov %rsi, %rcx
sub $2, %rcx
jne b
sub %rbx, %rax
jmp z

b:
mov %rsi, %rcx
sub $3, %rcx
jne c
mul %rbx
jmp z
c:
mov %rsi, %rcx
sub $4, %rcx
jne z
div %rbx
z:
//exit
mov $60, %rax
mov $0, %rdi
syscall
