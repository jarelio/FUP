echo "Script para criar arquivos Python"
FOR /L %%A IN (8,1,39) DO (
	ECHO %%A
	copy NUL 1.%%A.py
)
pause