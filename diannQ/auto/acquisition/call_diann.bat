@echo off

rem source file:
set fasta_type=%1
set raw_data_path=%2

rem add path to python env
run_acquisition.py "%raw_data_path%" "%fasta_type%"
