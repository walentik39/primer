.text
.global _start
_start:

movq %rsp, %rbp    /*сохранить начальное значение %rsp*/
subq $9, %rsp     /*выделяем 10 байтов на стеке*/


subq $8, %rsp
movq $0x000a3a7478657420, %rax /* text */
movq %rax, 0(%rsp)

subq $8, %rsp
movq $0x72756f590a3a7478, %rax /* xt: Your */
movq %rax, 0(%rsp)

subq $8, %rsp
movq $0x6574207475706e49, %rax /* Input te */
movq %rax, 0(%rsp)

/* вывести сообщение Input text: */
movq $1, %rax      /*sys_write номер функции*/
movq $1, %rdi      /*дескриптор стандартного входного потока (терминал)*/
movq %rsp, %rsi    /* загрузить адрес пространства где хранится %rsp*/
movq $12, %rdx     /* максимальное количество считываемых символов*/
syscall
/* Ввести строку с клавиятуры */
movq $0, %rax /* номер функции sys_read */
movq $1, %rdi /* дескриптор стандартного входного потока (клавиатура)*/
movq %rsp, %rsi /* адрес сохранения строки */
addq $23, %rsi
movq $10, %rdx  /* максимальное количество символов */
syscall

movq %rbp, %rsp    /* очистить память */

movq $60, %rax
movq $0, %rdi
syscall
