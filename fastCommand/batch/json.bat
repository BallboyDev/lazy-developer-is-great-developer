@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

set param=%*

for %%a in (%param%) do (
    echo %%a
    for /f "tokens=1,2 delims=:" %%b in (command.json) do (
        echo "%%a %%b %%c"
        
        if %%a==%%b (
            echo ballboy Test
        )
    )
    echo "================"
)


ENDLOCAL