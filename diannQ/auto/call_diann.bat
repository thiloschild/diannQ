@echo off

rem source file:
set raw_data_path=%2

rem it's important that raw_data_path does not end with "\"
for %%I in ("%raw_data_path%") do (
    set folder=%%~nxI
)

echo.folder is: %folder%

robocopy %raw_data_path% M:\test\%folder%\
run_acquisition.py "%folder%" "%1"