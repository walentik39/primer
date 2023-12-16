program Work;
var x: integer;
begin
	writeln('Введите возраст');
	read(x);
	if (x >= 25) and (x <= 40) then
		writeln('Подходит!')
	else
		writeln('Не подходит. ');
end.
