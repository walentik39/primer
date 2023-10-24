global fizz
section .text
fizz:
	mov eax, edi
	mov ebx, 3
	cdq          ; расширение 32 бит в 64 бита edx:eax
	idiv ebx     ; edx:eax / 3
	mov eax, edx ; остаток в edx, переносим его в eax
	test eax, eax ; взводим ZF если eax = 0
	sete al       ; кладём 01h в al, если ZF==1
	movzx eax, al ; копируем с расширением а eax - return
	ret

