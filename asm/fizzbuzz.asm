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

global buzz
section .text
buzz:
	mov eax, edi ; int buzz(int n)
	mov ebx,  5
	cdq
	idiv ebx
	sub edx, 1 ;если edx 0, то edx - 1 взводит флан CF=1
	sbb eax, eax ; eax - eax -CF, -1 = FFh или 0 = 00h
	neg eax      ; FFh => 01h, 00h => 00h
	ret	
