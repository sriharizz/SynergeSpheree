Write-Host "Starting SynergySphere..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
