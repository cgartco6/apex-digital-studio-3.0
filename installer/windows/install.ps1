Write-Host "Installing Apex Digital Studio 3.1" -ForegroundColor Cyan

./check_requirements.ps1
./setup_env.ps1

Set-Location ../..
docker-compose build

Write-Host "Installation complete." -ForegroundColor Green
