program Num;
var x: integer;
begin
	writeln('Введите число');
	read(x);
	if (10<=  x) and (x <= 99) 
			and (x mod 7 = 0) then
		writeln('Да!')
	else
		writeln('Нет ');
end.
