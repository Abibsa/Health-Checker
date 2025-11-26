from typing import Tuple


KG_PER_POUND = 0.45359237
M_PER_CM = 0.01
M_PER_INCH = 0.0254


def kg_from_lb(pounds: float) -> float:
    return pounds * KG_PER_POUND


def m_from_cm(cm: float) -> float:
    return cm * M_PER_CM


def m_from_in(inches: float) -> float:
    return inches * M_PER_INCH


def calculate_bmi(weight: float, height: float, units: str = "metric") -> Tuple[float, float]:
    """Return BMI (raw and rounded to 2 decimals) given weight & height."""
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if height <= 0:
        raise ValueError("Height must be greater than zero")

    units = (units or "metric").lower()
    if units == "imperial":
        weight_kg = kg_from_lb(weight)
        height_m = m_from_in(height)
    else:
        weight_kg = float(weight)
        height_m = m_from_cm(height)

    if height_m <= 0:
        raise ValueError("Height (in meters) must be greater than zero")

    bmi = weight_kg / (height_m ** 2)
    return bmi, round(bmi, 2)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Normal"
    if bmi < 30.0:
        return "Overweight"
    return "Obesity"


def get_ideal_weight_range(height_m: float) -> Tuple[float, float]:
    """Calculate ideal weight range (BMI 18.5-24.9) in kg."""
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return round(min_weight, 1), round(max_weight, 1)


def calculate_weight_difference(current_weight_kg: float, ideal_min: float, ideal_max: float) -> dict:
    """Calculate how much weight needs to be gained or lost."""
    if current_weight_kg < ideal_min:
        diff = ideal_min - current_weight_kg
        return {"type": "gain", "amount": round(diff, 1), "target": round(ideal_min, 1)}
    elif current_weight_kg > ideal_max:
        diff = current_weight_kg - ideal_max
        return {"type": "lose", "amount": round(diff, 1), "target": round(ideal_max, 1)}
    else:
        return {"type": "ideal", "amount": 0, "target": None}


def get_bmi_category_details(bmi: float) -> dict:
    """Get detailed information about BMI category including health risks and recommendations."""
    category = bmi_category(bmi)
    
    if bmi < 18.5:
        return {
            "category": "Underweight",
            "description": "Berat badan di bawah normal",
            "health_risks": [
                "Kekurangan nutrisi dan energi",
                "Sistem kekebalan tubuh melemah",
                "Risiko osteoporosis meningkat",
                "Gangguan pertumbuhan dan perkembangan (pada remaja)",
                "Masalah kesuburan"
            ],
            "recommendations": [
                "Konsultasi dengan ahli gizi untuk rencana penambahan berat badan yang sehat",
                "Tingkatkan asupan kalori dengan makanan bergizi seimbang",
                "Lakukan latihan kekuatan untuk membangun massa otot",
                "Makan lebih sering dalam porsi kecil",
                "Hindari makanan cepat saji, pilih makanan padat nutrisi"
            ],
            "severity": "moderate"
        }
    elif bmi < 25.0:
        return {
            "category": "Normal",
            "description": "Berat badan ideal",
            "health_risks": [
                "Risiko kesehatan minimal",
                "Tingkat energi optimal",
                "Fungsi metabolik yang baik"
            ],
            "recommendations": [
                "Pertahankan pola makan seimbang dan bergizi",
                "Lakukan aktivitas fisik rutin (minimal 150 menit per minggu)",
                "Jaga pola tidur yang cukup (7-9 jam per hari)",
                "Hindari kebiasaan merokok dan konsumsi alkohol berlebihan",
                "Lakukan pemeriksaan kesehatan rutin"
            ],
            "severity": "low"
        }
    elif bmi < 30.0:
        return {
            "category": "Overweight",
            "description": "Kelebihan berat badan",
            "health_risks": [
                "Peningkatan risiko penyakit jantung",
                "Risiko diabetes tipe 2",
                "Tekanan darah tinggi (hipertensi)",
                "Masalah sendi dan tulang",
                "Sleep apnea (gangguan tidur)",
                "Risiko stroke meningkat"
            ],
            "recommendations": [
                "Mulai program penurunan berat badan dengan pendekatan bertahap",
                "Kurangi asupan kalori harian (500-750 kalori defisit)",
                "Tingkatkan aktivitas fisik (cardio dan latihan kekuatan)",
                "Konsultasi dengan ahli gizi untuk rencana diet yang tepat",
                "Pantau berat badan secara rutin",
                "Hindari diet ekstrem, pilih perubahan gaya hidup berkelanjutan"
            ],
            "severity": "moderate"
        }
    else:
        obesity_class = "Obesitas Kelas I" if bmi < 35.0 else ("Obesitas Kelas II" if bmi < 40.0 else "Obesitas Kelas III (Ekstrem)")
        return {
            "category": "Obesity",
            "description": f"Obesitas ({obesity_class})",
            "health_risks": [
                "Risiko sangat tinggi penyakit jantung dan stroke",
                "Diabetes tipe 2 dengan komplikasi",
                "Tekanan darah tinggi yang sulit dikontrol",
                "Sleep apnea berat",
                "Penyakit hati berlemak",
                "Risiko kanker tertentu meningkat",
                "Masalah sendi dan mobilitas",
                "Depresi dan masalah kesehatan mental"
            ],
            "recommendations": [
                "Segera konsultasi dengan dokter atau ahli gizi profesional",
                "Program penurunan berat badan yang diawasi medis",
                "Evaluasi kondisi kesehatan menyeluruh",
                "Pertimbangkan intervensi medis jika diperlukan",
                "Dukungan psikologis untuk perubahan gaya hidup",
                "Aktivitas fisik yang disesuaikan dengan kondisi",
                "Monitoring kesehatan rutin"
            ],
            "severity": "high"
        }


def estimate_bmr(weight_kg: float, height_cm: float, age: int = 30, gender: str = "male") -> float:
    """Estimate Basal Metabolic Rate using Mifflin-St Jeor Equation."""
    # Using average age 30 if not provided
    if gender.lower() == "female":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    return round(bmr, 0)
