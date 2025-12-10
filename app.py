from flask import Flask, render_template, request, jsonify, session
from src.inference_engine import infer
from src.nlp_processor import SymptomDetector, generate_response
from src.ai_chat import HealthChatAI
from src.health_metrics import (
    calculate_bmi, 
    bmi_category, 
    get_ideal_weight_range, 
    calculate_weight_difference,
    get_bmi_category_details,
    estimate_bmr,
    m_from_cm,
    m_from_in
)
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize AI Chat (akan error jika tidak ada API key, tapi kita handle di route)
try:
    # Untuk development lokal, bisa langsung pakai API key
    # Untuk production/GitHub, hapus parameter api_key ini dan pakai .env
    ai_chat = HealthChatAI(api_key="AIzaSyBRjRmOJJIpUNhU4tb8ezWzDk2KOk3P0s4")
    AI_ENABLED = True
except Exception as e:
    print(f"Warning: AI Chat tidak tersedia: {e}")
    print("Chatbot akan menggunakan rule-based fallback.")
    AI_ENABLED = False

# Gejala dikategorikan untuk UI yang lebih baik
SYMPTOM_CATEGORIES = {
    "Pernapasan": [
        ("fever", "Demam"),
        ("cough", "Batuk"),
        ("sore_throat", "Sakit Tenggorokan"),
        ("shortness_of_breath", "Sesak Napas"),
        ("runny_nose", "Hidung Berair"),
        ("congested_nose", "Hidung Tersumbat"),
        ("sneezing", "Bersin-bersin"),
        ("wheezing", "Mengi (Napas Berbunyi)"),
        ("chest_pain", "Nyeri Dada"),
        ("chest_tightness", "Dada Terasa Sesak"),
        ("rapid_breathing", "Napas Cepat"),
        ("cough_with_phlegm", "Batuk Berdahak"),
        ("dry_cough", "Batuk Kering"),
    ],
    "Neurologis": [
        ("headache", "Sakit Kepala"),
        ("stiff_neck", "Kaku Leher"),
        ("dizziness", "Pusing"),
        ("vertigo", "Vertigo (Pusing Berputar)"),
        ("confusion", "Kebingungan"),
        ("seizure", "Kejang"),
        ("numbness", "Kesemutan/Mati Rasa"),
        ("weakness", "Kelemahan Otot"),
        ("memory_loss", "Kehilangan Memori"),
        ("vision_blurred", "Penglihatan Kabur"),
        ("double_vision", "Penglihatan Ganda"),
    ],
    "Pencernaan": [
        ("nausea", "Mual"),
        ("vomiting", "Muntah"),
        ("diarrhea", "Diare"),
        ("constipation", "Sembelit"),
        ("abdominal_pain", "Nyeri Perut"),
        ("stomach_cramps", "Kram Perut"),
        ("bloating", "Perut Kembung"),
        ("loss_of_appetite", "Kehilangan Nafsu Makan"),
        ("excessive_thirst", "Rasa Haus Berlebihan"),
        ("difficulty_swallowing", "Sulit Menelan"),
    ],
    "Indra": [
        ("loss_of_smell", "Hilang Indra Penciuman"),
        ("loss_of_taste", "Hilang Indra Pengecap"),
        ("ear_pain", "Nyeri Telinga"),
        ("hearing_loss", "Gangguan Pendengaran"),
        ("ringing_ears", "Telinga Berdenging"),
        ("eye_discharge", "Keluarnya Cairan dari Mata"),
    ],
    "Kulit & Alergi": [
        ("rash", "Ruam Kulit"),
        ("itching", "Gatal-gatal"),
        ("hives", "Biduran"),
        ("skin_redness", "Kemerahan pada Kulit"),
        ("swelling", "Pembengkakan"),
        ("watery_eyes", "Mata Berair"),
        ("red_eyes", "Mata Merah"),
    ],
    "Sistemik": [
        ("fatigue", "Kelelahan"),
        ("body_aches", "Nyeri Badan"),
        ("muscle_pain", "Nyeri Otot"),
        ("joint_pain", "Nyeri Sendi"),
        ("chills", "Menggigil"),
        ("night_sweats", "Keringat Malam"),
        ("frequent_urination", "Sering Buang Air Kecil"),
        ("painful_urination", "Nyeri Saat Buang Air Kecil"),
        ("blood_in_urine", "Darah dalam Urine"),
        ("irregular_heartbeat", "Detak Jantung Tidak Teratur"),
        ("high_blood_pressure", "Tekanan Darah Tinggi"),
        ("low_blood_pressure", "Tekanan Darah Rendah"),
        ("pale_skin", "Kulit Pucat"),
        ("weight_loss", "Penurunan Berat Badan"),
        ("weight_gain", "Kenaikan Berat Badan"),
        ("anxiety", "Kecemasan"),
        ("sleep_disturbance", "Gangguan Tidur"),
        ("snoring", "Mendengkur"),
        ("daytime_sleepiness", "Kantuk di Siang Hari"),
        ("facial_pain", "Nyeri Wajah"),
    ],
}

