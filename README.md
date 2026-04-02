# 🏗️ AI DDR Generator (Detailed Defect Report)

## 📌 Overview
This project is an AI-powered system that converts raw inspection and thermal reports into a structured, client-ready Detailed Defect Report (DDR).

It processes both textual and visual data from PDFs and generates a professional engineering report.

---

## 🚀 Features
- Extracts text from PDF reports
- Performs OCR on embedded images
- Combines inspection + thermal data
- Generates structured DDR using LLM
- Handles missing or unclear data gracefully
- Downloadable report output

---

## 🧠 Tech Stack
- Frontend: Streamlit
- Backend: Python
- PDF Processing: PyMuPDF
- OCR: Tesseract
- AI Model: DeepSeek (LLM)
- Libraries: LangChain (optional), dotenv

---

## ⚙️ How It Works
1. Upload inspection and thermal reports
2. Extract text using PyMuPDF
3. Extract image data using OCR (Tesseract)
4. Combine all extracted data
5. Generate DDR using LLM
6. Display and download report

---

## ⚠️ Limitations
- OCR accuracy depends on image quality
- No direct image embedding in report (future improvement)
- Noisy data may affect output clarity

---

## 🔮 Future Improvements
- Embed images directly into DDR
- Improve OCR with advanced models
- Better structured data extraction
- Enhanced UI/UX

---


---

## 👩‍💻 Author
Rajama
