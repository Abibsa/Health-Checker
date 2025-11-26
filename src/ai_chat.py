"""
AI Chat Integration using Google Gemini API
"""
import os
import google.generativeai as genai
from typing import Optional

class HealthChatAI:
    """AI Chatbot untuk konsultasi kesehatan menggunakan Gemini"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini AI
        
        Args:
            api_key: Google Gemini API key (optional, akan cari di env var)
        """
        # Coba ambil dari parameter atau environment variable
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY tidak ditemukan. "
                "Set environment variable atau pass sebagai parameter."
            )
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        
        # Setup model - gunakan gemini-2.5-flash (available model)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # System prompt untuk health assistant
        self.system_prompt = """Anda adalah Health Assistant AI, asisten kesehatan virtual yang membantu pengguna menganalisis gejala mereka.

PERAN ANDA:
- Anda adalah asisten kesehatan yang ramah, empatik, dan profesional
- Anda membantu pengguna memahami gejala mereka dan memberikan saran awal
- Anda BUKAN dokter dan TIDAK memberikan diagnosa medis final

CARA ANDA BEKERJA:
1. Dengarkan keluhan pengguna dengan seksama
2. Tanyakan pertanyaan follow-up jika perlu untuk memahami lebih detail
3. Berikan analisis berdasarkan gejala yang disebutkan
4. Sarankan tindakan yang tepat (istirahat, ke dokter, UGD, dll)
5. Selalu ingatkan bahwa ini bukan pengganti konsultasi dokter

GAYA KOMUNIKASI:
- Gunakan bahasa Indonesia yang natural dan mudah dipahami
- Ramah tapi tetap profesional
- Empati terhadap kondisi pengguna
- Jangan gunakan istilah medis yang terlalu teknis kecuali perlu
- Berikan jawaban yang terstruktur dan mudah dibaca

BATASAN:
- JANGAN memberikan diagnosa pasti
- JANGAN meresepkan obat spesifik
- JANGAN memberikan saran medis yang berbahaya
- SELALU sarankan konsultasi dokter untuk kondisi serius
- Untuk gejala darurat (demam tinggi, sesak napas parah, nyeri dada, dll), SEGERA sarankan ke UGD

PRIORITAS KONDISI:
🚨 DARURAT (segera ke UGD):
- Demam >39°C yang tidak turun
- Sesak napas berat
- Nyeri dada
- Kejang
- Pendarahan hebat
- Kehilangan kesadaran

⚠️ SEGERA (konsultasi dokter hari ini):
- Demam tinggi >38°C lebih dari 3 hari
- Muntah terus menerus
- Diare parah
- Sakit kepala hebat
- Gejala yang memburuk

📌 OBSERVASI (pantau 1-2 hari):
- Demam ringan <38°C
- Batuk pilek ringan
- Sakit kepala ringan
- Kelelahan

ℹ️ PERAWATAN MANDIRI:
- Gejala ringan yang umum
- Istirahat cukup
- Minum air putih
- Obat bebas jika perlu

Selalu akhiri dengan disclaimer: "Ini adalah saran awal. Untuk diagnosa akurat, silakan konsultasi dengan dokter."
"""
        
        # Initialize chat session
        self.chat = self.model.start_chat(history=[])
    
    def send_message(self, user_message: str) -> str:
        """
        Kirim pesan ke AI dan dapatkan response
        
        Args:
            user_message: Pesan dari user
            
        Returns:
            Response dari AI
        """
        try:
            # Gabungkan system prompt dengan user message untuk context
            full_message = f"{self.system_prompt}\n\nUser: {user_message}\n\nAssistant:"
            
            # Generate response
            response = self.chat.send_message(full_message)
            
            return response.text
            
        except Exception as e:
            return f"Maaf, terjadi kesalahan: {str(e)}"
    
    def reset_conversation(self):
        """Reset percakapan (mulai dari awal)"""
        self.chat = self.model.start_chat(history=[])
