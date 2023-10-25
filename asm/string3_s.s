.text
.global _start
_start:
movq %rsp, %rbp    /*сохранить начальное значение %rsp*/
/* вывести сообщение Input text */
movq $1, %rax /* номер функции sys_write */
movq $1, %rdi /* дескриптор стандартного выходного потока(терминал) */
movq $str1, %rsi
movq $12, %rdx
syscall

/* ввести строку с клавиатуры */
movq $0, %rax /* номер функции sys_read */
movq $1, %rdi
movq $str3, %rsi /* адрес сохранение строки */
movq $10, %rdx /* максимальное количество символов */
syscall

/* вывести на экран сообщение Your text: и введённую строку */
movq %rax, %rdx /* количество символов в введёной строке*/
addq $11, %rdx /*плюс количество символов в строке Your text: */
movq $1, %rax /* функция sys_write */
movq $str2, %rsi
syscall

movq %rbp, %rsp    /* очистить память */

movq $60, %rax
movq $0, %rdi
syscall
.data
str1: .ascii "Input text:\n"
str2: .ascii "Your text:\n"
str3: .fill 10, 1, 0
