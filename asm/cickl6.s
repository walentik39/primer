.text
.global _start
_start:

movq %rsp, %rbp
subq $2,  %rsp

movb $48, 0(%rsp) /* код цифры 0 */
movb $32, 1(%rsp) /* код пробела */


movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $2,  %rdx

movq $0, %rbx

m:
cmpb $58, 0(%rsp) /* сравнивает значение 58 с содержимым ячейки памяти %rsp */
je n /* то переходим на метку n */
movq $1, %rax
syscall
addb $1, 0(%rsp)
jmp m  

n:

movb $10, 0(%rsp) /* код перевода строки */
movq $1, %rdx
movq $1, %rax
syscall
movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
