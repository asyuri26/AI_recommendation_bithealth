# 🧠 AI-based Department Recommendation - BitHealth

Proyek ini merupakan aplikasi berbasis **FastAPI** yang memanfaatkan **LLM (Large Language Model)** untuk merekomendasikan **departemen medis** berdasarkan gejala yang diberikan oleh pengguna. Aplikasi ini cocok untuk digunakan dalam proses triase awal secara otomatis dalam sistem kesehatan digital.

---

## 🚀 Fitur Utama

- Form input sederhana berbasis HTML
- Proses rekomendasi departemen menggunakan LLM dan prompt dinamis
- Endpoint API yang fleksibel: respon HTML (untuk browser) & JSON (untuk Swagger/API)
- Swagger UI otomatis tersedia untuk testing dan dokumentasi

---

## 🛠 Tools & Teknologi

| Tools            | Deskripsi                                |
|------------------|--------------------------------------------|
| 🐍 Python        | Bahasa pemrograman utama                  |
| ⚡ FastAPI       | Web framework asynchronous                |
| 🔮 OpenAI / LLM  | Model bahasa besar untuk analisis gejala |
| 🧾 Jinja2        | Template engine untuk HTML rendering      |
| 🌐 HTML/CSS      | Tampilan user form                        |
| 🧪 Swagger UI    | Interface interaktif untuk testing API    |
| 🚀 Uvicorn       | ASGI server untuk menjalankan aplikasi    |

---

## 📁 Struktur Proyek

bithealth/
├── llm_utils/
│ ├── config.py # Konfigurasi LLM/API
│ └── prompt.py # Template prompt dan contoh
├── templates/
│ ├── form.html # Form input pengguna
│ └── result.html # Hasil rekomendasi
├── example_dataset.json # Contoh dataset gejala
├── main.py # File utama aplikasi FastAPI
├── requirements.txt # Daftar dependencies
└── README.md # Dokumentasi proyek

yaml
Copy
Edit

---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/asyuri26/AI_recommendation-bithealth.git
cd AI_recommendation-bithealth
2. Buat Virtual Environment (opsional tapi direkomendasikan)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # MacOS/Linux
venv\Scripts\activate           # Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Jalankan Aplikasi
bash
Copy
Edit
uvicorn main:app --reload
5. Akses Aplikasi
Form HTML (User Interface):
http://127.0.0.1:8000/

Swagger UI (Testing API):
http://127.0.0.1:8000/docs

📌 Catatan Tambahan
Pastikan koneksi internet aktif jika menggunakan OpenAI API.

Endpoint /api/recommend akan otomatis menyesuaikan response:

Browser → Tampilkan HTML

API Client / Swagger → Tampilkan JSON

Jika kamu menggunakan OpenAI, pastikan API Key sudah diatur (bisa disimpan di .env atau langsung dalam config.py).

👨‍💻 Author
Made with ❤️ by asyuri26

yaml
Copy
Edit
