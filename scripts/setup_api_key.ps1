# Setup Gemini API Key - PowerShell Script
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  SETUP GEMINI API KEY - Health Checker" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Langkah-langkah:" -ForegroundColor Yellow
Write-Host "1. Buka: https://aistudio.google.com/app/apikey"
Write-Host "2. Login dengan Google"
Write-Host "3. Klik 'Create API Key'"
Write-Host "4. Copy API key yang muncul"
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

$API_KEY = Read-Host "Paste API Key Anda di sini"

if ([string]::IsNullOrWhiteSpace($API_KEY)) {
    Write-Host ""
    Write-Host "ERROR: API Key tidak boleh kosong!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Setting environment variable..." -ForegroundColor Yellow

# Set untuk session saat ini
$env:GEMINI_API_KEY = $API_KEY

# Set permanent untuk user
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', $API_KEY, 'User')

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "  SUCCESS! API Key berhasil di-set" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "PENTING:" -ForegroundColor Yellow
Write-Host "1. API Key sudah aktif untuk session ini"
Write-Host "2. Jalankan: python app.py"
Write-Host "3. Chat AI akan aktif otomatis!"
Write-Host ""
Write-Host "Untuk session baru, API key sudah tersimpan permanent." -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to continue"
