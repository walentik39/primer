.text
.global _start
_start:
mov $8, %rax
mov $4, %rbx
mov $3, %rcx

cmp $1, %rcx
jne a
add %rdx, %rax
jmp z

a:

cmp $2, %rcx
jne b
sub %rbx, %rax
jmp z

b:
cmp $3, %rcx
jne c
mul %rbx
jmp z

c:
cmp $4, %rcx
jne z
div %rbx

z:

//exit
mov $60, %rax
mov $0, %rdi
syscall