# Flatten untuk backward compatibility
SYMPTOMS = []
for category, symptoms in SYMPTOM_CATEGORIES.items():
    SYMPTOMS.extend(symptoms)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/diagnosa", methods=["GET"])
def diagnose():
    return render_template("diagnose.html", symptoms=SYMPTOMS, symptom_categories=SYMPTOM_CATEGORIES)

@app.route("/check", methods=["POST"])
def check():
    selected = request.form.getlist("symptom")
    metrics = None
    metrics_error = None

    units = request.form.get("units", "metric")
    weight_raw = (request.form.get("weight") or "").strip()
    height_raw = (request.form.get("height") or "").strip()

    if weight_raw or height_raw:
        if not weight_raw or not height_raw:
            metrics_error = "Berat dan tinggi harus diisi lengkap untuk menghitung BMI."
        else:
            try:
                weight = float(weight_raw)
                height = float(height_raw)
                bmi_raw, bmi_display = calculate_bmi(weight, height, units=units)
                metrics = {
                    "weight": weight,
                    "height": height,
                    "units": units,
                    "bmi_raw": bmi_raw,
                    "bmi": bmi_display,
                    "bmi_category": bmi_category(bmi_raw),
                }
            except ValueError as exc:
                metrics_error = str(exc)

    results = infer(selected, metrics=metrics)
    # Create symptom map for easier lookup in template
    symptom_map = dict(SYMPTOMS)
    return render_template(
        "result.html",
        selected=selected,
        results=results,
        symptoms=SYMPTOMS,
        symptom_map=symptom_map,
        metrics=metrics,
        metrics_error=metrics_error,
    )

# Admin page to view rules (simple, read-only)
@app.route("/admin", methods=["GET"])
def admin():
    # load rules summary from data file
    import json
    rules_path = os.path.join(os.path.dirname(__file__), "data", "rules.json")
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = json.load(f)
    # Create symptom mapping for display
    symptom_map = dict(SYMPTOMS)
    return render_template("admin.html", rules=rules, symptom_map=symptom_map)


@app.route("/bmi", methods=["GET", "POST"])
def bmi_page():
    result = None
    error = None
    defaults = {"units": "metric", "name": "", "weight": "", "height": ""}

    if request.method == "POST":
        defaults["units"] = request.form.get("units", "metric")
        defaults["name"] = request.form.get("name", "").strip()
        defaults["weight"] = request.form.get("weight", "")
        defaults["height"] = request.form.get("height", "")
        try:
            weight = float(defaults["weight"])
            height = float(defaults["height"])
            bmi_raw, bmi_display = calculate_bmi(weight, height, units=defaults["units"])
            
            # Convert to metric for calculations
            if defaults["units"] == "imperial":
                weight_kg = weight * 0.45359237
                height_m = height * 0.0254
                height_cm = height * 2.54
            else:
                weight_kg = weight
                height_m = height * 0.01
                height_cm = height
            
            # Calculate additional metrics
            ideal_min, ideal_max = get_ideal_weight_range(height_m)
            weight_diff = calculate_weight_difference(weight_kg, ideal_min, ideal_max)
            category_details = get_bmi_category_details(bmi_raw)
            bmr = estimate_bmr(weight_kg, height_cm)
            
            result = {
                "name": defaults["name"] or "Anda",
                "weight": weight,
                "height": height,
                "weight_kg": round(weight_kg, 1),
                "height_m": round(height_m, 2),
                "height_cm": round(height_cm, 1),
                "units": defaults["units"],
                "bmi_raw": bmi_raw,
                "bmi": bmi_display,
                "bmi_category": bmi_category(bmi_raw),
                "ideal_weight_min": ideal_min,
                "ideal_weight_max": ideal_max,
                "weight_difference": weight_diff,
                "category_details": category_details,
                "bmr": bmr,
            }
        except ValueError as exc:
            error = str(exc)
        except TypeError:
            error = "Berat dan tinggi harus berupa angka."

    return render_template(
        "bmi.html",
        result=result,
        error=error,
        defaults=defaults,
    )

