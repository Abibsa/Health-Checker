# Chatbot AI - Health Checker

## Deskripsi
Fitur chatbot AI yang memungkinkan pengguna untuk berinteraksi dengan sistem pakar menggunakan bahasa natural (bahasa Indonesia).

## Cara Kerja

### 1. Natural Language Processing (NLP)
- **Deteksi Gejala**: Sistem menggunakan keyword matching untuk mendeteksi gejala dari teks input pengguna
- **Ekstraksi BMI**: Sistem dapat mengekstrak informasi berat dan tinggi badan dari teks
- **Pattern Matching**: Menggunakan regex untuk mencocokkan kata kunci dengan database gejala

### 2. Integrasi dengan Inference Engine
- Gejala yang terdeteksi dikirim ke inference engine yang sama dengan diagnosa manual
- Hasil analisis ditampilkan dalam format yang mudah dibaca
- Top 3 hasil ditampilkan untuk menghindari information overload

### 3. Response Generation
- Sistem menghasilkan response natural dalam bahasa Indonesia
- Menampilkan gejala yang terdeteksi
- Menampilkan hasil diagnosa dengan prioritas
- Menyertakan disclaimer medis

## Fitur Utama

### 1. Chat Interface
- UI modern dengan desain chat bubble
- Real-time typing indicator
- Auto-scroll ke pesan terbaru
- Quick action buttons untuk gejala umum

### 2. Deteksi Gejala Otomatis
Sistem dapat mendeteksi berbagai gejala dari teks, contoh:
- "Saya merasa demam dan batuk" → Deteksi: Demam, Batuk
- "Pusing dan mual sejak tadi pagi" → Deteksi: Pusing, Mual
- "Sakit kepala parah" → Deteksi: Sakit Kepala

### 3. Ekstraksi BMI
Sistem dapat mengekstrak informasi BMI dari teks, contoh:
- "Berat badan 70 kg, tinggi 170 cm" → BMI dihitung otomatis
- "BB 65, TB 165" → BMI dihitung otomatis

### 4. Riwayat Percakapan
- Menyimpan riwayat percakapan dalam session
- Dapat dihapus dengan tombol clear

## Teknologi

### Backend
- **Flask**: Web framework
- **Python Regex**: Pattern matching untuk NLP
- **JSON**: Format data untuk komunikasi API

### Frontend
- **HTML/CSS**: UI chatbot
- **JavaScript**: Interaksi real-time
- **Fetch API**: Komunikasi dengan backend

## API Endpoint

### POST /chat/api
Request:
```json
{
  "message": "Saya merasa demam dan batuk"
}
```

Response:
```json
{
  "success": true,
  "response": "Formatted response text",
  "detected_symptoms": ["Demam", "Batuk"],
  "results": [...]
}
```

## Contoh Penggunaan

### 1. Gejala Sederhana
**Input**: "Saya merasa demam dan batuk"
**Output**: 
- Deteksi gejala: Demam, Batuk
- Hasil diagnosa: Infeksi Pernapasan (prioritas 2)
- Saran: Istirahat, minum air putih, konsultasi dokter jika memburuk

### 2. Gejala dengan BMI
**Input**: "Berat badan 90 kg, tinggi 165 cm, sering pusing"
**Output**:
- Deteksi gejala: Pusing
- BMI: 33.1 (Obesity)
- Hasil diagnosa: Risiko hipertensi (prioritas 1)
- Saran: Segera konsultasi dokter, diet sehat

### 3. Gejala Darurat
**Input**: "Demam tinggi 40 derajat, sesak napas"
**Output**:
- Deteksi gejala: Demam, Sesak Napas
- Hasil diagnosa: Kondisi Darurat (prioritas 0)
- Saran: 🚨 SEGERA KE UGD/RUMAH SAKIT

## Keunggulan

1. **User-Friendly**: Tidak perlu memilih dari checklist, cukup ketik gejala
2. **Natural**: Menggunakan bahasa sehari-hari
3. **Cepat**: Response real-time
4. **Akurat**: Menggunakan inference engine yang sama dengan diagnosa manual
5. **Offline**: Tidak memerlukan API eksternal (OpenAI, Gemini, dll)

## Keterbatasan

1. **Keyword-Based**: Hanya mendeteksi gejala yang ada dalam database keyword
2. **Bahasa Indonesia**: Hanya mendukung bahasa Indonesia
3. **Konteks Terbatas**: Tidak memahami konteks percakapan sebelumnya
4. **Tidak Belajar**: Tidak menggunakan machine learning, hanya rule-based

## Pengembangan Lebih Lanjut

1. **Fuzzy Matching**: Mendeteksi typo dan variasi kata
2. **Context Awareness**: Memahami konteks percakapan
3. **Multi-turn Conversation**: Bertanya follow-up questions
4. **Voice Input**: Integrasi dengan speech-to-text
5. **Sentiment Analysis**: Mendeteksi tingkat keparahan dari tone

## Disclaimer

Chatbot ini adalah sistem pakar untuk tujuan edukasi dan informasi awal. Hasil diagnosa **BUKAN pengganti saran medis profesional**. Untuk kondisi serius atau darurat, segera konsultasi dengan dokter atau pergi ke rumah sakit.
