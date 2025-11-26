# 📝 CATATAN PERUBAHAN

Semua perubahan penting pada proyek ini akan didokumentasikan dalam file ini.

---

## [2.1.0] - 2025-11-26

### 🎨 Peningkatan Responsivitas

#### Ditambahkan
- ✅ **Media queries komprehensif** untuk berbagai ukuran layar
- ✅ **Breakpoint mobile** (0-480px) dengan layout yang dioptimalkan
- ✅ **Breakpoint tablet** (481px-768px dan 769px-1024px)
- ✅ **Breakpoint desktop** (1025px+)
- ✅ **Touch target improvements** untuk perangkat sentuh
- ✅ **Landscape orientation support** untuk tampilan horizontal
- ✅ **Print styles** untuk mencetak halaman

#### Diperbaiki
- 🐛 **Navigasi mobile** - Sekarang stack secara vertikal dengan baik
- 🐛 **Category tabs** - Scroll horizontal yang mulus di mobile
- 🐛 **Symptom grid** - 1 kolom di mobile, 2 kolom di tablet
- 🐛 **Form inputs** - Font size 16px untuk mencegah zoom di iOS
- 🐛 **Height chart** - Layout responsif untuk semua ukuran layar
- 🐛 **BMI classification rows** - Stack vertikal di mobile
- 🐛 **Tables** - Horizontal scroll di layar kecil

#### Diubah
- 🔄 **Container padding** - Dikurangi di mobile untuk lebih banyak ruang
- 🔄 **Typography scaling** - Ukuran font yang lebih kecil di mobile
- 🔄 **Hero section** - Single column di mobile dan tablet
- 🔄 **Feature cards** - Grid responsif berdasarkan ukuran layar
- 🔄 **Search placeholder** - Teks lebih pendek di mobile

---

## [2.0.0] - 2025-11-25

### 🎯 Restrukturisasi Besar

#### Ditambahkan
- ✅ **Struktur folder terorganisir** dengan `src/` dan `scripts/`
- ✅ **README.md komprehensif** - Semua dokumentasi dalam satu tempat
- ✅ **`.gitignore`** - Aturan Git ignore yang tepat
- ✅ **Kartu gejala yang dapat diklik** - UX lebih baik untuk form diagnosis
- ✅ **Generator dokumentasi PDF** - Otomatis membuat PDF dari Markdown

#### Diubah
- 🔄 **Memindahkan source code** ke folder `src/`
- 🔄 **Memindahkan utility scripts** ke folder `scripts/`
- 🔄 **Memperbarui import paths** untuk menggunakan `src.*`
- 🔄 **Mengkonsolidasikan dokumentasi** ke dalam satu README.md
- 🔄 **Meningkatkan organisasi proyek** - Dari 17 file root menjadi 6

#### Dihapus
- ❌ File dokumentasi yang redundan (AI_CHATBOT_README.md, PROJECT_STRUCTURE.md, dll.)
- ❌ Beberapa versi PDF generator (hanya menyimpan `make_pdfs_direct.py`)

### 📁 Struktur Baru

```
Sebelum: 17 file di root (berantakan)
Setelah:  6 file di root (rapi)
          + Folder terorganisir (src/, scripts/, dll.)
```

### 🎨 Peningkatan UI/UX

- ✅ Kartu gejala sekarang dapat diklik di mana saja (tidak hanya checkbox)
- ✅ Feedback cursor yang lebih baik (pointer saat hover)
- ✅ Pengalaman pengguna yang ditingkatkan pada form diagnosis

---

## [1.0.0] - 2025-11-24

### 🚀 Rilis Awal

#### Fitur
- ✅ **Sistem pakar berbasis aturan** untuk diagnosis kesehatan
- ✅ **Kalkulator BMI** dengan metrik kesehatan detail
- ✅ **Perbandingan tinggi** dengan visualisasi interaktif
- ✅ **Chatbot AI** terintegrasi dengan Google Gemini
- ✅ **Pemrosesan NLP** untuk deteksi gejala
- ✅ **Panel admin** untuk melihat basis pengetahuan
- ✅ **Tema gelap** desain UI modern
- ✅ **Desain responsif** untuk perangkat mobile

#### Tech Stack
- Flask (Framework web Python)
- Google Gemini API (Chatbot AI)
- HTML/CSS/JavaScript (Frontend)
- JSON (Basis pengetahuan)

---

## Legenda

- ✅ Ditambahkan
- 🔄 Diubah
- ❌ Dihapus
- 🐛 Diperbaiki
- 🎨 UI/UX
- 📚 Dokumentasi
- 🔒 Keamanan
