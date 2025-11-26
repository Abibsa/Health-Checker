# Technical Manual — Health Checker

## Ringkasan

- Bahasa: Python 3
- Framework: Flask
- Inference: Rule-based (load dari `data/rules.json`) + dukungan Body Metrics (BMI).

## Struktur

(Lihat README pada root)

## Menambah/Mengubah Rule

- Edit `data/rules.json` tambahkan objek rule sesuai format.
- Opsional: tambahkan properti `bmi_category` (`Underweight|Normal|Overweight|Obesity`) untuk mensyaratkan kategori BMI tertentu.
- Restart aplikasi (atau implementasi reload bila perlu).

## Modul Body Metrics

- `health_metrics.py` menyediakan konversi unit, kalkulasi BMI, dan kategorisasi WHO.
- Form utama (`index.html`) serta halaman `/metrics` memungkinkan input berat/tinggi dalam unit metric/imperial.
- Endpoint `/check` mengirim `metrics` ke `infer()`; rules dengan `bmi_category` hanya aktif jika kategori cocok.
- Tambahan pengujian berada di `tests/test_health_metrics.py`.

## Konversi Manual ke PDF

- Opsional: gunakan pandoc: pandoc docs/user_manual.md -o docs_pdf/user_manual.pdf
- Atau gunakan make_pdfs.py yang disertakan (membutuhkan pypandoc dan pandoc).

## Deployment

- Gunakan Gunicorn + Nginx untuk produksi. Contoh: gunicorn -w 4 app:app.
