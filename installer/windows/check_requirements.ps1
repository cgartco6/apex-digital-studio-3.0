Write-Host "Checking system requirements..."

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  Write-Host "Python not found. Please install Python 3.11+" -ForegroundColor Red
  exit 1
}

$docker = Get-Command docker -ErrorAction SilentlyContinue
if (-not $docker) {
  Write-Host "Docker not found. Please install Docker Desktop." -ForegroundColor Red
  exit 1
}

Write-Host "All requirements satisfied." -ForegroundColor Green
