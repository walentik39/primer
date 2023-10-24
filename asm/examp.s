.text
.global _start
_start:
mov $1, %rax
mov $1, %rdi
mov $msg, %rsi
mov $21, %rdx
syscall
//exit
mov $60, %rax
mov $0, %rdi
syscall
.data
 msg:
.ascii "Привет Мир!\n" 
