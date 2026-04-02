import streamlit as st
import fitz  # PyMuPDF
from src.image_extractor import extract_images
from src.generate_ddr import generate_ddr

st.set_page_config(page_title="AI DDR Generator", layout="wide")

st.title("🏗️ AI DDR Report Generator")

inspection_file = st.file_uploader("Upload Inspection Report", type=["pdf"])
thermal_file = st.file_uploader("Upload Thermal Report", type=["pdf"])

def extract_text(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if st.button("Generate DDR"):
    if inspection_file and thermal_file:

        with st.spinner("Processing reports..."):

            # Extract text
            inspection_text = extract_text(inspection_file)
            thermal_text = extract_text(thermal_file)

            # Extract OCR text from images
            inspection_images_text = extract_images(inspection_file)
            thermal_images_text = extract_images(thermal_file)

            # Combine everything
            context = f"""
INSPECTION TEXT:
{inspection_text}

THERMAL TEXT:
{thermal_text}

INSPECTION OCR TEXT:
{inspection_images_text}

THERMAL OCR TEXT:
{thermal_images_text}
"""

            # Generate DDR
            report = generate_ddr(context)

        st.success("DDR Generated Successfully!")

        st.subheader("📄 Generated Report")
        st.write(report)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="DDR_Report.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please upload both files.")
