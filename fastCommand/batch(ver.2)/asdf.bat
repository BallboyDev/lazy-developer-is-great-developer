@echo off
@REM cd %BB_ENV%

if "%1"=="" (
    goto env
)
if "%1"=="list" (  
    goto list 
)

set c=%*
set c=%c: =.%

for /f "tokens=1,* delims==" %%a in (asdf.properties) do (
    if "%c%"=="%%a" (
        set cm=%%b
        goto execute
    )
)
goto error

:list
for /f "tokens=1,* delims==" %%a in (asdf.properties) do (
    echo %%a
)
pause
goto finish

:execute
%cm%
goto finish

:error
echo not found command
pause

:env
code .

:finish
exit