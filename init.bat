@echo off
if exist "env\Scripts\Activate.bat" (
    echo "La carpeta 'env' y el archivo 'Activate.bat' existen.";

    env\Scripts\activate.bat && python pingpong.py 
) else (
    python -m venv env
    echo La carpeta 'env' y/o el archivo 'Activate.bat' Creado.
    env\Scripts\activate.bat && python -m pip install -r requirements.txt && python pingpong.py
)