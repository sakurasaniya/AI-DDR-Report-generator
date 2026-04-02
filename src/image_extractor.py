import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# ✅ FIX: Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_images(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_text = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image = Image.open(io.BytesIO(image_bytes))

            # OCR
            text = pytesseract.image_to_string(image)

            if text and text.strip():
                extracted_text.append(text.strip())

    # 🔥 CRITICAL FIX (prevents empty embeddings error)
    if not extracted_text:
        return "No text found in images"

    return "\n".join(extracted_text)