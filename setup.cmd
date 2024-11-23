@echo off
setlocal enabledelayedexpansion

:: Set paths
set SOURCE_FOLDER=functions
set COMPILED_FOLDER=compiled_functions

:: Ensure the compiled_functions folder exists
if not exist "%COMPILED_FOLDER%" (
    echo Creating the compiled_functions folder...
    mkdir "%COMPILED_FOLDER%"
)

:: Loop through all .py files in the source folder
for %%f in (%SOURCE_FOLDER%\*.py) do (
    :: Get the base filename (without extension)
    set FILE_NAME=%%~nf

    :: Run mypyc on the current file
    echo Compiling %%f with mypyc...
    mypyc %%f

    :: Check if the .pyd file exists in the source folder after compilation
    if exist "!FILE_NAME!*.pyd" (
        echo Moving !FILE_NAME! to the compiled_functions folder...
        move /Y "!FILE_NAME!*.pyd" "%COMPILED_FOLDER%\"
    ) else (
        echo No .pyd file generated for !FILE_NAME!...
    )

    echo.
)

echo All files compiled and moved successfully.
