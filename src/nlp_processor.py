"""
NLP Processor untuk Health Checker Chatbot
Mendeteksi gejala dari input teks pengguna menggunakan keyword matching
"""
import re
from typing import List, Set, Tuple


class SymptomDetector:
    """Deteksi gejala dari teks input pengguna"""
    
    def __init__(self, symptoms_map):
        """
        symptoms_map: list of tuples (symptom_key, symptom_label_indonesian)
        """
        self.symptoms_map = symptoms_map
        self.keyword_patterns = self._build_keyword_patterns()
    
    def _build_keyword_patterns(self):
        """Membangun pola keyword untuk setiap gejala"""
        patterns = {}
        
        # Mapping manual untuk keyword yang lebih natural
        keyword_mapping = {
            "fever": ["demam", "panas", "meriang"],
            "cough": ["batuk"],
            "sore_throat": ["sakit tenggorokan", "tenggorokan sakit", "radang tenggorokan"],
            "shortness_of_breath": ["sesak napas", "sesak", "napas pendek", "sulit bernapas"],
            "runny_nose": ["hidung berair", "meler", "ingus"],
            "congested_nose": ["hidung tersumbat", "hidung buntu", "sumbat"],
            "sneezing": ["bersin", "bersin-bersin"],
            "wheezing": ["mengi", "napas berbunyi"],
            "chest_pain": ["nyeri dada", "sakit dada", "dada sakit"],
            "chest_tightness": ["dada sesak", "sesak dada"],
            "rapid_breathing": ["napas cepat", "napas terengah"],
            "cough_with_phlegm": ["batuk berdahak", "dahak"],
            "dry_cough": ["batuk kering"],
            "headache": ["sakit kepala", "pusing", "kepala sakit", "pening"],
            "stiff_neck": ["kaku leher", "leher kaku"],
            "dizziness": ["pusing", "kliyengan"],
            "vertigo": ["vertigo", "pusing berputar"],
            "confusion": ["bingung", "kebingungan"],
            "seizure": ["kejang"],
            "numbness": ["kesemutan", "mati rasa", "kebas"],
            "weakness": ["lemas", "lemah", "kelemahan"],
            "memory_loss": ["lupa", "kehilangan memori"],
            "vision_blurred": ["penglihatan kabur", "mata kabur", "kabur"],
            "double_vision": ["penglihatan ganda", "dobel"],
            "nausea": ["mual", "eneg"],
            "vomiting": ["muntah"],
            "diarrhea": ["diare", "mencret"],
            "constipation": ["sembelit", "susah bab"],
            "abdominal_pain": ["nyeri perut", "sakit perut", "perut sakit"],
            "stomach_cramps": ["kram perut", "perut kram"],
            "bloating": ["kembung", "perut kembung"],
            "loss_of_appetite": ["tidak nafsu makan", "hilang nafsu makan", "tidak lapar"],
            "excessive_thirst": ["haus", "haus terus"],
            "difficulty_swallowing": ["sulit menelan", "susah menelan"],
            "loss_of_smell": ["hilang penciuman", "tidak bisa mencium"],
            "loss_of_taste": ["hilang pengecap", "tidak bisa merasakan"],
            "ear_pain": ["nyeri telinga", "sakit telinga"],
            "hearing_loss": ["gangguan pendengaran", "tidak bisa dengar"],
            "ringing_ears": ["telinga berdenging", "denging"],
            "rash": ["ruam", "bintik merah"],
            "itching": ["gatal"],
            "hives": ["biduran"],
            "skin_redness": ["kemerahan", "kulit merah"],
            "swelling": ["bengkak", "pembengkakan"],
            "watery_eyes": ["mata berair"],
            "red_eyes": ["mata merah"],
            "fatigue": ["lelah", "capek", "kelelahan"],
            "body_aches": ["nyeri badan", "pegal"],
            "muscle_pain": ["nyeri otot", "otot sakit"],
            "joint_pain": ["nyeri sendi", "sendi sakit"],
            "chills": ["menggigil", "kedinginan"],
            "night_sweats": ["keringat malam"],
            "frequent_urination": ["sering kencing", "sering buang air kecil"],
            "painful_urination": ["nyeri kencing", "sakit kencing"],
            "blood_in_urine": ["darah dalam urine", "kencing berdarah"],
            "irregular_heartbeat": ["jantung tidak teratur", "detak tidak teratur"],
            "high_blood_pressure": ["tekanan darah tinggi", "hipertensi"],
            "low_blood_pressure": ["tekanan darah rendah", "hipotensi"],
            "pale_skin": ["pucat"],
            "weight_loss": ["berat badan turun", "kurus"],
            "weight_gain": ["berat badan naik", "gemuk"],
            "anxiety": ["cemas", "kecemasan"],
            "sleep_disturbance": ["gangguan tidur", "susah tidur", "insomnia"],
            "snoring": ["mendengkur", "ngorok"],
            "daytime_sleepiness": ["kantuk", "ngantuk"],
            "facial_pain": ["nyeri wajah", "wajah sakit"],
            "eye_discharge": ["mata berair", "kotoran mata"],
        }
        
        for symptom_key, symptom_label in self.symptoms_map:
            # Gunakan keyword mapping jika ada
            if symptom_key in keyword_mapping:
                keywords = keyword_mapping[symptom_key]
            else:
                # Fallback: gunakan label sebagai keyword
                keywords = [symptom_label.lower()]
            
            patterns[symptom_key] = keywords
        
        return patterns
    
    def detect_symptoms(self, text: str) -> Tuple[Set[str], List[str]]:
        """
        Deteksi gejala dari teks input
        
        Returns:
            (detected_symptom_keys, detected_symptom_labels)
        """
        text_lower = text.lower()
        detected_keys = set()
        detected_labels = []
        
        # Cari setiap gejala
        for symptom_key, keywords in self.keyword_patterns.items():
            for keyword in keywords:
                # Gunakan word boundary untuk menghindari false positive
                pattern = r'\b' + re.escape(keyword) + r'\b'
                if re.search(pattern, text_lower):
                    detected_keys.add(symptom_key)
                    # Cari label yang sesuai
                    for key, label in self.symptoms_map:
                        if key == symptom_key:
                            detected_labels.append(label)
                            break
                    break  # Sudah ketemu, tidak perlu cek keyword lain
        
        return detected_keys, detected_labels
    
    def extract_bmi_info(self, text: str) -> dict:
        """
        Ekstrak informasi berat dan tinggi dari teks
        
        Returns:
            dict dengan keys: weight, height (atau None jika tidak ditemukan)
        """
        result = {"weight": None, "height": None}
        
        # Pattern untuk berat (kg atau lbs)
        weight_patterns = [
            r'berat\s*(?:badan)?\s*(\d+(?:\.\d+)?)\s*(?:kg|kilo)?',
            r'(\d+(?:\.\d+)?)\s*kg',
            r'bb\s*(\d+(?:\.\d+)?)',
        ]
        
        # Pattern untuk tinggi (cm atau m)
        height_patterns = [
            r'tinggi\s*(?:badan)?\s*(\d+(?:\.\d+)?)\s*(?:cm|centi)?',
            r'(\d+(?:\.\d+)?)\s*cm',
            r'tb\s*(\d+(?:\.\d+)?)',
        ]
        
        text_lower = text.lower()
        
        # Cari berat
        for pattern in weight_patterns:
            match = re.search(pattern, text_lower)
            if match:
                try:
                    result["weight"] = float(match.group(1))
                    break
                except (ValueError, IndexError):
                    pass
        
        # Cari tinggi
        for pattern in height_patterns:
            match = re.search(pattern, text_lower)
            if match:
                try:
                    result["height"] = float(match.group(1))
                    break
                except (ValueError, IndexError):
                    pass
        
        return result


