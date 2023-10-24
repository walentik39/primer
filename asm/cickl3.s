.text
.global _start
_start:

movq %rsp, %rbp
sub $2,  %rsp

movb $35, 0(%rsp) /* вывод символа # */
movb $10, 1(%rsp) /* перевод строки */

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $2,  %rdx

movq $0, %rbx

m:
cmp $5, %rbx /* счётчик повторений проверяет равняется ли %rbx 5 */
je n /* то переходим на метку n */
movq $1, %rax
syscall
add $1, %rbx
jmp m  

n:


movb $10, 0(%rsp) /* перевод строки */
syscall
movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
