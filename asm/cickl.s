.text
.global _start
_start:

movq %rsp, %rbp
sub $1,  %rsp

movb $35, 0(%rsp) /* вывод символа # */

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $1,  %rdx
syscall 
syscall 
syscall 
syscall 
syscall 
syscall 
syscall 

movb $10, 0(%rsp) /* перевод строки */
syscall

movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
