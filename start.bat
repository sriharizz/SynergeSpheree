@echo off
echo Starting SynergySphere...
call venv\Scripts\activate.bat
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
pause
