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
