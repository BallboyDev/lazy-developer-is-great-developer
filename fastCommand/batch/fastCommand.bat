@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

for %%x in (%*) do (
	set /a "paramLen+=1"
	call set path!paramLen!=%%~!paramLen!
)

set index=1
call set param=%%path!index!%%

for /f "tokens=1,2 delims=:" %%a in (command.json) do (
	
	set json=%%a
	REM 한칸 띄어쓰기 제거
	set json=!json: =!
	REM Tab 공백 제거
	set json=!json:	=!
	rem 쌍따옴표 제거
	set json=!json:"=!
	
	if !json!==!param! (


		if !paramLen!==!index! (
			set cmd=%%b
			set cmd=!cmd: =!
			set cmd=!cmd:	=!
			@REM set cmd=!cmd:{=!

			if !cmd!=={ (

				call set param=init
			)

			if not !cmd!=={ (
				set exe=%%b
				set exe=!exe:"=!
				set exe=!exe:,=!

				echo !exe!
				goto execute
			)
		)

		if not !paramLen!==!index! (

			set /a "index+=1"
			call set param=%%path!index!%%
		)
		
	)
)
goto error

:execute
start !exe!
goto finish

:error
echo not found cmd

:finish
exit
ENDLOCAL