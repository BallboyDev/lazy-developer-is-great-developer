@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

SET PARAM=%*

FOR %%Z IN (%PARAM%) DO (
    @REM ECHO %%Z
    
    
    FOR /F "TOKENS=1,2 DELIMS=:" %%A IN (command.json) DO (
        SET LINE1=%%A
        SET LINE2=!LINE1: =!

        ECHO !P! / !LINE2!
        
        IF !P!==!LINE2!(
            ECHO BALLBOY
        )
    )
)

ENDLOCAL




@ECHO OFF
setlocal enabledelayedexpansion

SET I=1

FOR %%A IN (%*) DO (
    SET PARAM!I!=%%A
    SET /A I+=1
)

FOR /L %%A IN (1, 1, 3) DO (
    ECHO %%A
    ECHO !PARAM%%A!
)

endlocal


SET I=1
FOR %%A IN (%*) DO (
    SET PARAM!I!=%%A
    SET /A I+=1
)

SET CURPARAM=%1

FOR /F "TOKENS=1,2 DELIMS=:" %%A IN (command.json) DO (
    SET CMD=%%A
    SET CMD=!CMD: =!
    IF "!CURPARAM!"==!CMD! (
        ECHO BALLBOY
    )
    
    FOR %%Q IN (%*) DO (
        
    )
)
