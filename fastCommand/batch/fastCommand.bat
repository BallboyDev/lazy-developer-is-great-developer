@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
echo %*

for %%x in (%*) do (
	set /a "i+=1"
	call set path!i!=%%~!i!
)

set index=1

for /f "tokens=1,2 delims=:" %%a in (test.json) do (
	call set param=%%path!index!%%
	set cmd=%%a
	REM 한칸 띄어쓰기 제거
	set cmd=!cmd: =!
	REM Tab 공백 제거
	set cmd=!cmd:	=!
	rem 쌍따옴표 제거
	set cmd=!cmd:"=!
	
	if !cmd!==!param! (
		echo !cmd! / !param!
		set /a "index+=1"
		call set param=%%path!index!%%
		echo %%b
	)
)

ENDLOCAL