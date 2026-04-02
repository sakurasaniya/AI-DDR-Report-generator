from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_pdf(text, path="data/output/ddr_report.pdf"):
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    y = height - 40

    for line in text.split("\n"):
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()