.text
.global _start
_start:
movq %rsp, %rbp    /*сохранить начальное значение %rsp*/
movq $0, %rax
xorq %rdx, %rdx /* по разрядная исключаюшая или обнуляющая %rdx */
movb $123, %al

subq $1, %rsp
movb $10, 0(%rsp)

movq $10, %rbx

div  %rbx
addb $48, %dl
subq $1, %rsp
movb %dl, (%rsp)



movq $0, %rdx
div  %rbx
addb $48, %dl
subq $1, %rsp
movb %dl, (%rsp)

movq $0, %rdx
div  %rbx
addb $48, %dl
subq $1, %rsp
movb %dl, (%rsp)


movq $1, %rax /*номер системного вызова sys_write */
movq $1, %rdi /* куда выводить на экран */
movq %rsp, %rsi /* адрес начала выводимых данных */
movq $3, %rdx /* количество выводимых символов */
syscall

movq %rbp, %rsp    /* очистить память */

movq $60, %rax
movq $0, %rdi
syscall
