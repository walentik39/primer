Var
	gradus, minuta: integer;
	radian: real;
begin
	write('gradus= ');
	//ввод переменной gradus.
	readln(gradus);
	//вывод на экран символов минута.
	write('minuta= ');
	//ввод переменной minuta.
	readln(minuta);
	//вычисление.
	radian:=gradus*pi/180+minuta*pi/(180*60);
	writeln('radian= ', radian);
	end.
