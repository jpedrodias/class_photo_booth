# Define variáveis de ambiente necessárias

$env:MAIL_USERNAME = ""
$env:MAIL_PASSWORD = ""
$env:MAIL_SENDER   = ''

$env:FLASK_APP   = "app.py"         # Substitua pelo seu arquivo Flask principal
$env:FLASK_ENV   = "development"    # Ou "production" se for o
$env:FLASK_DEBUG = "1"            # Ativar debug mode

Write-Host "Ambiente Flask configurado:"
Write-Host "`tMAIL_SENDER = $env:MAIL_SENDER"
Write-Host "`tFLASK_APP = $env:FLASK_APP"
Write-Host "`tFLASK_ENV = $env:FLASK_ENV"
Write-Host "`tFLASK_DEBUG = $env:FLASK_DEBUG"
