@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION


:: Read file "package.json" into variable string, removing line breaks.
set string=
for /f "delims=" %%x in (test.json) do set "string=!string!%%x"

rem Remove quotes
set string=%string:"=%
@REM echo !string!

rem Remove braces
set "string=%string:~2,-2%"
@REM echo !string!

rem Change colon+space by equal-sign
set "string=%string:: ==%"
@REM echo !string!

rem Separate parts at comma into individual assignments
set "%string:, =" & set "%"
echo !string!

ENDLOCAL