@app.route("/compare", methods=["GET", "POST"])
def compare_page():
    error = None
    compare_error = None
    defaults = {"name": "", "height": "", "gender": "male"}
    comparison_defaults = [{"name": "", "height": "", "gender": ""} for _ in range(3)]
    comparison_results = []

    if request.method == "POST":
        defaults["name"] = request.form.get("name", "").strip()
        defaults["height"] = request.form.get("height", "")
        defaults["gender"] = request.form.get("gender", "male")
        
        if not defaults["name"]:
            error = "Nama harus diisi."
        elif not defaults["height"]:
            error = "Tinggi harus diisi."
        else:
            try:
                main_height = float(defaults["height"])
                if main_height <= 0:
                    error = "Tinggi harus lebih besar dari 0."
            except ValueError:
                error = "Tinggi harus berupa angka."

        compare_names = request.form.getlist("compare_name")
        compare_heights = request.form.getlist("compare_height")
        compare_genders = request.form.getlist("compare_gender")
        comparison_defaults = [
            {"name": n, "height": h, "gender": g} for n, h, g in zip(compare_names, compare_heights, compare_genders)
        ]
        while len(comparison_defaults) < 3:
            comparison_defaults.append({"name": "", "height": "", "gender": ""})
        
        temp_results = []
        
        # Add main person
        if defaults["name"] and defaults["height"]:
            try:
                main_height_val = float(defaults["height"])
                if main_height_val > 0:
                    temp_results.append({
                        "name": defaults["name"],
                        "height_cm": main_height_val,
                        "gender": defaults["gender"] or "male"
                    })
            except ValueError:
                pass

        # Add comparison profiles
        for name, height_txt, gender in zip(compare_names, compare_heights, compare_genders):
            name = (name or "").strip()
            height_txt = (height_txt or "").strip()
            gender = (gender or "").strip()
            if not name and not height_txt:
                continue
            if not height_txt:
                compare_error = f"Tinggi untuk {name or 'profil'} harus diisi."
                continue
            try:
                height_val = float(height_txt)
                if height_val <= 0:
                    raise ValueError
            except ValueError:
                compare_error = f"Tinggi {height_txt} tidak valid."
                continue
            temp_results.append({
                "name": name or "Tanpa Nama",
                "height_cm": height_val,
                "gender": gender or "male"
            })

        if temp_results:
            max_height = max(r["height_cm"] for r in temp_results)
            for item in temp_results:
                percent = (item["height_cm"] / max_height) * 100 if max_height else 0
                item["percent"] = percent
            comparison_results = temp_results

    # Create height labels for the chart (0 to 210 in increments of 10)
    height_labels = list(range(0, 211, 10))
    
    return render_template(
        "compare.html",
        error=error,
        defaults=defaults,
        comparison_defaults=comparison_defaults,
        comparison_results=comparison_results,
        compare_error=compare_error,
        height_labels=height_labels,
    )

