#!/bin/sh
echo $GZCTF_FLAG > flag
7z a -tzip 0 flag -pCFCD -sdel
python pic.py
python -m http.server 80