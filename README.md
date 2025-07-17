# AI-based Department Recommendation - BitHealth

Proyek ini merupakan aplikasi berbasis **FastAPI** yang memanfaatkan **LLM (Large Language Model)** untuk merekomendasikan **departemen medis** berdasarkan gejala yang diberikan oleh pengguna. Aplikasi ini cocok untuk digunakan dalam proses triase awal secara otomatis dalam sistem kesehatan digital.

---

## Fitur Utama

- Form input sederhana berbasis HTML
- Proses rekomendasi departemen menggunakan LLM (model gpt-4o-mini) dan prompt dinamis 
- Endpoint API yang fleksibel: respon HTML (untuk browser) & JSON (untuk Swagger/API)
- Swagger UI otomatis tersedia untuk testing dan dokumentasi

---

## 🧠 Cara Kerja Web Rekomendasi

1. **Input Form Pengguna**
   - User mengisi **gender**, **usia**, dan **daftar gejala** dalam form HTML. Seperti contoh, male, 30, pusing, mual, dan sakit pinggang.

2. **Parsing dan Preprocessing**
   - Gejala yang diketik (dipisah koma) akan diproses menjadi list Python dan dibersihkan dari spasi.

3. **Prompt Engineering**
   - Sistem mengambil **beberapa contoh kasus (few-shot learning)** dan menggabungkannya dengan input pengguna untuk membentuk *prompt dinamis*.

4. **Prediksi dengan LLM**
   - Prompt dikirim ke model **GPT-4o-mini** melalui API untuk memprediksi **departemen medis yang sesuai** (misal: “Neurology”, “Cardiology”, dll).

---

## 🛠 Tools & Teknologi

| Tools            | Deskripsi                                |
|------------------|--------------------------------------------|
| 🐍 Python        | Bahasa pemrograman utama                  |
| ⚡ FastAPI       | Web framework asynchronous                |
| 🔮 OpenAI / LLM (gpt-4o-mini)   | Model bahasa besar untuk analisis gejala |
| 🧾 Jinja2        | Template engine untuk HTML rendering      |
| 🌐 HTML          | Tampilan user form                        |
| 🧪 Swagger UI    | Interface interaktif untuk testing API    |
| 🚀 Uvicorn       | Server untuk menjalankan aplikasi    |

---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/asyuri26/AI_recommendation-bithealth.git
cd AI_recommendation-bithealth
```

2. Buat Virtual Environment (opsional tapi direkomendasikan)
```bash
python -m venv venv
source venv/bin/activate # MacOS/Linux
venv\Scripts\activate  # Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Jalankan Aplikasi
```bash
uvicorn main:app --reload
```

5. Akses Aplikasi
``` bash
Form HTML (User Interface):
http://127.0.0.1:8000/

Swagger UI (Testing API):
http://127.0.0.1:8000/docs
```

Author
Made by asyuri26
