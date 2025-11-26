# 🚀 Deployment Guide - Render

Panduan lengkap untuk men-deploy aplikasi **Health Checker Rule-Based Expert System** ke Render.

---

## 📋 Prerequisites

- ✅ Akun GitHub (sudah ada)
- ✅ Repository GitHub: https://github.com/Abibsa/Health-Checker
- ✅ Akun Render (gratis): https://render.com

---

## 🎯 Langkah-Langkah Deployment ke Render

### 1. **Buat Akun di Render**

1. Kunjungi: **https://render.com**
2. Klik **"Get Started for Free"**
3. Sign up dengan **GitHub account** Anda
4. Authorize Render untuk mengakses GitHub

### 2. **Buat Web Service Baru**

1. Setelah login, klik **"New +"** di dashboard
2. Pilih **"Web Service"**
3. Klik **"Connect a repository"**
4. Pilih repository: **Abibsa/Health-Checker**
   - Jika tidak muncul, klik "Configure account" dan berikan akses ke repository

### 3. **Konfigurasi Web Service**

Isi form dengan konfigurasi berikut:

#### Basic Settings:
- **Name**: `health-checker` (atau nama lain yang Anda inginkan)
- **Region**: `Singapore` (atau pilih yang terdekat)
- **Branch**: `main`
- **Root Directory**: (kosongkan)
- **Runtime**: `Python 3`

#### Build & Deploy Settings:
- **Build Command**: 
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command**: 
  ```bash
  gunicorn app:app
  ```

#### Instance Type:
- **Plan**: Pilih **"Free"**
  - 750 jam/bulan gratis
  - 512 MB RAM
  - Akan sleep setelah 15 menit tidak aktif

### 4. **Set Environment Variables**

Scroll ke bagian **"Environment Variables"** dan tambahkan:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | `<your-gemini-api-key>` |
| `FLASK_ENV` | `production` |
| `PYTHON_VERSION` | `3.11.0` |

**Cara mendapatkan GEMINI_API_KEY:**
1. Kunjungi: https://aistudio.google.com/app/apikey
2. Login dengan akun Google
3. Klik "Create API Key"
4. Copy API key dan paste di Render

> **Note**: Jika tidak ada API key, aplikasi tetap berfungsi dengan rule-based fallback.

### 5. **Deploy!**

1. Scroll ke bawah dan klik **"Create Web Service"**
2. Render akan mulai build aplikasi (5-10 menit)
3. Tunggu hingga status berubah menjadi **"Live"** ✅

### 6. **Akses Aplikasi**

Setelah deployment selesai, aplikasi Anda akan tersedia di:

```
https://health-checker.onrender.com
```

(atau sesuai nama yang Anda pilih)

---

## 🔧 Troubleshooting

### Build Failed

**Error**: `No module named 'xxx'`

**Solusi**: 
- Pastikan semua dependencies ada di `requirements.txt`
- Cek build logs di Render dashboard

### Application Error

**Error**: `Application failed to respond`

**Solusi**:
- Cek logs di Render dashboard
- Pastikan `Procfile` berisi: `web: gunicorn app:app`
- Pastikan PORT environment variable digunakan di `app.py`

### API Key Not Working

**Error**: AI chatbot tidak berfungsi

**Solusi**:
- Cek environment variable `GEMINI_API_KEY` sudah di-set
- Pastikan API key valid
- Aplikasi tetap berfungsi dengan rule-based fallback

### App Sleeps (Free Tier)

**Gejala**: App lambat saat pertama kali diakses

**Penjelasan**: 
- Free tier Render akan sleep setelah 15 menit tidak aktif
- Cold start membutuhkan 30-60 detik
- Ini normal untuk free tier

**Solusi**:
- Upgrade ke paid plan ($7/bulan) untuk always-on
- Atau gunakan UptimeRobot untuk ping setiap 5 menit (keep alive)

---

## 📊 Monitoring & Logs

### Melihat Logs

1. Buka Render dashboard
2. Klik service Anda
3. Tab **"Logs"** untuk melihat real-time logs
4. Tab **"Events"** untuk melihat deployment history

### Metrics

