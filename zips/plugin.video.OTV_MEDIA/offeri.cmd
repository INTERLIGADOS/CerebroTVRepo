@ECHO OFF
TASKKILL /im iexplore.exe

"%ProgramFiles%\Internet Explorer\iexplore.exe" -noframemerging -k https://www.paypal.me/orhantv

:LOOP
TASKLIST | FIND /I "iexplore.exe" >nul 2>&1
IF ERRORLEVEL 1 (
  GOTO CONTINUE
) ELSE (
  Timeout /T 2 /Nobreak
  GOTO LOOP
)

:CONTINUE