# Keep old /metrics route for backwards compatibility
@app.route("/metrics", methods=["GET", "POST"])
def metrics_page():
    result = None
    error = None
    compare_error = None
    defaults = {"units": "metric", "name": "", "weight": "", "height": ""}
    comparison_defaults = [{"name": "", "height": ""} for _ in range(3)]
    comparison_results = []

    if request.method == "POST":
        defaults["units"] = request.form.get("units", "metric")
        defaults["name"] = request.form.get("name", "").strip()
        defaults["weight"] = request.form.get("weight", "")
        defaults["height"] = request.form.get("height", "")
        try:
            weight = float(defaults["weight"])
            height = float(defaults["height"])
            bmi_raw, bmi_display = calculate_bmi(weight, height, units=defaults["units"])
            result = {
                "name": defaults["name"] or "Anda",
                "weight": weight,
                "height": height,
                "units": defaults["units"],
                "bmi_raw": bmi_raw,
                "bmi": bmi_display,
                "bmi_category": bmi_category(bmi_raw),
            }
        except ValueError as exc:
            error = str(exc)
        except TypeError:
            error = "Berat dan tinggi harus berupa angka."

        compare_names = request.form.getlist("compare_name")
        compare_heights = request.form.getlist("compare_height")
        if compare_names or compare_heights:
            comparison_defaults = [
                {"name": n, "height": h} for n, h in zip(compare_names, compare_heights)
            ]
            while len(comparison_defaults) < 3:
                comparison_defaults.append({"name": "", "height": ""})
            temp_results = []
            for name, height_txt in zip(compare_names, compare_heights):
                name = (name or "").strip()
                height_txt = (height_txt or "").strip()
                if not name and not height_txt:
                    continue
                if not height_txt:
                    compare_error = f"Tinggi untuk {name or 'profil'} harus diisi."
                    continue
                try:
                    height_val = float(height_txt)
                    if height_val <= 0:
                        raise ValueError
                except ValueError:
                    compare_error = f"Tinggi {height_txt} tidak valid."
                    continue
                temp_results.append({"name": name or "Tanpa Nama", "height_cm": height_val})

            # Add main person to comparison if they have name and height
            if result and result.get("name") and result.get("height"):
                main_height_cm = result["height"]
                if result["units"] == "imperial":
                    # Convert inches to cm
                    main_height_cm = main_height_cm * 2.54
                temp_results.insert(0, {
                    "name": result["name"],
                    "height_cm": main_height_cm
                })

            if temp_results:
                max_height = max(r["height_cm"] for r in temp_results)
                for item in temp_results:
                    percent = (item["height_cm"] / max_height) * 100 if max_height else 0
                    item["percent"] = percent
                comparison_results = temp_results

    return render_template(
        "metrics.html",
        result=result,
        error=error,
        defaults=defaults,
        comparison_defaults=comparison_defaults,
        comparison_results=comparison_results,
        compare_error=compare_error,
    )

# Initialize symptom detector
symptom_detector = SymptomDetector(SYMPTOMS)

@app.route("/chat", methods=["GET"])
def chat_page():
    """Halaman chatbot"""
    return render_template("chat.html")

@app.route("/chat/api", methods=["POST"])
def chat_api():
    """API endpoint untuk chatbot - menggunakan AI jika tersedia"""
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        use_ai = data.get("use_ai", True)  # Default gunakan AI jika tersedia
        
        if not user_message:
            return jsonify({
                "success": False,
                "error": "Pesan tidak boleh kosong"
            }), 400
        
        # Jika AI enabled dan user mau pakai AI
        if AI_ENABLED and use_ai:
            try:
                # Gunakan Gemini AI
                ai_response = ai_chat.send_message(user_message)
                
                return jsonify({
                    "success": True,
                    "response": ai_response,
                    "mode": "ai",
                    "detected_symptoms": [],
                    "results": []
                })
            except Exception as ai_error:
                print(f"AI Error: {ai_error}")
                # Fallback ke rule-based jika AI error
                pass
        
        # Fallback: Gunakan rule-based system
        # Deteksi gejala dari teks
        detected_keys, detected_labels = symptom_detector.detect_symptoms(user_message)
        
        # Ekstrak informasi BMI jika ada
        bmi_info_raw = symptom_detector.extract_bmi_info(user_message)
        bmi_info = None
        
        # Hitung BMI jika berat dan tinggi tersedia
        if bmi_info_raw["weight"] and bmi_info_raw["height"]:
            try:
                weight = bmi_info_raw["weight"]
                height = bmi_info_raw["height"]
                bmi_raw, bmi_display = calculate_bmi(weight, height, units="metric")
                bmi_info = {
                    "weight": weight,
                    "height": height,
                    "bmi_raw": bmi_raw,
                    "bmi": bmi_display,
                    "bmi_category": bmi_category(bmi_raw),
                }
            except ValueError:
                pass
        
        # Jalankan inference engine
        results = infer(list(detected_keys), metrics=bmi_info)
        
        # Generate response
        response_text = generate_response(detected_labels, results, bmi_info)
        
        return jsonify({
            "success": True,
            "response": response_text,
            "mode": "rule-based",
            "detected_symptoms": detected_labels,
            "results": results[:3] if results else []  # Top 3 results
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Terjadi kesalahan: {str(e)}"
        }), 500


if __name__ == "__main__":
    # Use debug=False for production
    app.run(host='0.0.0.0', port=5000, debug=True)
