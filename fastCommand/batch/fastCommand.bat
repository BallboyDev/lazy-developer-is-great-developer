@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

SET PARAMLEN=0
FOR %%A IN (%*) DO (
    SET /A PARAMLEN+=1
    SET PARAM!PARAMLEN!=%%A
)
SET CURPARAM=!PARAM1!
SET CURINDEX=1

ECHO !PARAM1! / !PARAM2! / !PARAM3! / !PARAMLEN!

FOR /F "TOKENS=1,2 DELIMS=:" %%A IN (command.json) DO (
    SET CMD=%%A
    SET CMD=!CMD: =!

    IF "!CURPARAM!"==!CMD! (
        ECHO "!CURPARAM!" / !CMD!
        FOR /L %%P IN (1, 1, !PARAMLEN!) DO (
            IF !CURINDEX!==%%P (
                ECHO !CURINDEX! / %%P
                SET TEMPINDEX=!CURINDEX!+1
                SET CURPARAM=
            )
        )
    )

)

ENDLOCAL