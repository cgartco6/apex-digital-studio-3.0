if (!(Test-Path "../.env")) {
  Copy-Item "../.env.example" "../.env"
  Write-Host ".env file created"
}

Write-Host "Environment configuration ready." -ForegroundColor Green
