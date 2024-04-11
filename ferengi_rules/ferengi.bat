@echo off
setlocal enabledelayedexpansion
set /a "n=%RANDOM% %% 155 + 1"

set /a "line=0"
for /f "delims=" %%l in (rules.txt) do (
  set /a "line+=1"
  if !line!==%n% (
    set "text=%%l"
    goto :done
  )
)

:done
endlocal & set "text=%text%"

cd F:\Projekts\EInkDisplay
call .venv\Scripts\activate
python client.py "%text%"
