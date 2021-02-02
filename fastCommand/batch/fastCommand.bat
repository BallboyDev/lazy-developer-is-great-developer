@REM @ECHO OFF
@REM SETLOCAL ENABLEDELAYEDEXPANSION

@REM for %%x in (%*) do (
@REM 	set /a "paramLen+=1"
@REM 	call set path!paramLen!=%%~!paramLen!
@REM )

@REM set index=1
@REM call set param=%%path!index!%%

@REM if "%1"=="" (
@REM 	set paramLen=1
@REM 	call set param=init
@REM )

@REM for /f "tokens=1,* delims=:" %%a in (command.json) do (
	
@REM 	set json=%%a
@REM 	REM 한칸 띄어쓰기 제거
@REM 	set json=!json: =!
@REM 	REM Tab 공백 제거
@REM 	set json=!json:	=!
@REM 	rem 쌍따옴표 제거
@REM 	set json=!json:"=!
	
@REM 	echo [!json!] / [!param!] / [!paramLen!]
@REM 	if !json!==!param! (


@REM 		if !paramLen!==!index! (
@REM 			set cmd=%%b
@REM 			set cmd=!cmd: =!
@REM 			set cmd=!cmd:	=!
@REM 			@REM set cmd=!cmd:{=!

@REM 			if !cmd!=={ (

@REM 				call set param=init
@REM 			)

@REM 			if not !cmd!=={ (
@REM 				set exe=%%b
@REM 				set exe=!exe:"=!
@REM 				set exe=!exe:,=!
@REM 				goto execute
@REM 			)
@REM 		)

@REM 		if not !paramLen!==!index! (

@REM 			set /a "index+=1"
@REM 			call set param=%%path!index!%%
@REM 		)
		
@REM 	)
@REM )
@REM goto error

@REM :execute
@REM echo !exe!
@REM pause
@REM %exe%
@REM goto finish

@REM :error
@REM echo not found cmd
@REM goto finish

@REM :init
@REM notepad "./command.json"

@REM :finish
@REM @REM exit
@REM ENDLOCAL