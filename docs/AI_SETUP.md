# Setup AI Chatbot dengan Google Gemini

## Langkah 1: Dapatkan API Key

1. Buka [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Login dengan akun Google Anda
3. Klik "Create API Key"
4. Copy API key yang diberikan

## Langkah 2: Setup Environment Variable

### Windows (PowerShell):
```powershell
# Temporary (hanya untuk session saat ini)
$env:GEMINI_API_KEY="your_api_key_here"

# Permanent (untuk user)
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'your_api_key_here', 'User')
```

### Windows (Command Prompt):
```cmd
set GEMINI_API_KEY=your_api_key_here
```

### Linux/Mac:
```bash
export GEMINI_API_KEY="your_api_key_here"

# Untuk permanent, tambahkan ke ~/.bashrc atau ~/.zshrc:
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### Menggunakan file .env:
```bash
# Copy file .env.example ke .env
cp .env.example .env

# Edit .env dan isi dengan API key Anda
# GEMINI_API_KEY=your_actual_api_key_here
```

Kemudian install python-dotenv:
```bash
pip install python-dotenv
```

Dan tambahkan di app.py:
```python
from dotenv import load_dotenv
load_dotenv()  # Load .env file
```

## Langkah 3: Jalankan Aplikasi

```bash
python app.py
```

## Mode Fallback

Jika API key tidak tersedia atau ada error, chatbot akan otomatis menggunakan **rule-based system** sebagai fallback. Aplikasi tetap berfungsi normal!

## Verifikasi

Untuk memverifikasi AI aktif, cek console output saat aplikasi start:
- ✅ Jika AI aktif: Tidak ada warning
- ⚠️ Jika fallback: "Warning: AI Chat tidak tersedia"

## Troubleshooting

### Error: "GEMINI_API_KEY tidak ditemukan"
- Pastikan environment variable sudah di-set
- Restart terminal/PowerShell setelah set environment variable
- Cek dengan: `echo $env:GEMINI_API_KEY` (PowerShell) atau `echo %GEMINI_API_KEY%` (CMD)

### Error: "API key not valid"
- Pastikan API key yang di-copy benar
- Cek di Google AI Studio apakah API key masih aktif
- Generate API key baru jika perlu

### Chatbot tidak merespons dengan AI
- Cek console untuk error message
- Pastikan koneksi internet aktif (Gemini memerlukan internet)
- Coba restart aplikasi

## Batasan Gratis

Google Gemini API gratis memiliki batasan:
- 60 requests per minute
- 1,500 requests per day

Untuk penggunaan lebih tinggi, upgrade ke paid plan.