Tab **"Metrics"** menampilkan:
- CPU usage
- Memory usage
- Request count
- Response time

---

## 🔄 Update Aplikasi

Setiap kali Anda push ke GitHub, Render akan **auto-deploy**:

```bash
# Di local
git add .
git commit -m "Update fitur baru"
git push

# Render akan otomatis detect dan deploy
```

### Manual Deploy

Jika auto-deploy tidak berfungsi:
1. Buka Render dashboard
2. Klik service Anda
3. Klik **"Manual Deploy"** → **"Deploy latest commit"**

---

## 🎨 Custom Domain (Opsional)

### Setup Custom Domain

1. Beli domain (Namecheap, GoDaddy, dll)
2. Di Render dashboard, buka tab **"Settings"**
3. Scroll ke **"Custom Domain"**
4. Klik **"Add Custom Domain"**
5. Masukkan domain Anda (contoh: `healthchecker.com`)
6. Render akan memberikan DNS records
7. Tambahkan DNS records di domain provider Anda:
   - **Type**: CNAME
   - **Name**: @ atau www
   - **Value**: `<your-app>.onrender.com`
8. Tunggu DNS propagation (5-60 menit)
9. SSL certificate akan otomatis di-setup oleh Render

---

## 🔒 Security Best Practices

### 1. Environment Variables

✅ **DO**: Simpan API keys di environment variables
❌ **DON'T**: Hardcode API keys di kode

### 2. HTTPS

✅ Render otomatis menyediakan SSL certificate gratis
✅ Semua traffic akan di-redirect ke HTTPS

### 3. Rate Limiting

Untuk production, tambahkan rate limiting:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    key_func=lambda: request.remote_addr,
    default_limits=["200 per day", "50 per hour"]
)
```

---

## 💰 Pricing

### Free Tier
- ✅ 750 jam/bulan
- ✅ 512 MB RAM
- ✅ Auto-sleep setelah 15 menit
- ✅ SSL certificate
- ✅ Custom domain support
- ⚠️ Cold start 30-60 detik

### Starter ($7/month)
- ✅ Always-on (no sleep)
- ✅ 512 MB RAM
- ✅ Faster deployment
- ✅ Priority support

### Standard ($25/month)
- ✅ 2 GB RAM
- ✅ Better performance
- ✅ More concurrent requests

---

## 📱 Testing Deployment

Setelah deploy, test fitur-fitur berikut:

- [ ] Homepage loading
- [ ] Sistem diagnosa (pilih gejala, submit)
- [ ] BMI calculator
- [ ] Perbandingan tinggi
- [ ] AI Chatbot (jika API key di-set)
- [ ] Admin panel
- [ ] Responsive design (mobile/tablet)

---

## 🎓 Untuk Presentasi UAS

### Demo URL
Gunakan URL Render untuk presentasi:
```
https://health-checker.onrender.com
```

### Tips Presentasi
1. **Buka tab sebelumnya** (5 menit sebelum presentasi) untuk warm-up
2. **Siapkan backup** - Screenshot atau video jika koneksi lambat
3. **Tunjukkan GitHub repo** untuk menunjukkan source code
4. **Explain deployment process** - Auto-deploy dari GitHub

---

## 🆘 Support

Jika ada masalah:

1. **Cek Render Logs**: Dashboard → Logs
2. **Cek GitHub Actions**: Pastikan push berhasil
3. **Render Status**: https://status.render.com
4. **Render Docs**: https://render.com/docs

---

## ✅ Checklist Deployment

- [x] Push ke GitHub
- [x] Buat Procfile
- [x] Update requirements.txt (gunicorn, python-dotenv)
- [x] Update app.py (dynamic PORT)
- [ ] Buat akun Render
- [ ] Connect GitHub repository
- [ ] Konfigurasi web service
- [ ] Set environment variables (GEMINI_API_KEY)
- [ ] Deploy
- [ ] Test aplikasi
- [ ] (Opsional) Setup custom domain

---

**Selamat! Aplikasi Anda sekarang live di internet! 🚀**

**Repository**: https://github.com/Abibsa/Health-Checker
**Live URL**: https://health-checker.onrender.com (setelah deploy)
