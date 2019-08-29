@ECHO off

cd ..

ECHO Hilo inicial
SET /p init=
ECHO Limite de hilos por proceso
SET /p limit=
ECHO Cantidad de procesos paralelos
SET /p procesos=
SET x=0

rem : Iniciar hilos
:while
IF NOT %x% == %procesos% (
	START python FcBrowser %init% %limit%
	SET /a "x=%x%+1"
	SET /a "init=%init%+%limit%"
	GOTO :while
)

