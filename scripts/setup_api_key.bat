@echo off
echo ================================================
echo   SETUP GEMINI API KEY - Health Checker
echo ================================================
echo.
echo Langkah-langkah:
echo 1. Buka: https://aistudio.google.com/app/apikey
echo 2. Login dengan Google
echo 3. Klik "Create API Key"
echo 4. Copy API key yang muncul
echo.
echo ================================================
echo.

set /p API_KEY="Paste API Key Anda di sini: "

if "%API_KEY%"=="" (
    echo ERROR: API Key tidak boleh kosong!
    pause
    exit /b 1
)

echo.
echo Setting environment variable...
setx GEMINI_API_KEY "%API_KEY%"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================
    echo   SUCCESS! API Key berhasil di-set
    echo ================================================
    echo.
    echo PENTING: 
    echo 1. Restart terminal/PowerShell Anda
    echo 2. Jalankan: python app.py
    echo 3. Chat AI akan aktif otomatis!
    echo.
) else (
    echo.
    echo ERROR: Gagal set environment variable
    echo Coba jalankan sebagai Administrator
    echo.
)

pause
