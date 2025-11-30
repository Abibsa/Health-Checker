# 🏥 Health Checker - Rule-Based Expert System

Sistem pakar berbasis aturan untuk diagnosis kesehatan dengan integrasi AI chatbot menggunakan Google Gemini.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange.svg)](https://ai.google.dev/)
[![Responsive](https://img.shields.io/badge/Responsive-Mobile%20%7C%20Tablet%20%7C%20Desktop-brightgreen.svg)]()

---

## 📋 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Quick Start](#-quick-start)
- [Struktur Proyek](#-struktur-proyek)
- [Setup AI Chatbot](#-setup-ai-chatbot-opsional)
- [Cara Penggunaan](#-cara-penggunaan)
- [Development](#-development)
- [Troubleshooting](#-troubleshooting)
- [Tech Stack](#-tech-stack)



---

## ✨ Fitur Utama

### 🔍 Sistem Diagnosa Gejala
- ✅ **Rule-Based Expert System** - Diagnosis berdasarkan aturan medis yang terstruktur
- ✅ **90+ Gejala** - Database gejala yang komprehensif
- ✅ **Pencarian Real-time** - Cari gejala dengan mudah menggunakan search bar
- ✅ **Kategorisasi Gejala** - Gejala dikelompokkan berdasarkan sistem tubuh:
  - 🫁 Pernapasan
  - 🧠 Neurologis
  - 🍽️ Pencernaan
  - 👁️ Indra
  - 🩹 Kulit & Alergi
  - 💪 Sistemik
- ✅ **Filter Kategori** - Tab untuk memfilter gejala berdasarkan kategori
- ✅ **Visual Feedback** - Animasi smooth dan highlight untuk gejala yang dipilih
- ✅ **Keyboard Shortcuts** - Tekan `Ctrl+K` untuk fokus ke search bar
- ✅ **Match Percentage** - Tingkat kesesuaian gejala dengan kondisi
- ✅ **Priority System** - Rekomendasi berdasarkan tingkat prioritas (Darurat, Tinggi, Sedang, Rendah)

### ⚖️ Kalkulator BMI
- ✅ **Perhitungan BMI Akurat** - Berdasarkan standar WHO
- ✅ **Dual Unit Support** - Metric (kg/cm) dan Imperial (lbs/inches)
- ✅ **Kategori BMI** - Underweight, Normal, Overweight, Obesity
- ✅ **Rentang Berat Ideal** - Rekomendasi berat badan ideal
- ✅ **BMR Calculator** - Estimasi kebutuhan kalori harian
- ✅ **Health Risks** - Informasi risiko kesehatan berdasarkan kategori BMI
- ✅ **Rekomendasi Kesehatan** - Saran untuk mencapai berat badan ideal
- ✅ **Visual Classification** - Tabel klasifikasi BMI dengan highlight kategori aktif

### 📊 Perbandingan Tinggi Badan
- ✅ **Visualisasi Interaktif** - Grafik perbandingan tinggi dengan silhouette
- ✅ **Multi-Person Comparison** - Bandingkan hingga 4 orang sekaligus
- ✅ **Gender Differentiation** - Silhouette berbeda untuk pria dan wanita
- ✅ **Height Scale** - Skala tinggi yang akurat
- ✅ **Responsive Chart** - Grafik menyesuaikan dengan ukuran layar

### 💬 AI Chatbot
- ✅ **Google Gemini Integration** - Powered by Gemini 1.5 Flash
- ✅ **Natural Conversation** - Percakapan seperti dengan manusia
- ✅ **Context Awareness** - Memahami konteks percakapan
- ✅ **Symptom Detection** - Deteksi gejala dari teks natural
- ✅ **Health Recommendations** - Saran kesehatan yang personal
- ✅ **Fallback System** - Tetap berfungsi tanpa AI (rule-based)
- ✅ **Chat Widget** - Widget chat yang mudah diakses di setiap halaman

### 🎨 User Interface
- ✅ **Modern Dark Theme** - Desain gelap yang nyaman di mata
- ✅ **Gradient Accents** - Warna gradien yang vibrant
- ✅ **Smooth Animations** - Transisi dan animasi yang halus
- ✅ **Glassmorphism** - Efek kaca modern dengan backdrop blur
- ✅ **Hover Effects** - Feedback visual saat hover
- ✅ **Loading States** - Indikator loading yang jelas

### 📱 Responsive Design
- ✅ **Mobile First** - Dioptimalkan untuk perangkat mobile
- ✅ **Breakpoints Komprehensif**:
  - 📱 Mobile (0-480px)
  - 📱 Large Phone (481-768px)
  - 📱 Tablet (769-1024px)
  - 💻 Desktop (1025px+)
- ✅ **Touch Optimized** - Touch target minimal 44px untuk perangkat sentuh
- ✅ **Landscape Support** - Layout khusus untuk orientasi landscape
- ✅ **iOS Zoom Prevention** - Font size 16px untuk mencegah auto-zoom
- ✅ **Horizontal Scroll** - Smooth scrolling untuk category tabs di mobile

### 🔐 Admin Panel
- ✅ **Knowledge Base Viewer** - Lihat semua rules dalam sistem
- ✅ **Rule Statistics** - Statistik jumlah rules dan gejala
- ✅ **Detailed Rule Info** - Informasi lengkap setiap rule:
  - Rule ID & Priority
  - Conditions (gejala & BMI requirement)
  - Conclusions & Advice
  - Health recommendations

---

## 🚀 Quick Start

### 1. Setup Project

Clone repository dan install dependencies:

```bash
git clone https://github.com/Abibsa/Health-Checker.git
cd Health-Checker
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi

```bash
python app.py
```

Buka browser: **http://localhost:5000**

**That's it!** Aplikasi sudah bisa digunakan dengan rule-based system.

> **Note**: Untuk mengaktifkan AI chatbot, lihat [Setup AI Chatbot](#-setup-ai-chatbot-opsional)

---

## 📁 Struktur Proyek

```
health-checker-rule-based/
├── 📄 app.py                    # ⭐ Entry point aplikasi Flask
├── 📄 requirements.txt          # Python dependencies
├── 📄 .env.example              # Template environment variables
├── 📄 .gitignore                # Git ignore rules
├── 📄 README.md                 # Dokumentasi utama
├── 📄 CHANGELOG.md              # Catatan perubahan
│
├── 📁 src/                      # 🔧 Source code utama
│   ├── ai_chat.py              # Google Gemini AI integration
│   ├── health_metrics.py       # BMI calculator & health metrics
│   ├── inference_engine.py     # Rule-based inference engine
│   ├── nlp_processor.py        # NLP untuk deteksi gejala
│   └── rules.py                # Definisi rules
│
├── 📁 scripts/                  # 🛠️ Utility scripts
│   ├── make_pdfs_direct.py     # ⭐ PDF generator (recommended)
│   ├── setup_api_key.bat       # Setup API key (Windows CMD)
│   └── setup_api_key.ps1       # Setup API key (PowerShell)
│
├── 📁 templates/                # 🎨 HTML templates (Flask)
│   ├── base.html               # Base template dengan navbar & footer
│   ├── index.html              # Homepage
│   ├── diagnose.html           # Form diagnosis dengan search & filter
│   ├── result.html             # Hasil diagnosis
│   ├── bmi.html                # Kalkulator BMI
│   ├── compare.html            # Perbandingan tinggi badan
│   ├── chat.html               # Chatbot interface
│   ├── admin.html              # Admin panel
│   └── metrics.html            # Metrics page
│
├── 📁 static/                   # 🎨 Static files (CSS, JS)
│   ├── css/
│   │   ├── style.css           # Main stylesheet (responsive)
│   │   ├── chat-widget.css     # Chat widget styling
│   │   └── footer.css          # Footer styling
│   └── js/
│       ├── main.js             # Main JavaScript
│       └── chat-widget.js      # Chat widget functionality
│
├── 📁 data/                     # 💾 Data files
│   └── rules.json              # Knowledge base rules
│
├── 📁 tests/                    # 🧪 Unit tests
│   └── test_gemini.py          # Test Gemini integration
│
├── 📁 docs/                     # 📚 Documentation (Markdown)
│   ├── AI_SETUP.md
│   ├── chatbot_documentation.md
│   ├── technical_manual.md
│   └── user_manual.md
│
└── 📁 docs_pdf/                 # 📄 Generated PDF documentation
```

### Penjelasan Folder Utama

| Folder | Deskripsi |
|--------|-----------|
| **`src/`** | Semua source code Python inti aplikasi |
| **`scripts/`** | Utility scripts (PDF generator, setup tools) |
| **`templates/`** | HTML templates untuk Flask |
| **`static/`** | CSS, JavaScript, dan assets |
| **`data/`** | Knowledge base (rules.json) |
| **`docs/`** | Dokumentasi Markdown |
| **`docs_pdf/`** | Dokumentasi PDF (auto-generated) |

---

## 🤖 Setup AI Chatbot (Opsional)

AI Chatbot menggunakan **Google Gemini API** (GRATIS!). Ikuti langkah berikut:

### 1️⃣ Dapatkan API Key

1. Buka: **https://aistudio.google.com/app/apikey**
2. Login dengan akun Google
3. Klik **"Create API Key"**
4. **Copy** API key (contoh: `AIzaSyA...`)

### 2️⃣ Setup API Key

**Cara Otomatis (Recommended):**

```powershell
# PowerShell
.\scripts\setup_api_key.ps1

# Atau double-click:
scripts\setup_api_key.bat
```

**Cara Manual:**

```powershell
# Buat file .env di root folder
GEMINI_API_KEY=AIzaSyB1yplt-hF3ucUZd5vN3xhupY40VF9udhs
```

### 3️⃣ Restart Aplikasi

```bash
python app.py
```

### ✅ Verifikasi AI Aktif

Saat aplikasi start, cek console:
- ✅ **AI Aktif**: Tidak ada warning
- ⚠️ **Fallback**: Muncul "Warning: AI Chat tidak tersedia"

Test di chat widget:
1. Klik tombol chat di pojok kanan bawah
2. Ketik: "Halo, siapa kamu?"
3. Jika AI aktif, bot akan menjawab dengan natural

### 🆚 AI vs Rule-Based

| Fitur | 🤖 AI (Gemini) | 📋 Rule-Based |
|-------|----------------|---------------|
| **Percakapan** | Natural, seperti manusia | Template response |
| **Pemahaman** | Memahami konteks | Keyword matching |
| **Follow-up** | Bisa tanya balik | Tidak bisa |
| **Fleksibilitas** | Sangat fleksibel | Terbatas |
| **Internet** | Perlu | Tidak perlu |
| **Biaya** | Gratis (60 req/min) | Gratis unlimited |

### 📊 Batasan Gratis

- ✅ 60 requests/menit
- ✅ 1,500 requests/hari
- ✅ Unlimited untuk development

---

## 💻 Cara Penggunaan

### 1. Sistem Diagnosa

1. Buka **http://localhost:5000/diagnosa**
2. **Cari gejala** menggunakan search bar:
   - Ketik kata kunci (contoh: "batuk", "demam", "pusing")
   - Hasil akan ter-highlight secara real-time
   - Tekan `Ctrl+K` untuk fokus ke search bar
   - Tekan `Esc` untuk clear search
3. **Filter kategori** dengan klik tab kategori:
   - Semua (tampilkan semua gejala)
   - Pernapasan 🫁
   - Neurologis 🧠
   - Pencernaan 🍽️
   - Indra 👁️
   - Kulit & Alergi 🩹
   - Sistemik 💪
4. **Pilih gejala** yang Anda alami:
   - Klik checkbox atau klik card gejala
   - Gejala yang dipilih akan ter-highlight dengan gradient merah
   - Counter akan menampilkan jumlah gejala yang dipilih
   - Tombol "Hapus Semua" akan muncul jika ada gejala terpilih
5. (Opsional) Masukkan **berat & tinggi** untuk analisis BMI
6. Klik **"Periksa Sekarang"**
7. Lihat hasil diagnosis dengan:
   - Tingkat kesesuaian (match percentage)
   - Prioritas tindakan (Darurat/Tinggi/Sedang/Rendah)
   - Gejala yang sesuai
   - Gejala tambahan yang mungkin relevan
   - Rekomendasi kesehatan
8. Gunakan tombol **"Hapus Semua"** untuk reset pilihan

### 2. Kalkulator BMI

1. Buka **http://localhost:5000/bmi**
2. Masukkan **nama** (opsional), **berat**, dan **tinggi**
3. Pilih **unit** (Metric/Imperial)
4. Klik **"Hitung BMI"**
5. Lihat hasil lengkap dengan:
   - BMI value dan kategori
   - Berat dan tinggi dalam berbagai unit
   - BMR (Basal Metabolic Rate)
   - Rentang berat badan ideal
   - Target berat badan (jika perlu naik/turun)
   - Risiko kesehatan berdasarkan kategori
   - Rekomendasi kesehatan
   - Klasifikasi BMI WHO dengan highlight kategori aktif

### 3. Perbandingan Tinggi

1. Buka **http://localhost:5000/compare**
2. Masukkan **data Anda**:
   - Nama
   - Tinggi badan
   - Gender (Pria/Wanita)
3. Tambahkan **profil pembanding** (maksimal 3 orang)
4. Klik **"Bandingkan"**
5. Lihat visualisasi interaktif:
   - Silhouette berbeda untuk pria (biru) dan wanita (pink)
   - Skala tinggi yang akurat
   - Label nama dan tinggi di atas setiap silhouette
   - Hover untuk efek visual

### 4. AI Chatbot

1. Klik **tombol chat** (💬) di pojok kanan bawah
2. Ketik pertanyaan atau gejala Anda
3. Bot akan merespons secara natural
4. Contoh pertanyaan:
   - "Saya demam dan batuk, apa yang harus saya lakukan?"
   - "Bagaimana cara menurunkan berat badan?"
   - "Apa itu BMI dan bagaimana cara menghitungnya?"
   - "Saya pusing dan mual, kondisi apa ini?"
5. Bot dapat:
   - Mendeteksi gejala dari teks natural
   - Memberikan rekomendasi kesehatan
   - Menjawab pertanyaan umum tentang kesehatan
   - Melakukan follow-up questions

### 5. Admin Panel

1. Buka **http://localhost:5000/admin**
2. Lihat statistik knowledge base:
   - Total rules
   - Total gejala unik
   - Rules berdasarkan prioritas
3. Browse semua **rules** dalam knowledge base
4. Informasi setiap rule:
   - Rule ID & Priority
   - Conditions (gejala & BMI requirement)
   - Conclusions & Advice
   - Health recommendations

---

## 🛠️ Development

### Generate PDF Documentation

```bash
python scripts/make_pdfs_direct.py
```

PDF akan di-generate di folder `docs_pdf/`

### Run Tests

```bash
pytest tests/
```

### Update Requirements

```bash
pip freeze > requirements.txt
```

### Project Structure

File utama yang perlu diketahui:

- **`app.py`** - Main Flask application, routing
- **`src/inference_engine.py`** - Rule-based logic
- **`src/ai_chat.py`** - Gemini AI integration
- **`src/nlp_processor.py`** - NLP untuk deteksi gejala
- **`src/health_metrics.py`** - BMI calculator & health metrics
- **`data/rules.json`** - Knowledge base

### Adding New Rules

Edit `data/rules.json`:

```json
{
  "id": "rule_new",
  "priority": 2,
  "conditions": {
    "symptoms": ["symptom1", "symptom2"],
    "bmi_category": "Overweight"
  },
  "conclusion": "Kondisi baru",
  "advice": "Saran untuk kondisi baru"
}
```

### Customizing Styles

Edit `static/css/style.css`:
- Responsive breakpoints di bagian bawah file
- CSS variables di `:root` untuk warna tema
- Media queries untuk berbagai ukuran layar

---

## 🆘 Troubleshooting

### Aplikasi tidak bisa dijalankan

**Error**: `ModuleNotFoundError`

**Solusi**:
```bash
pip install -r requirements.txt
```

### AI Chatbot tidak aktif

**Gejala**: Warning "AI Chat tidak tersedia"

**Solusi**:
1. Pastikan API key sudah di-set
2. Cek file `.env` atau environment variable
3. Verifikasi: `echo $env:GEMINI_API_KEY` (PowerShell)
4. Restart aplikasi

### "API key not valid"

**Solusi**:
1. Cek API key di Google AI Studio
2. Pastikan tidak ada spasi di awal/akhir
3. Generate API key baru jika perlu

### Chatbot lambat merespons

**Penyebab**: Request ke Gemini API memerlukan internet

**Solusi**:
- Cek koneksi internet
- Tunggu 2-5 detik (normal)
- Gunakan rule-based jika offline

### Port 5000 sudah digunakan

**Solusi**:
```python
# Edit app.py, ubah port:
app.run(host='0.0.0.0', port=5001, debug=True)
```

### Layout tidak responsif di mobile

**Solusi**:
1. Clear browser cache
2. Hard refresh (Ctrl+Shift+R)
3. Pastikan viewport meta tag ada di base.html

### Category tabs tidak bisa di-scroll di mobile

**Solusi**:
- Swipe horizontal pada tab area
- Tabs sudah dioptimalkan untuk touch scrolling

### Import Error setelah restrukturisasi

**Solusi**:
Pastikan import menggunakan `src.`:
```python
from src.inference_engine import infer
from src.ai_chat import HealthChatAI
```

---

## 🔧 Tech Stack

### Backend
- **Flask 3.0+** - Web framework
- **Python 3.8+** - Programming language
- **Google Gemini API** - AI chatbot (Gemini 1.5 Flash)

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (Dark theme, Glassmorphism, Gradients)
- **JavaScript (ES6+)** - Interactivity

### Libraries
- **google-generativeai** - Gemini integration
- **python-dotenv** - Environment variables
- **markdown2** - Markdown to HTML
- **wkhtmltopdf** - PDF generation

### Data
- **JSON** - Knowledge base storage
- **Rule-based system** - Expert system logic

### Design Features
- **Responsive Design** - Mobile-first approach
- **Dark Theme** - Modern dark UI
- **Gradient Accents** - Vibrant color gradients
- **Glassmorphism** - Backdrop blur effects
- **Smooth Animations** - CSS transitions

---

## 📚 Dokumentasi Lengkap

Dokumentasi tersedia dalam 2 format:

### Markdown (di folder `docs/`)
- `AI_SETUP.md` - Setup guide untuk AI
- `chatbot_documentation.md` - Dokumentasi chatbot
- `technical_manual.md` - Manual teknis sistem
- `user_manual.md` - Panduan pengguna

### PDF (di folder `docs_pdf/`)
- `AI_SETUP.pdf`
- `chatbot_documentation.pdf`
- `technical_manual.pdf`
- `user_manual.pdf`

Generate ulang PDF:
```bash
python scripts/make_pdfs_direct.py
```

---

## 🎓 Untuk Presentasi UAS

### Highlight Points:

1. **Hybrid System** - Kombinasi AI + Rule-Based (best of both worlds)
2. **Fallback Mechanism** - Tetap berfungsi tanpa internet
3. **User Experience** - Natural conversation vs checkbox
4. **Innovation** - Menggunakan teknologi AI terkini (Gemini 1.5 Flash)
5. **Practical** - Gratis dan mudah di-deploy
6. **Well-Structured** - Kode terorganisir dan scalable
7. **Responsive Design** - Optimal di semua perangkat (mobile, tablet, desktop)
8. **Modern UI** - Dark theme dengan glassmorphism dan gradient accents

### Demo Flow:

1. **Homepage** - Tunjukkan overview fitur dan navigasi
2. **Sistem Diagnosa** - Demo search, filter, dan pemilihan gejala
3. **Hasil Diagnosis** - Tampilkan prioritas, match percentage, dan rekomendasi
4. **BMI Calculator** - Hitung BMI dengan visualisasi lengkap
5. **Perbandingan Tinggi** - Visualisasi interaktif perbandingan tinggi
6. **AI Chatbot** - Percakapan natural dengan bot
7. **Admin Panel** - Tunjukkan knowledge base dan statistik
8. **Responsive Demo** - Buka di mobile/tablet untuk tunjukkan responsivitas

### Key Features to Emphasize:

- ✅ 90+ gejala dengan kategorisasi
- ✅ Real-time search dengan highlighting
- ✅ Match percentage untuk akurasi diagnosis
- ✅ Priority system (Darurat/Tinggi/Sedang/Rendah)
- ✅ BMI calculator dengan health risks & recommendations
- ✅ AI chatbot dengan Gemini 1.5 Flash
- ✅ Fully responsive (mobile-first design)
- ✅ Modern UI dengan dark theme

---

## 🔒 Keamanan

⚠️ **JANGAN** commit API key ke Git!

File `.gitignore` sudah di-setup untuk mengabaikan:
- `.env`
- `__pycache__/`
- `.pytest_cache/`
- `*.pyc`

Jika tidak sengaja commit API key:
1. Revoke API key di Google AI Studio
2. Generate API key baru
3. Update environment variable
4. Remove dari Git history (jika perlu)

---

## 📝 License

Educational project untuk mata kuliah **Sistem Cerdas**.

---

## 👥 Contributors

- **Your Name** - Semester 5, Sistem Cerdas

---

## 📞 Support

Jika ada masalah:
1. Cek [Troubleshooting](#-troubleshooting)
2. Lihat console output untuk error message
3. Baca dokumentasi di folder `docs/`
4. Cek CHANGELOG.md untuk update terbaru

---


## 🚀 Recent Updates (v2.1.0)

- ✅ Comprehensive responsive design untuk semua perangkat
- ✅ Mobile-first approach dengan breakpoints optimal
- ✅ Touch-optimized UI dengan minimum 44px touch targets
- ✅ Improved category tabs dengan horizontal scroll
- ✅ Better form layouts untuk mobile
- ✅ Landscape orientation support
- ✅ Print styles untuk mencetak halaman
- ✅ **Ready for deployment** - Procfile dan production config

Lihat [CHANGELOG.md](CHANGELOG.md) untuk detail lengkap.

---

**Note**: Aplikasi ini untuk tujuan edukasi. Untuk diagnosis medis yang akurat, konsultasikan dengan tenaga medis profesional.

**Happy Coding!** 🚀