def generate_response(detected_symptoms: List[str], results: List[dict], 
                     bmi_info: dict = None) -> str:
    """
    Generate response natural untuk chatbot
    
    Args:
        detected_symptoms: list of detected symptom labels
        results: hasil dari inference engine
        bmi_info: informasi BMI jika ada
    
    Returns:
        Response text
    """
    if not detected_symptoms and not results:
        return ("Maaf, saya tidak mendeteksi gejala spesifik dari pesan Anda. "
                "Coba sebutkan gejala yang Anda alami, misalnya: "
                "'Saya merasa demam dan batuk' atau 'Saya pusing dan mual'.")
    
    response_parts = []
    
    # Konfirmasi gejala yang terdeteksi
    if detected_symptoms:
        if len(detected_symptoms) == 1:
            response_parts.append(f"Saya mendeteksi gejala: **{detected_symptoms[0]}**.")
        else:
            symptoms_str = ", ".join(detected_symptoms[:-1]) + f" dan {detected_symptoms[-1]}"
            response_parts.append(f"Saya mendeteksi gejala: **{symptoms_str}**.")
    
    # Informasi BMI jika ada
    if bmi_info and bmi_info.get("bmi"):
        response_parts.append(f"\nBMI Anda: **{bmi_info['bmi']}** ({bmi_info['bmi_category']})")
    
    # Hasil diagnosa
    if results:
        response_parts.append("\n### 📋 Hasil Analisis:\n")
        
        for idx, result in enumerate(results[:3], 1):  # Tampilkan top 3
            priority_label = {
                0: "🚨 DARURAT",
                1: "⚠️ SEGERA",
                2: "📌 OBSERVASI",
                3: "ℹ️ INFORMASI"
            }.get(result["priority"], "ℹ️")
            
            response_parts.append(
                f"{idx}. **{result['conclusion']}** {priority_label}\n"
                f"   - Tingkat kecocokan: {result['match_percentage']}%\n"
                f"   - Saran: {result['advice']}\n"
            )
    else:
        response_parts.append(
            "\n⚠️ Tidak ada kondisi spesifik yang cocok dengan gejala Anda. "
            "Jika gejala berlanjut atau memburuk, segera konsultasi dengan dokter."
        )
    
    # Footer disclaimer
    response_parts.append(
        "\n---\n"
        "💡 **Catatan**: Ini adalah analisis awal dari sistem pakar. "
        "Untuk diagnosa akurat, silakan konsultasi dengan tenaga medis profesional."
    )
    
    return "\n".join(response_parts)
