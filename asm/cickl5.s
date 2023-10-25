.text
.global _start
_start:

movq %rsp, %rbp
subq $4,  %rsp

movb $65, 0(%rsp) /* буква алфавита */
movb $97, 1(%rsp) /* маленькая буква */
movb $44, 2(%rsp) /* запятая */
movb $32, 3(%rsp) /* код пробела */

movq $1, %rax
movq $1, %rdi
movq %rsp, %rsi
movq $4,  %rdx

movq $0, %rbx

m:
cmpb $91, 0(%rsp) /* сравнивает значение 91 с разименованым регистром %rsp */
je n /* то переходим на метку n */
movq $1, %rax
syscall
addb $1, 0(%rsp)
addb $1, 1(%rsp)
jmp m  

n:


movb $8, 0(%rsp) /* забой black space */
movb $8, 1(%rsp)
movb $32, 2(%rsp)
movb $10, 3(%rsp) /* код перевода строки */
movq $4, %rdx
movq $1, %rax
syscall
movq %rbp, %rsp

movq $60, %rax
movq $0, %rdi
syscall
