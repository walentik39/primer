.text
.global _start
_start:

movq %rsp, %rbp    /*сохранить начальное значение %rsp*/
subq $10, %rsp     /*выделяем 10 байтов на стеке*/

movq $0, %rax      /*sys_read чтение из регистра*/
movq $1, %rdi      /*дескриптор стандартного входного потока (клавиатура)*/
movq %rsp, %rsi    /* загрузить адрес пространства где хранится %rsp*/
movq $10, %rdx     /* максимальное количество считываемых символов*/
syscall

movq %rax, %rdx
movq $1, %rax
syscall

movq %rbp, %rsp    /* очистить память */

movq $60, %rax
movq $0, %rdi
syscall
